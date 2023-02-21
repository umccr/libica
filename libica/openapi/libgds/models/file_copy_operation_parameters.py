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


class FileCopyOperationParameters(object):
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
        'source_volume_id': 'str',
        'source_file_ids': 'list[str]',
        'target_folder_id': 'str',
        'metadata_to_copy': 'list[str]',
        'duplicate_file_action': 'str'
    }

    attribute_map = {
        'source_volume_id': 'sourceVolumeId',
        'source_file_ids': 'sourceFileIds',
        'target_folder_id': 'targetFolderId',
        'metadata_to_copy': 'metadataToCopy',
        'duplicate_file_action': 'duplicateFileAction'
    }

    def __init__(self, source_volume_id=None, source_file_ids=None, target_folder_id=None, metadata_to_copy=None, duplicate_file_action=None, local_vars_configuration=None):  # noqa: E501
        """FileCopyOperationParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._source_volume_id = None
        self._source_file_ids = None
        self._target_folder_id = None
        self._metadata_to_copy = None
        self._duplicate_file_action = None
        self.discriminator = None

        if source_volume_id is not None:
            self.source_volume_id = source_volume_id
        if source_file_ids is not None:
            self.source_file_ids = source_file_ids
        if target_folder_id is not None:
            self.target_folder_id = target_folder_id
        if metadata_to_copy is not None:
            self.metadata_to_copy = metadata_to_copy
        if duplicate_file_action is not None:
            self.duplicate_file_action = duplicate_file_action

    @property
    def source_volume_id(self):
        """Gets the source_volume_id of this FileCopyOperationParameters.  # noqa: E501


        :return: The source_volume_id of this FileCopyOperationParameters.  # noqa: E501
        :rtype: str
        """
        return self._source_volume_id

    @source_volume_id.setter
    def source_volume_id(self, source_volume_id):
        """Sets the source_volume_id of this FileCopyOperationParameters.


        :param source_volume_id: The source_volume_id of this FileCopyOperationParameters.  # noqa: E501
        :type: str
        """

        self._source_volume_id = source_volume_id

    @property
    def source_file_ids(self):
        """Gets the source_file_ids of this FileCopyOperationParameters.  # noqa: E501

        The file Ids for the copy operation  # noqa: E501

        :return: The source_file_ids of this FileCopyOperationParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_file_ids

    @source_file_ids.setter
    def source_file_ids(self, source_file_ids):
        """Sets the source_file_ids of this FileCopyOperationParameters.

        The file Ids for the copy operation  # noqa: E501

        :param source_file_ids: The source_file_ids of this FileCopyOperationParameters.  # noqa: E501
        :type: list[str]
        """

        self._source_file_ids = source_file_ids

    @property
    def target_folder_id(self):
        """Gets the target_folder_id of this FileCopyOperationParameters.  # noqa: E501


        :return: The target_folder_id of this FileCopyOperationParameters.  # noqa: E501
        :rtype: str
        """
        return self._target_folder_id

    @target_folder_id.setter
    def target_folder_id(self, target_folder_id):
        """Sets the target_folder_id of this FileCopyOperationParameters.


        :param target_folder_id: The target_folder_id of this FileCopyOperationParameters.  # noqa: E501
        :type: str
        """

        self._target_folder_id = target_folder_id

    @property
    def metadata_to_copy(self):
        """Gets the metadata_to_copy of this FileCopyOperationParameters.  # noqa: E501


        :return: The metadata_to_copy of this FileCopyOperationParameters.  # noqa: E501
        :rtype: list[str]
        """
        return self._metadata_to_copy

    @metadata_to_copy.setter
    def metadata_to_copy(self, metadata_to_copy):
        """Sets the metadata_to_copy of this FileCopyOperationParameters.


        :param metadata_to_copy: The metadata_to_copy of this FileCopyOperationParameters.  # noqa: E501
        :type: list[str]
        """

        self._metadata_to_copy = metadata_to_copy

    @property
    def duplicate_file_action(self):
        """Gets the duplicate_file_action of this FileCopyOperationParameters.  # noqa: E501


        :return: The duplicate_file_action of this FileCopyOperationParameters.  # noqa: E501
        :rtype: str
        """
        return self._duplicate_file_action

    @duplicate_file_action.setter
    def duplicate_file_action(self, duplicate_file_action):
        """Sets the duplicate_file_action of this FileCopyOperationParameters.


        :param duplicate_file_action: The duplicate_file_action of this FileCopyOperationParameters.  # noqa: E501
        :type: str
        """

        self._duplicate_file_action = duplicate_file_action

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
        if not isinstance(other, FileCopyOperationParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileCopyOperationParameters):
            return True

        return self.to_dict() != other.to_dict()