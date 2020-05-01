# -*- coding: utf-8 -*-

"""libens module

Facade module interface for underlay ENS API operations
https://aps2.platform.illumina.com/ens/swagger/index.html

Should retain/suppress all IAP ENS API calls here, including handle
any specific exceptions.

Goal is, so that else where in code, just ``import libens`` and use it!

If unsure, start with Pass-through call.

Example usage:
 - See unit test cases in tests/test_libens.py
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
