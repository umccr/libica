# -*- coding: utf-8 -*-

"""libconsole module

Facade module interface for underlay Developer Console API operations
https://aps2.platform.illumina.com/console/swagger/index.html

Should retain/suppress all IAP Console API calls here, including handle
any specific exceptions.

Goal is, so that else where in code, just ``import libconsole`` and use it!

If unsure, start with Pass-through call.

Example usage:
 - See unit test cases in tests/test_libconsole.py
"""

from libiap import rest


def _health_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/health"


def _regions_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/regions"


def _accounts_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/accounts"


def _tokens_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/tokens"


def _usages_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/usages"


def get_service_health(**kwargs):
    client = rest.build(_health_endpoint(**kwargs), **kwargs)
    return client.get()


def list_regions(**kwargs):
    client = rest.build(_regions_endpoint(**kwargs), **kwargs)
    return client.get()


def get_account(account_id, **kwargs):
    client = rest.build(_accounts_endpoint(**kwargs) + f"/{account_id}", **kwargs)
    return client.get()


def get_token_details(**kwargs):
    client = rest.build(_tokens_endpoint(**kwargs) + f"/details", **kwargs)
    return client.get()


def get_usage(**kwargs):
    client = rest.build(_usages_endpoint(**kwargs), **kwargs)
    return client.get()


def get_usage_details(**kwargs):
    client = rest.build(_usages_endpoint(**kwargs) + f"/details", **kwargs)
    return client.get()
