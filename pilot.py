# -*- coding: utf-8 -*-

"""pilot module

Pilot run or Integration Test (IT) i.e. it will hit IAP web services endpoints.
Instead of mocking IAP responses as contrast to unit test cases.

Need to set the following Mandatory environment variable.
If Optional environment variables are set, they will be used.
Otherwise, Pilot will auto-discover and fly-through randomly!

Mandatory:
export IAP_BASE_URL=<baseUrl>
export IAP_AUTH_TOKEN=<tok>

Optional:
IAP_GDS_VOLUME
IAP_GDS_FILE
IAP_GDS_FOLDER
IAP_GDS_FOLDER_SESSION
IAP_TES_TASK_ID
IAP_TES_RUN_ID
IAP_TES_TASK_VERSION_ID
IAP_WES_WORKFLOW_ID
IAP_WES_RUN_ID
IAP_WES_SIGNAL_ID
IAP_WES_WORKFLOW_VERSION_NAME
IAP_ENS_SUBSCRIPTION_ID
IAP_ACCOUNT_ID

Usage: python pilot.py
"""
import inspect
import os
import random
import sys

from libiap import libgds, libtes, libwes, libens, libconsole


def _getenv(var: str, bag):
    env_var = os.getenv(var.upper(), None)
    if env_var:
        return env_var
    elif len(bag) > 0:
        env_var = bag[random.randint(0, len(bag) - 1)]
    else:
        print(f"{str(var).upper()} is not defined")
    return env_var


def _gds():
    volumes = []
    for volume in libgds.list_volumes(page_size=10):
        print(volume)
        volumes.append(volume['name'])

    iap_gds_volume = _getenv('iap_gds_volume', volumes)

    print(libgds.get_volume(volume_id=iap_gds_volume))

    files = []
    for file in libgds.list_files(volume_name=iap_gds_volume):
        print(file)
        files.append(file['id'])

    iap_gds_file = _getenv('iap_gds_file', files)
    print(libgds.get_file(file_id=iap_gds_file))

    folders = []
    for folder in libgds.list_folders(volume_name=iap_gds_volume):
        print(folder)
        folders.append(folder['id'])

    iap_gds_folder = _getenv('iap_gds_folder', folders)

    print(libgds.get_folder(folder_id=iap_gds_folder))

    iap_gds_folder_session = os.getenv('IAP_GDS_FOLDER_SESSION', None)
    if iap_gds_folder_session is not None:
        print(libgds.get_folder_session(iap_gds_folder, iap_gds_folder_session))
    else:
        print("IAP_GDS_FOLDER_SESSION is not defined")


def _tes():
    tasks = []
    for task in libtes.list_tasks():
        print(task)
        tasks.append(task['id'])

    iap_tes_task_id = _getenv('iap_tes_task_id', tasks)
    print(libtes.get_task(task_id=iap_tes_task_id))

    runs = []
    for task_run in libtes.list_task_runs():
        print(task_run)
        runs.append(task_run['id'])

    iap_tes_run_id = _getenv('iap_tes_run_id', runs)
    print(libtes.get_task_run(run_id=iap_tes_run_id))

    versions = []
    for version in libtes.list_task_versions(task_id=iap_tes_task_id):
        print(version)
        versions.append(version['id'])

    iap_tes_task_version_id = _getenv('iap_tes_task_version_id', versions)
    print(libtes.get_task_version(iap_tes_task_id, iap_tes_task_version_id))


def _wes():
    workflows = []
    for workflow in libwes.list_workflows():
        print(workflow)
        workflows.append(workflow['id'])

    iap_wes_workflow_id = _getenv('iap_wes_workflow_id', workflows)
    print(libwes.get_workflow(workflow_id=iap_wes_workflow_id))

    runs = []
    for workflow_run in libwes.list_workflow_runs():
        print(workflow_run)
        runs.append(workflow_run['id'])

    iap_wes_run_id = _getenv('iap_wes_run_id', runs)

    print(libwes.get_workflow_run(run_id=iap_wes_run_id))

    for history in libwes.list_workflow_run_history(run_id=iap_wes_run_id):
        print(history)

    for signal in libwes.list_signals():
        print(signal)

    iap_wes_signal_id = os.getenv('IAP_WES_SIGNAL_ID', None)
    if iap_wes_signal_id is not None:
        print(libwes.get_signal(signal_id=iap_wes_signal_id))
    else:
        print('IAP_WES_SIGNAL_ID is not defined')

    for all_ver in libwes.list_all_workflow_versions():
        print(all_ver)

    versions = []
    for version in libwes.list_workflow_versions(workflow_id=iap_wes_workflow_id):
        print(version)
        versions.append(version['version'])

    iap_wes_workflow_version_name = _getenv('iap_wes_workflow_version_name', versions)
    print(libwes.get_workflow_version(iap_wes_workflow_id, iap_wes_workflow_version_name))


def _ens():
    subscriptions = []
    for sub in libens.list_subscriptions():
        print(sub)
        subscriptions.append(sub['id'])

    iap_ens_subscription_id = _getenv('iap_ens_subscription_id', subscriptions)
    print(libens.get_subscription(subscription_id=iap_ens_subscription_id))


def _console():
    print(libconsole.get_token_details())

    iap_account_id = os.getenv('IAP_ACCOUNT_ID', libconsole.get_token_details()['uid'])
    print(libconsole.get_account(account_id=iap_account_id))

    print(libconsole.get_service_health())

    print(libconsole.list_regions())

    print(libconsole.get_usage())

    print(libconsole.get_usage_details())


if __name__ == '__main__':
    pilot = sys.modules[__name__]
    all_functions = inspect.getmembers(pilot, inspect.isfunction)
    for key, value in all_functions:
        if str(inspect.signature(value)) == "()":
            value()
