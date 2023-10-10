# coding: utf-8

"""
    Genomic Data Store Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from libica.openapi.libgds.configuration import Configuration


class ObjectStoreAccess(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'session_id': 'str',
        'aws_s3_temporary_upload_credentials': 'AwsS3TemporaryUploadCredentials',
        'aws_s3_presigned_url_for_upload': 'AwsS3PresignedUrlForUpload',
        'azure_temporary_upload_credentials': 'AzureTemporaryUploadCredentials',
        'aws_s3_temporary_read_only_credentials': 'AwsS3TemporaryReadOnlyCredentials',
        'azure_temporary_read_only_credentials': 'AzureTemporaryReadOnlyCredentials'
    }

    attribute_map = {
        'session_id': 'sessionId',
        'aws_s3_temporary_upload_credentials': 'awsS3TemporaryUploadCredentials',
        'aws_s3_presigned_url_for_upload': 'awsS3PresignedUrlForUpload',
        'azure_temporary_upload_credentials': 'azureTemporaryUploadCredentials',
        'aws_s3_temporary_read_only_credentials': 'awsS3TemporaryReadOnlyCredentials',
        'azure_temporary_read_only_credentials': 'azureTemporaryReadOnlyCredentials'
    }

    def __init__(self, session_id=None, aws_s3_temporary_upload_credentials=None, aws_s3_presigned_url_for_upload=None, azure_temporary_upload_credentials=None, aws_s3_temporary_read_only_credentials=None, azure_temporary_read_only_credentials=None, local_vars_configuration=None):  # noqa: E501
        """ObjectStoreAccess - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._session_id = None
        self._aws_s3_temporary_upload_credentials = None
        self._aws_s3_presigned_url_for_upload = None
        self._azure_temporary_upload_credentials = None
        self._aws_s3_temporary_read_only_credentials = None
        self._azure_temporary_read_only_credentials = None
        self.discriminator = None

        if session_id is not None:
            self.session_id = session_id
        if aws_s3_temporary_upload_credentials is not None:
            self.aws_s3_temporary_upload_credentials = aws_s3_temporary_upload_credentials
        if aws_s3_presigned_url_for_upload is not None:
            self.aws_s3_presigned_url_for_upload = aws_s3_presigned_url_for_upload
        if azure_temporary_upload_credentials is not None:
            self.azure_temporary_upload_credentials = azure_temporary_upload_credentials
        if aws_s3_temporary_read_only_credentials is not None:
            self.aws_s3_temporary_read_only_credentials = aws_s3_temporary_read_only_credentials
        if azure_temporary_read_only_credentials is not None:
            self.azure_temporary_read_only_credentials = azure_temporary_read_only_credentials

    @property
    def session_id(self):
        """Gets the session_id of this ObjectStoreAccess.  # noqa: E501


        :return: The session_id of this ObjectStoreAccess.  # noqa: E501
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ObjectStoreAccess.


        :param session_id: The session_id of this ObjectStoreAccess.  # noqa: E501
        :type: str
        """

        self._session_id = session_id

    @property
    def aws_s3_temporary_upload_credentials(self):
        """Gets the aws_s3_temporary_upload_credentials of this ObjectStoreAccess.  # noqa: E501


        :return: The aws_s3_temporary_upload_credentials of this ObjectStoreAccess.  # noqa: E501
        :rtype: AwsS3TemporaryUploadCredentials
        """
        return self._aws_s3_temporary_upload_credentials

    @aws_s3_temporary_upload_credentials.setter
    def aws_s3_temporary_upload_credentials(self, aws_s3_temporary_upload_credentials):
        """Sets the aws_s3_temporary_upload_credentials of this ObjectStoreAccess.


        :param aws_s3_temporary_upload_credentials: The aws_s3_temporary_upload_credentials of this ObjectStoreAccess.  # noqa: E501
        :type: AwsS3TemporaryUploadCredentials
        """

        self._aws_s3_temporary_upload_credentials = aws_s3_temporary_upload_credentials

    @property
    def aws_s3_presigned_url_for_upload(self):
        """Gets the aws_s3_presigned_url_for_upload of this ObjectStoreAccess.  # noqa: E501


        :return: The aws_s3_presigned_url_for_upload of this ObjectStoreAccess.  # noqa: E501
        :rtype: AwsS3PresignedUrlForUpload
        """
        return self._aws_s3_presigned_url_for_upload

    @aws_s3_presigned_url_for_upload.setter
    def aws_s3_presigned_url_for_upload(self, aws_s3_presigned_url_for_upload):
        """Sets the aws_s3_presigned_url_for_upload of this ObjectStoreAccess.


        :param aws_s3_presigned_url_for_upload: The aws_s3_presigned_url_for_upload of this ObjectStoreAccess.  # noqa: E501
        :type: AwsS3PresignedUrlForUpload
        """

        self._aws_s3_presigned_url_for_upload = aws_s3_presigned_url_for_upload

    @property
    def azure_temporary_upload_credentials(self):
        """Gets the azure_temporary_upload_credentials of this ObjectStoreAccess.  # noqa: E501


        :return: The azure_temporary_upload_credentials of this ObjectStoreAccess.  # noqa: E501
        :rtype: AzureTemporaryUploadCredentials
        """
        return self._azure_temporary_upload_credentials

    @azure_temporary_upload_credentials.setter
    def azure_temporary_upload_credentials(self, azure_temporary_upload_credentials):
        """Sets the azure_temporary_upload_credentials of this ObjectStoreAccess.


        :param azure_temporary_upload_credentials: The azure_temporary_upload_credentials of this ObjectStoreAccess.  # noqa: E501
        :type: AzureTemporaryUploadCredentials
        """

        self._azure_temporary_upload_credentials = azure_temporary_upload_credentials

    @property
    def aws_s3_temporary_read_only_credentials(self):
        """Gets the aws_s3_temporary_read_only_credentials of this ObjectStoreAccess.  # noqa: E501


        :return: The aws_s3_temporary_read_only_credentials of this ObjectStoreAccess.  # noqa: E501
        :rtype: AwsS3TemporaryReadOnlyCredentials
        """
        return self._aws_s3_temporary_read_only_credentials

    @aws_s3_temporary_read_only_credentials.setter
    def aws_s3_temporary_read_only_credentials(self, aws_s3_temporary_read_only_credentials):
        """Sets the aws_s3_temporary_read_only_credentials of this ObjectStoreAccess.


        :param aws_s3_temporary_read_only_credentials: The aws_s3_temporary_read_only_credentials of this ObjectStoreAccess.  # noqa: E501
        :type: AwsS3TemporaryReadOnlyCredentials
        """

        self._aws_s3_temporary_read_only_credentials = aws_s3_temporary_read_only_credentials

    @property
    def azure_temporary_read_only_credentials(self):
        """Gets the azure_temporary_read_only_credentials of this ObjectStoreAccess.  # noqa: E501


        :return: The azure_temporary_read_only_credentials of this ObjectStoreAccess.  # noqa: E501
        :rtype: AzureTemporaryReadOnlyCredentials
        """
        return self._azure_temporary_read_only_credentials

    @azure_temporary_read_only_credentials.setter
    def azure_temporary_read_only_credentials(self, azure_temporary_read_only_credentials):
        """Sets the azure_temporary_read_only_credentials of this ObjectStoreAccess.


        :param azure_temporary_read_only_credentials: The azure_temporary_read_only_credentials of this ObjectStoreAccess.  # noqa: E501
        :type: AzureTemporaryReadOnlyCredentials
        """

        self._azure_temporary_read_only_credentials = azure_temporary_read_only_credentials

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ObjectStoreAccess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ObjectStoreAccess):
            return True

        return self.to_dict() != other.to_dict()
