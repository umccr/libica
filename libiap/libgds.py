# -*- coding: utf-8 -*-

"""libgds module

Facade module interface for underlay GDS API operations
https://aps2.platform.illumina.com/gds/swagger/index.html

Should retain/suppress all IAP GDS API calls here, including handle
any specific exceptions.

Goal is, so that else where in code, just ``import libgds`` and use it!

If unsure, start with Pass-through call.

Example usage:
 - See unit test cases in tests/test_libgds.py
"""

from libiap import rest


def _volumes_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/volumes"


def _files_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/files"


def _folders_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/folders"


def list_files(volume_name, **kwargs):
    client = rest.build(_files_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(volume_name=volume_name, **kwargs)


def get_file(file_id, **kwargs):
    client = rest.build(_files_endpoint(**kwargs) + f"/{file_id}", **kwargs)
    return client.get()


def list_folders(volume_name, **kwargs):
    client = rest.build(_folders_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(volume_name=volume_name, **kwargs)


def get_folder(folder_id, **kwargs):
    client = rest.build(_folders_endpoint(**kwargs) + f"/{folder_id}", **kwargs)
    return client.get()


def get_folder_session(folder_id, session_id, **kwargs):
    client = rest.build(_folders_endpoint(**kwargs) + f"/{folder_id}/sessions/{session_id}", **kwargs)
    return client.get()


def list_volumes(**kwargs):
    client = rest.build(_volumes_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_volume(volume_id, **kwargs):
    client = rest.build(_volumes_endpoint(**kwargs) + f"/{volume_id}", **kwargs)
    return client.get()
