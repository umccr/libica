# -*- coding: utf-8 -*-
"""gds module

ImplNote:
Consider implementation here should be reusable application specific routines for GDS common use cases.
Consider not to re-do libgds SDK generality.
"""
import gzip
import logging
from tempfile import NamedTemporaryFile
from typing import List
from urllib.parse import urlparse

import boto3
import requests
from botocore.exceptions import ClientError

from libica.app import configuration
from libica.openapi import libgds

logger = logging.getLogger(__name__)


def get_gds_uri(gds_volume_name, gds_path):
    return f"gds://{gds_volume_name}{gds_path}"  # note gds path start with /


def parse_path(gds_path):
    gds_url_obj = urlparse(gds_path)
    return gds_url_obj.netloc, gds_url_obj.path


def check_file(gds_path) -> list:
    """See check_path

    NOTE: This is for "error checking" use case, hence, it may raise FileNotFoundError

    :param gds_path:
    :return:
    """
    vol, path = parse_path(gds_path)
    return check_path(vol, path)


def check_path(volume_name: str, path: str) -> list:
    """Use cases
    This behave like UNIX `ls` command whereas you can check an absolute path to file or a directory.
    You can use it to check whether a file exist in GDS because it raises FileNotFoundError.
    Otherwise, it return file(s) found.

    NOTE: This wrap get_file_list but more strict to raise FileNotFoundError if zero match.

    :param volume_name:
    :param path:
    :return: List of libgds.FileResponse objects
    :rtype: list[FileResponse]
    """

    files = get_file_list(volume_name=volume_name, path=path)
    if len(files) == 0:
        raise FileNotFoundError(f"Could not get file: gds://{volume_name}{path}")
    return files


def get_gds_file_to_bytes(gds_volume_name: str, gds_path: str) -> bytes:
    """
    get_object_to_bytes API, with on-the-fly gzip detection and decompression

    :param gds_volume_name:
    :param gds_path:
    :return bytes: bytes from the decompressed GDS File body
    """
    try:
        ntf = download_gds_file(gds_volume_name, gds_path)
        if gds_path.endswith(".gz"):
            obj_bytes = gzip.decompress(ntf.read())
        else:
            obj_bytes = ntf.read()
        ntf.close()
        return obj_bytes
    except Exception as e:
        message = f"Failed on reading the specified GDS File ({get_gds_uri(gds_volume_name, gds_path)})"
        raise FileNotFoundError(f"{message} Exception: {e}")


def get_file_list(volume_name: str, path: str = "/*") -> list:
    return get_files_list(volume_name=volume_name, paths=[path])


def get_files_list(volume_name: str, paths=None) -> list:
    """Use cases
    Get file listing for given volume_name and paths.
    If path are not specified, it will return listing of all files under given volume_name.
    Listing is recursive in nature for a volume or folder path.
    You can still specify an absolute path for a file.
    PreSignedUrl is always included.

    :param volume_name:
    :param paths: default list all
    :return: List of libgds.FileResponse objects
    :rtype: list[FileResponse]
    """

    if paths is None:
        paths = ["/*"]

    items = []

    with libgds.ApiClient(configuration(libgds)) as api_client:
        files_api = libgds.FilesApi(api_client)
        try:
            page_token = None
            while True:
                file_list: libgds.FileListResponse = files_api.list_files(
                    volume_name=[volume_name],
                    path=paths,
                    include="presignedUrl,totalItemCount",
                    page_size=1000,
                    page_token=page_token,
                )

                items.extend(file_list.items)

                page_token = file_list.next_page_token
                if not file_list.next_page_token:
                    break
            # while end

        except libgds.ApiException as e:
            logger.info("Exception when calling FilesApi: %s\n" % e)

    return items


def download_gds_file(volume_name: str, path: str) -> (NamedTemporaryFile, None):
    """Retrieve _single_ GDS file

    It collects matching path (expect single file) through get_file_list.
    Hence, there should only be one item in the list.
    Then, we use the requests library to download the gds file from presigned URL to temporary storage.
    The downloaded file is back by NamedTemporaryFile and, therefore will be deleted once it goes 'out of scope'.

    NOTE:
    It is caller responsibility to provide an absolute path to a file for the path parameter.
    If multiple files are found, it warns and return None.

    It is recommend to close NamedTemporaryFile after use.
    For example, work within closing context manager like so.
        with closing(ntf) as f:
            with open(f.name, newline='') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                ...
                ...

    :param volume_name:
    :param path: the GDS path of the file to download
    :return NamedTemporaryFile: or None if file is not found or multiple files are found
    """

    logger.info(f"Downloading file from GDS: gds://{volume_name}{path}")

    file_list = get_file_list(volume_name=volume_name, path=path)

    if not len(file_list) == 1:
        logger.warning(f"Please specify a single file. Found {len(file_list)} files at gds://{volume_name}{path}")
        return None

    if len(file_list) == 0:
        logger.warning(f"File not found: gds://{volume_name}{path}")
        return None

    file: libgds.FileResponse = file_list[0]

    gds_req = requests.get(file.presigned_url)

    ntf = NamedTemporaryFile()
    with open(ntf.name, 'wb') as f:
        f.write(gds_req.content)

    return ntf


