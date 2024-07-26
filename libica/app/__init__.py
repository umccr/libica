# -*- coding: utf-8 -*-
"""app package

ImplNote:
Consider implementation here should be reusable application needs for common use cases.
Consider not to re-do openapi generality.
"""
import copy
import logging
import os
from enum import Enum
from os.path import expanduser

import yaml

from libica.app.utils import aws

logger = logging.getLogger(__name__)

# v1
ICA_BASE_URL = "https://aps2.platform.illumina.com"
ICA_TOKEN_SECRET_NAME = "IcaSecretsPortal"  # pragma: allowlist secret

# v2
ICA_URL = "https://ica.illumina.com/ica/rest"
ICAV2_TOKEN_SECRET_NAME = "Icav2SecretsPortal"  # pragma: allowlist secret
ICAV2_API_KEY_SECRET_NAME = "Icav2ApiKeySecretsPortal"  # pragma: allowlist secret


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
        ica_access_token = aws.get_secret(secret_name=secret_name)
    elif ica_access_token is None:
        ica_access_token = aws.get_secret(secret_name=ICA_TOKEN_SECRET_NAME)

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
    # it prints stdout all libica.openapi http calls activity including JWT token in http header
    config.debug = debug

    return config


class ProjectDataType(Enum):
    FILE = "FILE"
    FOLDER = "FOLDER"

    @classmethod
    def from_value(cls, value):
        if str(value).lower() == str(cls.FILE.value).lower():
            return cls.FILE
        elif str(value).lower() == str(cls.FOLDER.value).lower():
            return cls.FOLDER
        else:
            raise ValueError(f"No matching enum found for value: {value}")


class AppHelper:

    def __init__(self, secret_name=None, ica_url=None, debug=False):
        self.session_file = expanduser("~/.icav2/.session.ica.yaml")
        self.secret_name = secret_name
        self.ica_url = ica_url
        self.debug = debug
        self.configuration = None

    def get_icav2_cli_session_file(self):
        return self.session_file

    def get_configuration(self):
        return self.configuration

    def get_icav2_cli_session(self) -> dict:
        try:
            with open(self.session_file, 'r') as f:
                session = yaml.safe_load(f)
                session['access_token'] = session.pop('access-token') if 'access-token' in session.keys() else None
                session['project_id'] = session.pop('project-id') if 'project-id' in session.keys() else None
                return copy.deepcopy(session)
        except FileNotFoundError as fnf:
            logger.info("Session file not found")
            logger.debug(fnf)
            return {}

    def get_icav2_cli_session_project_id(self):
        session = self.get_icav2_cli_session()
        project_id = os.getenv("ICAV2_PROJECT_ID", session.get('project_id'))
        return project_id

    def build_icav2_configuration(self):
        from libica.openapi.v2 import Configuration

        _icav2_access_token = os.getenv("ICAV2_ACCESS_TOKEN", None)
        if _icav2_access_token is None and self.secret_name:
            _icav2_access_token = aws.get_secret(secret_name=self.secret_name)
        elif _icav2_access_token is None:
            _icav2_access_token = aws.get_secret(secret_name=ICAV2_TOKEN_SECRET_NAME)

        _ica_url = os.getenv("ICA_URL", None)
        if _ica_url is None and self.ica_url:
            _ica_url = self.ica_url
        elif _ica_url is None:
            _ica_url = ICA_URL

        self.configuration = Configuration(
            host=_ica_url,
            access_token=_icav2_access_token,
        )

        self.configuration.debug = self.debug

        return self

    def build_icav2_configuration_with_cli_session(self):
        from libica.openapi.v2 import Configuration

        _icav2_access_token = os.getenv("ICAV2_ACCESS_TOKEN", self.get_icav2_cli_session()['access_token'])
        if _icav2_access_token is None and self.secret_name:
            _icav2_access_token = aws.get_secret(secret_name=self.secret_name)
        elif _icav2_access_token is None:
            _icav2_access_token = aws.get_secret(secret_name=ICAV2_TOKEN_SECRET_NAME)

        _ica_url = os.getenv("ICA_URL", None)
        if _ica_url is None and self.ica_url:
            _ica_url = self.ica_url
        elif _ica_url is None:
            _ica_url = ICA_URL

        self.configuration = Configuration(
            host=_ica_url,
            access_token=_icav2_access_token,
        )

        self.configuration.debug = self.debug

        return self

    def build_icav2_configuration_with_api_key(self, bearer=False):
        from libica.openapi.v2 import Configuration

        _icav2_api_key = os.getenv("ICAV2_API_KEY", None)
        if _icav2_api_key is None and self.secret_name:
            _icav2_api_key = aws.get_secret(secret_name=self.secret_name)
        elif _icav2_api_key is None:
            _icav2_api_key = aws.get_secret(secret_name=ICAV2_API_KEY_SECRET_NAME)

        _ica_url = os.getenv("ICA_URL", None)
        if _ica_url is None and self.ica_url:
            _ica_url = self.ica_url
        elif _ica_url is None:
            _ica_url = ICA_URL

        self.configuration = Configuration(
            host=_ica_url,
            api_key={
                'ApiKeyAuth': _icav2_api_key,
            },
        )

        if bearer:
            self.configuration.api_key_prefix['ApiKeyAuth'] = "Bearer"  # pragma: allowlist secret

        self.configuration.debug = self.debug

        return self

    def get_icav2_api_client(self):
        from libica.openapi.v2 import ApiClient
        return ApiClient(
            configuration=self.configuration,
            header_name="Content-Type",
            header_value="application/vnd.illumina.v3+json",
        )


class AppOps:

    def __init__(self, api_client=None):
        if api_client:
            self.api_client = api_client
        else:
            # otherwise, we build api_client with standard lookup from well-known locations
            from libica.openapi.v2 import ApiClient
            self.api_client: ApiClient = AppHelper().build_icav2_configuration().get_icav2_api_client()
