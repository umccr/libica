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


__all__ = ['Client']


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

    # gds
    volume_name = kwargs.get('volume_name', None)
    volume_id = kwargs.get('volume_id', None)
    path = kwargs.get('path', None)
    is_uploaded = kwargs.get('is_uploaded', None)
    archive_status = kwargs.get('archive_status', None)
    job_statuses = kwargs.get('job_statuses', None)

    # ens
    event_type = kwargs.get('event_type', None)

    # console
    instrument_type = kwargs.get('instrument_type', None)
    version = kwargs.get('version', None)
    periods = kwargs.get('periods', None)
    period_id = kwargs.get('period_id', None)

    # pagination
    page_size = kwargs.get('page_size', None)
    page_token = kwargs.get('page_token', None)

    # optional params
    names = kwargs.get('names', None)
    acls = kwargs.get('acls', None)
    versions = kwargs.get('versions', None)
    ids = kwargs.get('ids', None)
    tenant_id = kwargs.get('tenant_id', None)
    include = kwargs.get('include', None)
    sort = kwargs.get('sort', None)
    status = kwargs.get('status', None)

    if volume_name:
        params.update({"volume.name": volume_name})
    elif volume_id:
        params.update({"volume.id": volume_id})

    if path:
        params.update(path=path)

    if is_uploaded:
        params.update(isUploaded=is_uploaded)

    if archive_status:
        params.update(archiveStatus=archive_status)

    if job_statuses:
        params.update(jobStatuses=job_statuses)

    if event_type:
        params.update(eventType=event_type)

    if instrument_type:
        params.update(instrumentType=instrument_type)

    if version:
        params.update(version=version)

    if periods:
        params.update(periods=periods)

    if period_id:
        params.update(periodId=period_id)

    if page_token:
        params.update(pageToken=page_token)
    elif page_size:
        params.update(pageSize=page_size)
    else:
        params.update(pageSize=DEFAULT_PAGE_SIZE)

    if names:
        params.update(names=names)

    if acls:
        params.update(acls=acls)

    if versions:
        params.update(versions=versions)

    if ids:
        params.update(ids=ids)

    if tenant_id:
        params.update(tenantId=tenant_id)

    if include:
        params.update(include=include)

    if sort:
        params.update(sort=sort)

    if status:
        params.update(status=status)

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
