# -*- coding: utf-8 -*-

"""libens module
This module may deprecate in future.
Please use libiap.openapi when possible for better upstream support.
"""

from libiap import rest


def _subscriptions_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/subscriptions"


def list_subscriptions(**kwargs):
    client = rest.build(_subscriptions_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_subscription(subscription_id, **kwargs):
    client = rest.build(_subscriptions_endpoint(**kwargs) + f"/{subscription_id}", **kwargs)
    return client.get()
