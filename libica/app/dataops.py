import gzip
import logging
from contextlib import closing
from tempfile import NamedTemporaryFile

import requests

from libica.app import AppHelper
from libica.openapi.v2 import ApiException, ApiClient
from libica.openapi.v2.api.project_data_api import ProjectDataApi
from libica.openapi.v2.model.download import Download
from libica.openapi.v2.model.project_data import ProjectData
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList

logger = logging.getLogger(__name__)


class ProjectDataOps:

    def __init__(self, project_id: str, api_client: ApiClient = None):
        self.project_id: str = project_id

        if api_client:
            self.api_client = api_client
        else:
            # otherwise, we build api_client with standard lookup from well-known locations
            self.api_client: ApiClient = AppHelper().build_icav2_configuration().get_icav2_api_client()

    def check_path(self, file_path: str) -> list:
        """Use cases
        This behaves like UNIX `ls` command whereas you can check an absolute path to file or a directory.
        You can use it to check whether a file exist in GDS because it raises FileNotFoundError.
        Otherwise, it returns file(s) found.

        NOTE: This wrap list_files but more strict to raise FileNotFoundError if zero match.

        :param file_path:
        :return: List of ProjectData objects
        :rtype: list[ProjectData]
        """

        files = self.list_files(file_path)
        if len(files) == 0:
            raise FileNotFoundError(f"No file(s) found in project {self.project_id} at {file_path}")
        return files

    def get_file_to_bytes(self, file_path: str) -> bytes:
        """
        get_object_to_bytes API, with on-the-fly gzip detection and decompression

        :param file_path:
        :return bytes: bytes from the decompressed File body
        """
        try:
            ntf = self.download_file(file_path)
            if file_path.endswith(".gz"):
                obj_bytes = gzip.decompress(ntf.read())
            else:
                obj_bytes = ntf.read()
            ntf.close()
            return obj_bytes
        except Exception as e:
            message = f"Failed on reading the specified file in project {self.project_id} at {file_path}"
            raise FileNotFoundError(f"{message} Exception: {e}")

    def list_files(self, file_path=None) -> list:
        """Use cases
        Get file listing for given project_id and paths.
        If path are not specified, it will return listing of all files under given project_id.
        Listing is recursive in nature for folder path.
        You can still specify an absolute path for a file.

        :param file_path: default list all
        :return: List of ProjectData objects
        :rtype: list[ProjectData]
        """

        if file_path is None:
            file_path = []  # list everything
        elif isinstance(file_path, str):
            file_path = [file_path]  # wrap str into list

        items = []

        with closing(self.api_client) as ctx_api_client:
            project_data_api: ProjectDataApi = ProjectDataApi(api_client=ctx_api_client)

            try:
                page_token = ""
                while True:
                    project_data_paged_list: ProjectDataPagedList = project_data_api.get_project_data_list(
                        project_id=self.project_id,
                        file_path=file_path,
                        page_size=str(1000),
                        page_token=page_token,
                    )

                    items.extend(project_data_paged_list.items)

                    page_token = project_data_paged_list.next_page_token
                    if not project_data_paged_list.next_page_token:
                        break

            except ApiException as e:
                logger.error(e)

        return items

    def download(self, file_id):
        with closing(self.api_client) as ctx_api_client:
            project_data_api: ProjectDataApi = ProjectDataApi(api_client=ctx_api_client)
            dl: Download = project_data_api.create_download_url_for_data(
                project_id=self.project_id,
                data_id=file_id,
            )
            return dl

    def download_by_file_path(self, file_path: str) -> (Download, None):
        logger.info(f"Downloading file from project_id {self.project_id} at {file_path}")

        file_list = self.list_files(file_path=file_path)

        if not len(file_list) == 1:
            logger.warning(f"Please specify a single file. "
                           f"Found {len(file_list)} files in project_id {self.project_id} at {file_path}")
            return None

        if len(file_list) == 0:
            logger.warning(f"File not found in in project_id {self.project_id} at {file_path}")
            return None

        prj_data: ProjectData = file_list[0]

        return self.download(prj_data.data.id)

    def create_presigned_url(self, file_path: str) -> str:
        return self.download_by_file_path(file_path).url

    def download_file(self, file_path: str) -> (NamedTemporaryFile, None):
        """Retrieve _single_ Project data file

        It collects matching path (one exact file) through list_files().
        Hence, there should only be one item in the list.
        Then, we use requests library to download the file from presigned URL to temporary storage.
        The downloaded file is back by NamedTemporaryFile and, therefore will be deleted once it goes 'out of scope'.

        NOTE:
        If multiple files are found, it warns and return None.

        It is recommended to close NamedTemporaryFile after use.
        For example, work within closing context manager like so.
            with closing(ntf) as f:
                with open(f.name, newline='') as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    ...
                    ...

        :param file_path: the GDS path of the file to download
        :return NamedTemporaryFile: or None if file is not found or multiple files are found
        """
        presigned_url = self.create_presigned_url(file_path)

        req = requests.get(presigned_url)

        ntf = NamedTemporaryFile()
        with open(ntf.name, 'wb') as f:
            f.write(req.content)

        return ntf

    def presign_file(self, file_id: str) -> (bool, str):
        try:
            dl = self.download(file_id)
            return True, dl.url
        except ApiException as e:
            message = f"Failed to sign the specified file {file_id} in project {self.project_id}. Exception - {e}"
            logger.error(message)
            return False, message


class BundleDataOps:
    # TODO
    pass
