import gzip
import logging
from contextlib import closing
from tempfile import NamedTemporaryFile
from typing import List
from urllib.parse import urlparse, urlunsplit, quote_plus, unquote_plus

import requests

from libica.app.projectops import ProjectOps
from libica.openapi.v2 import ApiException, ApiClient
from libica.openapi.v2.api.project_data_api import ProjectDataApi
from libica.openapi.v2.model.download import Download
from libica.openapi.v2.model.project import Project
from libica.openapi.v2.model.project_data import ProjectData
from libica.openapi.v2.model.project_data_paged_list import ProjectDataPagedList

logger = logging.getLogger(__name__)

URI_SCHEME = "icav2"


def to_uri(project_name: str, file_path: str) -> str:
    """Warning Experimental
    NOTE: this is still experimental and early adopter of the following proposal in discussion
    https://github.com/umccr-illumina/ica_v2/issues/96

    It mimics the GDS scheme as follows:
        THEN
            gds://volume_name/path/to/folder/file.txt
        NOW
            icav2://owning-project-name/path/to/folder/
            icav2://owning-project-name/path/to/file.txt
    """
    netloc = quote_plus(project_name, safe="/")
    path_ = quote_plus(file_path, safe="/")
    return urlunsplit((URI_SCHEME, netloc, path_, "", ""))


def from_uri(icav2_uri: str) -> tuple:
    """
    Inverse of to_uri()
    """
    if not icav2_uri.startswith(URI_SCHEME):
        raise ValueError(f"Unrecognised protocol scheme: {icav2_uri}")

    icav2_url_obj = urlparse(icav2_uri)
    return unquote_plus(icav2_url_obj.netloc), unquote_plus(icav2_url_obj.path)


class ProjectDataOpsFactory(ProjectOps):

    def __init__(self, api_client: ApiClient = None):
        super(ProjectDataOpsFactory, self).__init__(api_client=api_client)

    def from_uri(self, icav2_uri: str):
        project_name, path_ = from_uri(icav2_uri=icav2_uri)
        project = self.get_project_by_name(project_name=project_name)
        return ProjectDataOps(project_id=project.id, file_path=path_, api_client=self.api_client)


