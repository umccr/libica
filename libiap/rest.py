# -*- coding: utf-8 -*-

"""rest module

Adapter/Wrapper module interface for performing `requests` REST API calls,
specifically tailored for handling IAP services endpoints.

Should retain/suppress all requests API calls here, including handle
any specific exceptions and data type that need for processing response.

Goal is, so that else where in code, it does not need to call and handle
API responses directly, but just `from libiap import rest` and use it!
"""

import copy
import logging
import os

import requests

DEFAULT_PAGE_SIZE = 1000

logger = logging.getLogger(__name__)


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


def _response(response: requests.Response):
    logger.debug(response.url)
    if response.status_code != 200:
        raise response.raise_for_status()
    return response.json()


def _params(**kwargs):
    """
    Build query parameters from pass-in kwargs dictionary

    :param kwargs:
    :return: copy of params dict
    """
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


def base_url(**kwargs):
    iap_base_url = kwargs.get('iap_base_url', None)
    if iap_base_url is None:
        iap_base_url = os.getenv('IAP_BASE_URL', None)
    assert iap_base_url is not None, "IAP_BASE_URL is not defined"
    return iap_base_url


def build(endpoint, **kwargs):
    return Client(endpoint, _headers(**kwargs))


class Client:

    def __init__(self, endpoint, headers):
        self.endpoint = endpoint
        self.headers = headers

    def paginated_list(self, **kwargs):
        params = _params(**kwargs)
        resp = requests.get(self.endpoint, params=params, headers=self.headers)
        page = _response(resp)

        logger.debug(params)
        logger.debug(kwargs.keys())

        for item in page['items']:
            yield item

        if 'nextPageToken' in page:
            kwargs.update(page_token=page['nextPageToken'])
            yield from self.paginated_list(**kwargs)

    def get(self, **kwargs):
        params = _params(**kwargs)
        resp = requests.get(self.endpoint, params=params, headers=self.headers)
        return _response(resp)

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass
