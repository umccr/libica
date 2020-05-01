# -*- coding: utf-8 -*-

"""libwes module

Facade module interface for underlay WES API operations
https://aps2.platform.illumina.com/wes/swagger/index.html

Should retain/suppress all IAP WES API calls here, including handle
any specific exceptions.

Goal is, so that else where in code, just ``import libwes`` and use it!

If unsure, start with Pass-through call.

Example usage:
 - See unit test cases in tests/test_libwes.py
"""


from libiap import rest


def _workflows_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/workflows"


def _workflows_runs_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/workflows/runs"


def _workflows_signals_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/workflows/signals"


def list_workflows(**kwargs):
    client = rest.build(_workflows_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_workflow(workflow_id, **kwargs):
    client = rest.build(_workflows_endpoint(**kwargs) + f"/{workflow_id}", **kwargs)
    return client.get()


def list_workflow_runs(**kwargs):
    client = rest.build(_workflows_runs_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_workflow_run(run_id, **kwargs):
    client = rest.build(_workflows_runs_endpoint(**kwargs) + f"/{run_id}", **kwargs)
    return client.get()


def list_workflow_run_history(run_id, **kwargs):
    client = rest.build(_workflows_runs_endpoint(**kwargs) + f"/{run_id}/history", **kwargs)
    yield from client.paginated_list(**kwargs)


def list_signals(**kwargs):
    client = rest.build(_workflows_signals_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_signal(signal_id, **kwargs):
    client = rest.build(_workflows_signals_endpoint(**kwargs) + f"/{signal_id}", **kwargs)
    return client.get()


def list_all_workflow_versions(**kwargs):
    client = rest.build(_workflows_endpoint(**kwargs) + f"/versions", **kwargs)
    yield from client.paginated_list(**kwargs)


def list_workflow_versions(workflow_id, **kwargs):
    client = rest.build(_workflows_endpoint(**kwargs) + f"/{workflow_id}/versions", **kwargs)
    yield from client.paginated_list(**kwargs)


def get_workflow_version(workflow_id, version_name, **kwargs):
    client = rest.build(_workflows_endpoint(**kwargs) + f"/{workflow_id}/versions/{version_name}", **kwargs)
    return client.get()
