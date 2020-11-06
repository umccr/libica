# -*- coding: utf-8 -*-

"""libconsole module
This module may deprecate in future.
Please use libiap.openapi when possible for better upstream support.
"""
import warnings

from libiap import rest, __alpha_deprecation__

warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)


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
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_health_endpoint(**kwargs), **kwargs)
    return client.get()


def list_regions(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_regions_endpoint(**kwargs), **kwargs)
    return client.get()


def get_account(account_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_accounts_endpoint(**kwargs) + f"/{account_id}", **kwargs)
    return client.get()


def get_token_details(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_tokens_endpoint(**kwargs) + f"/details", **kwargs)
    return client.get()


def get_usage(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_usages_endpoint(**kwargs), **kwargs)
    return client.get()


def get_usage_details(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_usages_endpoint(**kwargs) + f"/details", **kwargs)
    return client.get()
