# -*- coding: utf-8 -*-

"""libwes module
This module may deprecate in future.
Please use libiap.openapi when possible for better upstream support.
"""
import warnings

from libiap import rest, __alpha_deprecation__

warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)


def _workflows_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/workflows"


def _workflows_runs_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/workflows/runs"


def _workflows_signals_endpoint(**kwargs):
    return rest.base_url(**kwargs) + "/v1/workflows/signals"


def list_workflows(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_workflow(workflow_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_endpoint(**kwargs) + f"/{workflow_id}", **kwargs)
    return client.get()


def list_workflow_runs(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_runs_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_workflow_run(run_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_runs_endpoint(**kwargs) + f"/{run_id}", **kwargs)
    return client.get()


def list_workflow_run_history(run_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_runs_endpoint(**kwargs) + f"/{run_id}/history", **kwargs)
    yield from client.paginated_list(**kwargs)


def list_signals(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_signals_endpoint(**kwargs), **kwargs)
    yield from client.paginated_list(**kwargs)


def get_signal(signal_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_signals_endpoint(**kwargs) + f"/{signal_id}", **kwargs)
    return client.get()


def list_all_workflow_versions(**kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_endpoint(**kwargs) + f"/versions", **kwargs)
    yield from client.paginated_list(**kwargs)


def list_workflow_versions(workflow_id, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_endpoint(**kwargs) + f"/{workflow_id}/versions", **kwargs)
    yield from client.paginated_list(**kwargs)


def get_workflow_version(workflow_id, version_name, **kwargs):
    warnings.warn(__alpha_deprecation__, DeprecationWarning, stacklevel=2)
    client = rest.build(_workflows_endpoint(**kwargs) + f"/{workflow_id}/versions/{version_name}", **kwargs)
    return client.get()