class ProjectDataOps(ProjectOps):
    """Usage:
    Create ProjectDataOps either using constructor or through available ProjectDataOpsFactory methods.

    Domain model UML class diagram is as follows:
        ProjectDataOps
            - private project: Project
            - private file_path: Any(str | List[str])

    The project property is bind at construction time that can't be changed after instantiated.
    The file_path property, however, is allowed to mutate throughout ProjectDataOps object life cycle.
    """

    def __init__(self, project_id: str, file_path=None, api_client: ApiClient = None):
        super(ProjectDataOps, self).__init__(api_client=api_client)
        self._project = self.get_project_by_id(project_id=project_id)
        self.__set_path(file_path=file_path)

    def __set_path(self, file_path):
        if file_path is None:
            self._file_path = []  # everything underneath of this project
        elif isinstance(file_path, str):
            self._file_path = [file_path]  # wrap str into list

    @property
    def project(self) -> Project:
        return self._project

    @property
    def file_path(self) -> List[str]:
        return self._file_path

    @file_path.setter
    def file_path(self, file_path):
        self.__set_path(file_path=file_path)

    def cd(self, file_path):
        self.__set_path(file_path=file_path)

    def check_path(self) -> list:
        """Use cases
        This behaves like UNIX `ls` command whereas you can check an absolute path to file or a directory.
        You can use it to check whether a file exist in ProjectData because it raises FileNotFoundError.
        Otherwise, it returns file(s) found.

        NOTE: This wrap list_files but more strict to raise FileNotFoundError if zero match.

        :return: List of ProjectData objects
        :rtype: list[ProjectData]
        """

        files = self.list_files()
        if len(files) == 0:
            raise FileNotFoundError(f"No file(s) found in project {self.project.name} at {self.file_path}")
        return files

    def get_file_to_bytes(self) -> bytes:
        """
        get_object_to_bytes API, with on-the-fly gzip detection and decompression

        :return bytes: bytes from the decompressed File body
        """
        file_path = self.file_path[0]
        try:
            ntf = self.download_file()
            if file_path.endswith(".gz"):
                obj_bytes = gzip.decompress(ntf.read())
            else:
                obj_bytes = ntf.read()
            ntf.close()
            return obj_bytes
        except Exception as e:
            message = f"Failed on reading the specified file in project {self.project.name} at {file_path}"
            raise FileNotFoundError(f"{message} Exception: {e}")

    def yield_data(self, page_size=1000):
        """Use cases
        Generator-based data lister for given project and paths.
        It will yield data by paginated chunks. Default page size chunk is 1000.
        If paths are not specified, it will return listing of all data under given project.
        Listing is recursive in nature for the path.
        The path can also be an absolute path for a data object.

        :param page_size:
        """

        with closing(self.api_client) as ctx_api_client:
            project_data_api: ProjectDataApi = ProjectDataApi(api_client=ctx_api_client)

            try:
                page_token = ""
                while True:
                    project_data_paged_list: ProjectDataPagedList = project_data_api.get_project_data_list(
                        project_id=self.project.id,
                        file_path=self.file_path,
                        page_size=str(page_size),
                        page_token=page_token,
                    )

                    yield project_data_paged_list.items

                    page_token = project_data_paged_list.next_page_token
                    if not project_data_paged_list.next_page_token:
                        break

            except ApiException as e:
                logger.error(e)

    def list_files(self, page_size=1000, suffix: str = "") -> list:
        """Use cases
        Get file listing for given project and paths.
        If paths are not specified, it will return listing of all files under given project.
        Listing is recursive in nature for folder path.
        You can still specify an absolute path for a file.

        :param page_size:
        :param suffix:
        :return: List of ProjectData objects
        :rtype: list[ProjectData]
        """
        items = []

        if suffix:
            for chunks in self.yield_data(page_size=page_size):
                for chunk in chunks:
                    project_data: ProjectData = chunk
                    if project_data.data.details is not None:
                        if str(project_data.data.details.path).endswith(suffix):
                            items.append(project_data)
        else:
            for chunks in self.yield_data(page_size=page_size):
                items.extend(chunks)

        return items

    def get_download_by_file_id(self, file_id) -> Download:
        with closing(self.api_client) as ctx_api_client:
            project_data_api: ProjectDataApi = ProjectDataApi(api_client=ctx_api_client)
            dl: Download = project_data_api.create_download_url_for_data(
                project_id=self.project.id,
                data_id=file_id,
            )
            return dl

    def get_download(self) -> (Download, None):
        file_path = self.file_path[0]

        logger.info(f"Downloading file from project {self.project.name} at {file_path}")

        file_list = self.list_files()

        if not len(file_list) == 1:
            logger.warning(f"Please specify a single file. "
                           f"Found {len(file_list)} files in project {self.project.name} at {file_path}")
            return None

        if len(file_list) == 0:
            logger.warning(f"File not found in in project {self.project.name} at {file_path}")
            return None

        prj_data: ProjectData = file_list[0]

        return self.get_download_by_file_id(prj_data.data.id)

    def create_presigned_url(self) -> str:
        return self.get_download().url

    def crete_presigned_url_by_file_id(self, file_id: str) -> (bool, str):
        try:
            dl = self.get_download_by_file_id(file_id)
            return True, dl.url
        except ApiException as e:
            message = f"Failed to sign the specified file {file_id} in project {self.project.name}. Exception - {e}"
            logger.error(message)
            return False, message

    def download_file(self) -> (NamedTemporaryFile, None):
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

        :return NamedTemporaryFile: or None if file is not found or multiple files are found
        """
        presigned_url = self.create_presigned_url()

        req = requests.get(presigned_url)

        ntf = NamedTemporaryFile()
        with open(ntf.name, 'wb') as f:
            f.write(req.content)

        return ntf


class BundleDataOps:
    # TODO
    pass
