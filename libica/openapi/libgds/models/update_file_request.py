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


class UpdateFileRequest(object):
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
        'type': 'str',
        'format': 'str',
        'format_edam': 'str',
        'life_cycle': 'FileLifeCycleSettings',
        'metadata': 'object',
        'add_metadata': 'object',
        'delete_metadata': 'object'
    }

    attribute_map = {
        'type': 'type',
        'format': 'format',
        'format_edam': 'formatEdam',
        'life_cycle': 'lifeCycle',
        'metadata': 'metadata',
        'add_metadata': 'addMetadata',
        'delete_metadata': 'deleteMetadata'
    }

    def __init__(self, type=None, format=None, format_edam=None, life_cycle=None, metadata=None, add_metadata=None, delete_metadata=None, local_vars_configuration=None):  # noqa: E501
        """UpdateFileRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._format = None
        self._format_edam = None
        self._life_cycle = None
        self._metadata = None
        self._add_metadata = None
        self._delete_metadata = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if format is not None:
            self.format = format
        if format_edam is not None:
            self.format_edam = format_edam
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if metadata is not None:
            self.metadata = metadata
        if add_metadata is not None:
            self.add_metadata = add_metadata
        if delete_metadata is not None:
            self.delete_metadata = delete_metadata

    @property
    def type(self):
        """Gets the type of this UpdateFileRequest.  # noqa: E501

        The new file type (e.g. \"text/plain\").  # noqa: E501

        :return: The type of this UpdateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateFileRequest.

        The new file type (e.g. \"text/plain\").  # noqa: E501

        :param type: The type of this UpdateFileRequest.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def format(self):
        """Gets the format of this UpdateFileRequest.  # noqa: E501

        The File's Format  # noqa: E501

        :return: The format of this UpdateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this UpdateFileRequest.

        The File's Format  # noqa: E501

        :param format: The format of this UpdateFileRequest.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def format_edam(self):
        """Gets the format_edam of this UpdateFileRequest.  # noqa: E501

        The File's Edam Format  # noqa: E501

        :return: The format_edam of this UpdateFileRequest.  # noqa: E501
        :rtype: str
        """
        return self._format_edam

    @format_edam.setter
    def format_edam(self, format_edam):
        """Sets the format_edam of this UpdateFileRequest.

        The File's Edam Format  # noqa: E501

        :param format_edam: The format_edam of this UpdateFileRequest.  # noqa: E501
        :type: str
        """

        self._format_edam = format_edam

    @property
    def life_cycle(self):
        """Gets the life_cycle of this UpdateFileRequest.  # noqa: E501


        :return: The life_cycle of this UpdateFileRequest.  # noqa: E501
        :rtype: FileLifeCycleSettings
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        """Sets the life_cycle of this UpdateFileRequest.


        :param life_cycle: The life_cycle of this UpdateFileRequest.  # noqa: E501
        :type: FileLifeCycleSettings
        """

        self._life_cycle = life_cycle

    @property
    def metadata(self):
        """Gets the metadata of this UpdateFileRequest.  # noqa: E501

        Metadata about this file and its contents  # noqa: E501

        :return: The metadata of this UpdateFileRequest.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this UpdateFileRequest.

        Metadata about this file and its contents  # noqa: E501

        :param metadata: The metadata of this UpdateFileRequest.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def add_metadata(self):
        """Gets the add_metadata of this UpdateFileRequest.  # noqa: E501

        Add an item to a metadata with array type  # noqa: E501

        :return: The add_metadata of this UpdateFileRequest.  # noqa: E501
        :rtype: object
        """
        return self._add_metadata

    @add_metadata.setter
    def add_metadata(self, add_metadata):
        """Sets the add_metadata of this UpdateFileRequest.

        Add an item to a metadata with array type  # noqa: E501

        :param add_metadata: The add_metadata of this UpdateFileRequest.  # noqa: E501
        :type: object
        """

        self._add_metadata = add_metadata

    @property
    def delete_metadata(self):
        """Gets the delete_metadata of this UpdateFileRequest.  # noqa: E501

        Delete an item from a metadata with array type  # noqa: E501

        :return: The delete_metadata of this UpdateFileRequest.  # noqa: E501
        :rtype: object
        """
        return self._delete_metadata

    @delete_metadata.setter
    def delete_metadata(self, delete_metadata):
        """Sets the delete_metadata of this UpdateFileRequest.

        Delete an item from a metadata with array type  # noqa: E501

        :param delete_metadata: The delete_metadata of this UpdateFileRequest.  # noqa: E501
        :type: object
        """

        self._delete_metadata = delete_metadata

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
        if not isinstance(other, UpdateFileRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateFileRequest):
            return True

        return self.to_dict() != other.to_dict()
