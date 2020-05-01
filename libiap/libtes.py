# -*- coding: utf-8 -*-

"""libtes module

Facade module interface for underlay TES API operations
https://aps2.platform.illumina.com/tes/swagger/index.html

Should retain/suppress all IAP TES API calls here, including handle
any specific exceptions.

Goal is, so that else where in code, just ``import libtes`` and use it!

If unsure, start with Pass-through call.

Example usage:
 - See unit test cases in tests/test_libtes.py
"""


from libiap import rest


def _tasks_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/tasks"


def _tasks_runs_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/tasks/runs"


def list_tasks(**kwargs):
    client = rest.build(_tasks_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_task(task_id, **kwargs):
    client = rest.build(_tasks_endpoint(**kwargs) + f"/{task_id}", **kwargs)
    return client.get()


def list_task_runs(**kwargs):
    client = rest.build(_tasks_runs_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_task_run(run_id, **kwargs):
    client = rest.build(_tasks_runs_endpoint(**kwargs) + f"/{run_id}", **kwargs)
    return client.get()


def list_task_versions(task_id, **kwargs):
    client = rest.build(_tasks_endpoint(**kwargs) + f"/{task_id}/versions", **kwargs)
    yield from client.paginated_list(**kwargs)


def get_task_version(task_id, version_id, **kwargs):
    client = rest.build(_tasks_endpoint(**kwargs) + f"/{task_id}/versions/{version_id}", **kwargs)
    return client.get()
