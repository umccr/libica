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


class AwsS3PresignedUrlForUpload(object):
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
        'single_part_url': 'str',
        'multipart_template': 'str',
        'multipart_signatures': 'list[PartInfo]',
        'multipart_upload_id': 'str',
        'server_side_encryption_algorithm': 'str',
        'server_side_encryption_key': 'str'
    }

    attribute_map = {
        'single_part_url': 'singlePartUrl',
        'multipart_template': 'multipartTemplate',
        'multipart_signatures': 'multipartSignatures',
        'multipart_upload_id': 'multipartUploadId',
        'server_side_encryption_algorithm': 'serverSideEncryptionAlgorithm',
        'server_side_encryption_key': 'serverSideEncryptionKey'
    }

    def __init__(self, single_part_url=None, multipart_template=None, multipart_signatures=None, multipart_upload_id=None, server_side_encryption_algorithm=None, server_side_encryption_key=None, local_vars_configuration=None):  # noqa: E501
        """AwsS3PresignedUrlForUpload - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._single_part_url = None
        self._multipart_template = None
        self._multipart_signatures = None
        self._multipart_upload_id = None
        self._server_side_encryption_algorithm = None
        self._server_side_encryption_key = None
        self.discriminator = None

        if single_part_url is not None:
            self.single_part_url = single_part_url
        if multipart_template is not None:
            self.multipart_template = multipart_template
        if multipart_signatures is not None:
            self.multipart_signatures = multipart_signatures
        if multipart_upload_id is not None:
            self.multipart_upload_id = multipart_upload_id
        if server_side_encryption_algorithm is not None:
            self.server_side_encryption_algorithm = server_side_encryption_algorithm
        if server_side_encryption_key is not None:
            self.server_side_encryption_key = server_side_encryption_key

    @property
    def single_part_url(self):
        """Gets the single_part_url of this AwsS3PresignedUrlForUpload.  # noqa: E501

        A single part presigned url for upload  # noqa: E501

        :return: The single_part_url of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :rtype: str
        """
        return self._single_part_url

    @single_part_url.setter
    def single_part_url(self, single_part_url):
        """Sets the single_part_url of this AwsS3PresignedUrlForUpload.

        A single part presigned url for upload  # noqa: E501

        :param single_part_url: The single_part_url of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :type: str
        """

        self._single_part_url = single_part_url

    @property
    def multipart_template(self):
        """Gets the multipart_template of this AwsS3PresignedUrlForUpload.  # noqa: E501

        A url template for multi parts presigned url for upload  # noqa: E501

        :return: The multipart_template of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :rtype: str
        """
        return self._multipart_template

    @multipart_template.setter
    def multipart_template(self, multipart_template):
        """Sets the multipart_template of this AwsS3PresignedUrlForUpload.

        A url template for multi parts presigned url for upload  # noqa: E501

        :param multipart_template: The multipart_template of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :type: str
        """

        self._multipart_template = multipart_template

    @property
    def multipart_signatures(self):
        """Gets the multipart_signatures of this AwsS3PresignedUrlForUpload.  # noqa: E501

        Multi parts info that needs to be applied to the MultipartTemplate  # noqa: E501

        :return: The multipart_signatures of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :rtype: list[PartInfo]
        """
        return self._multipart_signatures

    @multipart_signatures.setter
    def multipart_signatures(self, multipart_signatures):
        """Sets the multipart_signatures of this AwsS3PresignedUrlForUpload.

        Multi parts info that needs to be applied to the MultipartTemplate  # noqa: E501

        :param multipart_signatures: The multipart_signatures of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :type: list[PartInfo]
        """

        self._multipart_signatures = multipart_signatures

    @property
    def multipart_upload_id(self):
        """Gets the multipart_upload_id of this AwsS3PresignedUrlForUpload.  # noqa: E501

        Multi part upload id  # noqa: E501

        :return: The multipart_upload_id of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :rtype: str
        """
        return self._multipart_upload_id

    @multipart_upload_id.setter
    def multipart_upload_id(self, multipart_upload_id):
        """Sets the multipart_upload_id of this AwsS3PresignedUrlForUpload.

        Multi part upload id  # noqa: E501

        :param multipart_upload_id: The multipart_upload_id of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :type: str
        """

        self._multipart_upload_id = multipart_upload_id

    @property
    def server_side_encryption_algorithm(self):
        """Gets the server_side_encryption_algorithm of this AwsS3PresignedUrlForUpload.  # noqa: E501

        The server side encryption method used by S3.  This value is used to determine the Amazon S3 header \"x-amz-server-side-encryption\" value.  Possible values: 'AES256' and 'aws:kms'.  # noqa: E501

        :return: The server_side_encryption_algorithm of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :rtype: str
        """
        return self._server_side_encryption_algorithm

    @server_side_encryption_algorithm.setter
    def server_side_encryption_algorithm(self, server_side_encryption_algorithm):
        """Sets the server_side_encryption_algorithm of this AwsS3PresignedUrlForUpload.

        The server side encryption method used by S3.  This value is used to determine the Amazon S3 header \"x-amz-server-side-encryption\" value.  Possible values: 'AES256' and 'aws:kms'.  # noqa: E501

        :param server_side_encryption_algorithm: The server_side_encryption_algorithm of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :type: str
        """

        self._server_side_encryption_algorithm = server_side_encryption_algorithm

    @property
    def server_side_encryption_key(self):
        """Gets the server_side_encryption_key of this AwsS3PresignedUrlForUpload.  # noqa: E501

        Server-side encryption key that might be associated with the specified server-side encryption algorithm  This value can be the AWS KMS arn key, to be used for the Amazon S3 header \"x-amz-server-side-encryption-aws-kms-key-id\" value  This is only used when ServerSideEncryptionAlgorithm is 'aws:kms'  # noqa: E501

        :return: The server_side_encryption_key of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :rtype: str
        """
        return self._server_side_encryption_key

    @server_side_encryption_key.setter
    def server_side_encryption_key(self, server_side_encryption_key):
        """Sets the server_side_encryption_key of this AwsS3PresignedUrlForUpload.

        Server-side encryption key that might be associated with the specified server-side encryption algorithm  This value can be the AWS KMS arn key, to be used for the Amazon S3 header \"x-amz-server-side-encryption-aws-kms-key-id\" value  This is only used when ServerSideEncryptionAlgorithm is 'aws:kms'  # noqa: E501

        :param server_side_encryption_key: The server_side_encryption_key of this AwsS3PresignedUrlForUpload.  # noqa: E501
        :type: str
        """

        self._server_side_encryption_key = server_side_encryption_key

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
        if not isinstance(other, AwsS3PresignedUrlForUpload):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwsS3PresignedUrlForUpload):
            return True

        return self.to_dict() != other.to_dict()