def presign_gds_file(file_id: str, volume_name: str, path_: str, presigned_url_mode: str = "Attachment") -> (bool, str):
    with libgds.ApiClient(configuration(libgds)) as gds_client:
        files_api = libgds.FilesApi(gds_client)
        try:
            file_details: libgds.FileResponse = files_api.get_file(file_id=file_id,
                                                                   presigned_url_mode=presigned_url_mode)
            return True, file_details.presigned_url
        except libgds.ApiException as e:
            message = f"Failed to sign the specified GDS file (gds://{volume_name}{path_}). Exception - {e}"
            logger.error(message)
            return False, message


def presign_gds_file_with_override(file_id: str, **kwargs) -> (bool, str):
    """Default override option for response_content_type is text/html and response_content_disposition is inline"""
    with libgds.ApiClient(configuration(libgds)) as gds_client:
        files_api = libgds.FilesApi(gds_client)
        try:
            resp: libgds.FileResponse = files_api.update_file(file_id=file_id, include='objectStoreAccess')
            cred: libgds.AwsS3TemporaryUploadCredentials = resp.object_store_access.aws_s3_temporary_upload_credentials

            # See S3 API, "Overriding Response Header Values" section on for all possible override
            # https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html

            expiration = kwargs.get('expiration', 3600)
            response_content_type = kwargs.get('response_content_type', 'text/html')
            response_content_disposition = kwargs.get('response_content_disposition', 'inline')

            s3_client = boto3.client(
                's3',
                aws_access_key_id=cred.access_key_id,
                aws_secret_access_key=cred.secret_access_key,
                aws_session_token=cred.session_token,
                region_name=cred.region,
            )

            signed_url = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': cred.bucket_name,
                    'Key': cred.key_prefix,
                    'ResponseContentType': response_content_type,
                    'ResponseContentDisposition': response_content_disposition,
                },
                ExpiresIn=expiration)
            return True, signed_url
        except libgds.ApiException as e:
            message = f"Failed to sign the GDS file ID ({file_id}). Exception - {e}"
            logger.error(message)
            return False, message
        except ClientError as e:
            message = f"Failed to sign the GDS file ID ({file_id}). Exception - {e}"
            return False, message


def get_file_cred(file_id: str) -> (bool, libgds.AwsS3TemporaryUploadCredentials):
    """Return underlay S3 object store credential details for given GDS File ID with r+w"""
    with libgds.ApiClient(configuration(libgds)) as gds_client:
        files_api = libgds.FilesApi(gds_client)
        try:
            resp: libgds.FileResponse = files_api.update_file(file_id=file_id, include='objectStoreAccess')
            cred: libgds.AwsS3TemporaryUploadCredentials = resp.object_store_access.aws_s3_temporary_upload_credentials
            return True, cred
        except libgds.ApiException as e:
            message = f"Failed to get temporary credentials for GDS file ID ({file_id}). Exception - {e}"
            logger.error(message)
            return False, message


def get_folder_cred(folder_id: str) -> (bool, libgds.AwsS3TemporaryUploadCredentials):
    """Return underlay S3 object store credential details for given GDS Folder ID with r+w"""
    with libgds.ApiClient(configuration(libgds)) as gds_client:
        folders_api = libgds.FoldersApi(gds_client)
        try:
            resp: libgds.FolderResponse = folders_api.update_folder(folder_id=folder_id, include='objectStoreAccess')
            cred: libgds.AwsS3TemporaryUploadCredentials = resp.object_store_access.aws_s3_temporary_upload_credentials
            return True, cred
        except libgds.ApiException as e:
            message = f"Failed to get temporary credentials for GDS folder ID ({folder_id}). Exception - {e}"
            logger.error(message)
            return False, message


def get_files_from_gds_by_suffix(location: str, file_suffix: str) -> List[str]:
    """
    Use case:
        For given gds://vol/path/to/folder find file end with extension defined in file_suffix e.g. '.bam'
        Collect all found and return a list ['gds://location/1.bam', ...]
    """
    volume_name, path_ = parse_path(location)

    file_list = []

    with libgds.ApiClient(configuration(libgds)) as api_client:
        files_api = libgds.FilesApi(api_client)
        try:
            page_token = None
            while True:
                file_list_response: libgds.FileListResponse = files_api.list_files(
                    volume_name=[volume_name],
                    path=[f"{path_}/*"],
                    page_size=1000,
                    page_token=page_token,
                )

                for item in file_list_response.items:
                    file_: libgds.FileResponse = item

                    if file_.name.endswith(file_suffix):
                        file_list.append(f"gds://{file_.volume_name}{file_.path}")

                page_token = file_list_response.next_page_token
                if not file_list_response.next_page_token:
                    break
            # while end

        except libgds.ApiException as e:
            logger.error(f"Exception when calling list_files: \n{e}")

    return file_list
