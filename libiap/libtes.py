# -*- coding: utf-8 -*-

"""libtes module
This module may deprecate in future.
Please use libiap.openapi when possible for better upstream support.
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
