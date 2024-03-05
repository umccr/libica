import base64
import logging

import boto3

logger = logging.getLogger(__name__)


def session(**kwargs):
    """
    https://boto3.amazonaws.com/v1/documentation/api/latest/reference/core/session.html

    :param kwargs:
    :return:
    """
    return boto3.session.Session(**kwargs)


def client(service_name, **kwargs):
    return session().client(service_name=service_name, **kwargs)


def sm_client(**kwargs):
    return client('secretsmanager', **kwargs)


def get_secret(secret_name):
    """
    If you are in long-running process and querying rotating value from secret manager such as JWT token, you may
    clear the cache before get secret call. e.g.

        libumccr.aws.libsm.get_secret.cache_clear()

    See https://github.com/umccr/gridss-purple-linx-nf/pull/25/files

    :param secret_name:
    :return:
    """
    resp = sm_client().get_secret_value(
        SecretId=secret_name
    )

    if 'SecretString' in resp:
        return resp['SecretString']
    else:
        return base64.b64decode(resp['SecretBinary'])
