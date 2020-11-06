# -*- coding: utf-8 -*-

"""libens module
This module may deprecate in future.
Please use libiap.openapi when possible for better upstream support.
"""
import warnings

from libiap import rest, __alpha_deprecation__

warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)


def _subscriptions_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/subscriptions"


def list_subscriptions(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_subscriptions_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_subscription(subscription_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_subscriptions_endpoint(**kwargs) + f"/{subscription_id}", **kwargs)
    return client.get()
