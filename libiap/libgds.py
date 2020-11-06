# -*- coding: utf-8 -*-

"""libgds module
This module may deprecate in future.
Please use libiap.openapi when possible for better upstream support.
"""
import warnings

from libiap import rest, __alpha_deprecation__

warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)


def _volumes_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/volumes"


def _files_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/files"


def _folders_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/folders"


def list_files(volume_name, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_files_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(volume_name=volume_name, **kwargs)


def get_file(file_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_files_endpoint(**kwargs) + f"/{file_id}", **kwargs)
    return client.get()


def list_folders(volume_name, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_folders_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(volume_name=volume_name, **kwargs)


def get_folder(folder_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_folders_endpoint(**kwargs) + f"/{folder_id}", **kwargs)
    return client.get()


def get_folder_session(folder_id, session_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_folders_endpoint(**kwargs) + f"/{folder_id}/sessions/{session_id}", **kwargs)
    return client.get()


def list_volumes(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_volumes_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_volume(volume_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_volumes_endpoint(**kwargs) + f"/{volume_id}", **kwargs)
    return client.get()
