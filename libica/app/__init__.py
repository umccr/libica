# -*- coding: utf-8 -*-
"""app package

ImplNote:
Consider implementation here should be reusable application needs for common use cases.
Consider not to re-do openapi generality.
"""
import logging
import os
from enum import Enum

from libumccr.aws import libsm

logger = logging.getLogger(__name__)

ICA_BASE_URL = "https://aps2.platform.illumina.com"
ICA_TOKEN_SECRET_NAME = "IcaSecretsPortal"


class ENSEventType(Enum):
    """
    REF:
    https://support-docs.illumina.com/SW/ICA/Content/SW/ICA/ENS_AvailableEvents.htm
    """
    GDS_FILES = "gds.files"
    BSSH_RUNS = "bssh.runs"
    WES_RUNS = "wes.runs"


class GDSFilesEventType(Enum):
    """
    REF:
    https://support-docs.illumina.com/SW/ICA/Content/SW/ICA/ENS_AvailableEvents.htm
    """
    UPLOADED = "uploaded"
    DELETED = "deleted"
    ARCHIVED = "archived"
    UNARCHIVED = "unarchived"

    @classmethod
    def from_value(cls, value):
        if value == cls.UPLOADED.value:
            return cls.UPLOADED
        elif value == cls.DELETED.value:
            return cls.DELETED
        elif value == cls.ARCHIVED.value:
            return cls.ARCHIVED
        elif value == cls.UNARCHIVED.value:
            return cls.UNARCHIVED
        else:
            raise ValueError(f"No matching enum found for value: {value}")


def configuration(lib, secret_name=None, base_url=None, debug=False):
    ica_access_token = os.getenv("ICA_ACCESS_TOKEN", None)
    if ica_access_token is None and secret_name:
        ica_access_token = libsm.get_secret(secret_name=secret_name)
    elif ica_access_token is None:
        ica_access_token = libsm.get_secret(secret_name=ICA_TOKEN_SECRET_NAME)

    ica_base_url = os.getenv("ICA_BASE_URL", None)
    if ica_base_url is None and base_url:
        ica_base_url = base_url
    elif ica_base_url is None:
        ica_base_url = ICA_BASE_URL

    config = lib.Configuration(
        host=ica_base_url,
        api_key={
            'Authorization': ica_access_token
        },
        api_key_prefix={
            'Authorization': "Bearer"
        },
    )

    # WARNING:
    # it print stdout all libica.openapi http calls activity including JWT token in http header
    config.debug = debug

    return config
