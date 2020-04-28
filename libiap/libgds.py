# -*- coding: utf-8 -*-

"""libgds module

Module interface for underlay GDS API operations
https://aps2.platform.illumina.com/gds/swagger/index.html

Loosely based on design patterns: Facade, Adapter/Wrapper

Should retain/suppress all IAP GDS API calls here, including handle
any specific exceptions and data type that need for processing response.

Goal is, so that else where in code, it does not need to call and handle
API responses directly, but just import libgds and use it!

If unsure, start with Pass-through call.

Example usage:
 - See unit test cases in tests/test_libgds.py
"""

import copy
import logging
import os

import requests

logger = logging.getLogger(__name__)

DEFAULT_PAGE_SIZE = 1000


def _base_url(**kwargs):
    iap_base_url = kwargs.get('iap_base_url', None)
    if iap_base_url is None:
        iap_base_url = os.getenv('IAP_BASE_URL', None)
    assert iap_base_url is not None, "IAP_BASE_URL is not defined"
    return iap_base_url


def _volumes_endpoint(**kwargs):
    return _base_url(**kwargs) + "/v1/volumes"


def _files_endpoint(**kwargs):
    return _base_url(**kwargs) + "/v1/files"


def _headers(**kwargs):
    iap_auth_token = kwargs.get('iap_auth_token', None)
    if iap_auth_token is None:
        iap_auth_token = os.getenv('IAP_AUTH_TOKEN', None)
    assert iap_auth_token is not None, "IAP_AUTH_TOKEN is not defined"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(iap_auth_token)
    }
    return headers


def _build(ep_callback, **kwargs):
    headers = _headers(**kwargs)
    ep = ep_callback(**kwargs)
    return ep, headers


def _response(response):
    logger.debug(response.url)
    if response.status_code != 200:
        raise response.raise_for_status()
    return response.json()


def _params(**kwargs):
    params = {}

    page_size = kwargs.get('page_size', None)
    page_token = kwargs.get('page_token', None)
    volume_name = kwargs.get('volume_name', None)
    volume_id = kwargs.get('volume_id', None)

    if page_token:
        params.update(pageToken=page_token)
    elif page_size:
        params.update(pageSize=page_size)
    else:
        params.update(pageSize=DEFAULT_PAGE_SIZE)

    if volume_name:
        params.update({"volume.name": volume_name})
    elif volume_id:
        params.update({"volume.id": volume_id})

    return copy.deepcopy(params)


def _paginated_list(ep, headers, **kwargs):
    params = _params(**kwargs)
    page = _response(requests.get(ep, params=params, headers=headers))

    logger.debug(params)
    logger.debug(kwargs.keys())

    for item in page['items']:
        yield item

    if 'nextPageToken' in page:
        kwargs.update(page_token=page['nextPageToken'])
        yield from _paginated_list(ep, headers, **kwargs)


def list_files(volume_name, **kwargs):
    ep, headers = _build(_files_endpoint, **kwargs)
    yield from _paginated_list(ep, headers, volume_name=volume_name, **kwargs)


def get_file(file_id, **kwargs):
    ep, headers = _build(_files_endpoint, **kwargs)
    return _response(requests.get(ep + f"/{file_id}", headers=headers))


def list_volumes(**kwargs):
    ep, headers = _build(_volumes_endpoint, **kwargs)
    yield from _paginated_list(ep, headers, **kwargs)


def get_volume(volume_id, **kwargs):
    ep, headers = _build(_volumes_endpoint, **kwargs)
    return _response(requests.get(ep + f"/{volume_id}", headers=headers))
