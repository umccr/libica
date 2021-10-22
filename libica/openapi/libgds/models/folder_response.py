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


class FolderResponse(object):
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
        'id': 'str',
        'name': 'str',
        'volume_id': 'str',
        'parent_folder_id': 'str',
        'volume_name': 'str',
        'tenant_id': 'str',
        'sub_tenant_id': 'str',
        'urn': 'str',
        'path': 'str',
        'acl': 'list[str]',
        'inherited_acl': 'list[str]',
        'time_created': 'datetime',
        'created_by': 'str',
        'time_modified': 'datetime',
        'modified_by': 'str',
        'metadata': 'object',
        'volume_metadata': 'object',
        'job_status': 'JobStatus',
        'job_id': 'str',
        'archive_job_storage_tier': 'StorageTier'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'volume_id': 'volumeId',
        'parent_folder_id': 'parentFolderId',
        'volume_name': 'volumeName',
        'tenant_id': 'tenantId',
        'sub_tenant_id': 'subTenantId',
        'urn': 'urn',
        'path': 'path',
        'acl': 'acl',
        'inherited_acl': 'inheritedAcl',
        'time_created': 'timeCreated',
        'created_by': 'createdBy',
        'time_modified': 'timeModified',
        'modified_by': 'modifiedBy',
        'metadata': 'metadata',
        'volume_metadata': 'volumeMetadata',
        'job_status': 'jobStatus',
        'job_id': 'jobId',
        'archive_job_storage_tier': 'archiveJobStorageTier'
    }

    def __init__(self, id=None, name=None, volume_id=None, parent_folder_id=None, volume_name=None, tenant_id=None, sub_tenant_id=None, urn=None, path=None, acl=None, inherited_acl=None, time_created=None, created_by=None, time_modified=None, modified_by=None, metadata=None, volume_metadata=None, job_status=None, job_id=None, archive_job_storage_tier=None, local_vars_configuration=None):  # noqa: E501
        """FolderResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._volume_id = None
        self._parent_folder_id = None
        self._volume_name = None
        self._tenant_id = None
        self._sub_tenant_id = None
        self._urn = None
        self._path = None
        self._acl = None
        self._inherited_acl = None
        self._time_created = None
        self._created_by = None
        self._time_modified = None
        self._modified_by = None
        self._metadata = None
        self._volume_metadata = None
        self._job_status = None
        self._job_id = None
        self._archive_job_storage_tier = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if volume_id is not None:
            self.volume_id = volume_id
        if parent_folder_id is not None:
            self.parent_folder_id = parent_folder_id
        if volume_name is not None:
            self.volume_name = volume_name
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if sub_tenant_id is not None:
            self.sub_tenant_id = sub_tenant_id
        if urn is not None:
            self.urn = urn
        if path is not None:
            self.path = path
        if acl is not None:
            self.acl = acl
        if inherited_acl is not None:
            self.inherited_acl = inherited_acl
        if time_created is not None:
            self.time_created = time_created
        if created_by is not None:
            self.created_by = created_by
        if time_modified is not None:
            self.time_modified = time_modified
        if modified_by is not None:
            self.modified_by = modified_by
        if metadata is not None:
            self.metadata = metadata
        if volume_metadata is not None:
            self.volume_metadata = volume_metadata
        if job_status is not None:
            self.job_status = job_status
        if job_id is not None:
            self.job_id = job_id
        if archive_job_storage_tier is not None:
            self.archive_job_storage_tier = archive_job_storage_tier

    @property
    def id(self):
        """Gets the id of this FolderResponse.  # noqa: E501

        A unique identifier for this Folder  # noqa: E501

        :return: The id of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FolderResponse.

        A unique identifier for this Folder  # noqa: E501

        :param id: The id of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FolderResponse.  # noqa: E501

        The name of this Folder  # noqa: E501

        :return: The name of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FolderResponse.

        The name of this Folder  # noqa: E501

        :param name: The name of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def volume_id(self):
        """Gets the volume_id of this FolderResponse.  # noqa: E501

        The unique identifier for this Folder's Volume  # noqa: E501

        :return: The volume_id of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this FolderResponse.

        The unique identifier for this Folder's Volume  # noqa: E501

        :param volume_id: The volume_id of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._volume_id = volume_id

    @property
    def parent_folder_id(self):
        """Gets the parent_folder_id of this FolderResponse.  # noqa: E501

        The unique identifier for this folder's parent folder  # noqa: E501

        :return: The parent_folder_id of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._parent_folder_id

    @parent_folder_id.setter
    def parent_folder_id(self, parent_folder_id):
        """Sets the parent_folder_id of this FolderResponse.

        The unique identifier for this folder's parent folder  # noqa: E501

        :param parent_folder_id: The parent_folder_id of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._parent_folder_id = parent_folder_id

    @property
    def volume_name(self):
        """Gets the volume_name of this FolderResponse.  # noqa: E501

        The name of this Folder's Volume  # noqa: E501

        :return: The volume_name of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """Sets the volume_name of this FolderResponse.

        The name of this Folder's Volume  # noqa: E501

        :param volume_name: The volume_name of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._volume_name = volume_name

    @property
    def tenant_id(self):
        """Gets the tenant_id of this FolderResponse.  # noqa: E501

        The unique identifier for this Folders's Tenant  # noqa: E501

        :return: The tenant_id of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this FolderResponse.

        The unique identifier for this Folders's Tenant  # noqa: E501

        :param tenant_id: The tenant_id of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def sub_tenant_id(self):
        """Gets the sub_tenant_id of this FolderResponse.  # noqa: E501

        The unique identifier for this Folder's Sub Tenant  # noqa: E501

        :return: The sub_tenant_id of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._sub_tenant_id

    @sub_tenant_id.setter
    def sub_tenant_id(self, sub_tenant_id):
        """Sets the sub_tenant_id of this FolderResponse.

        The unique identifier for this Folder's Sub Tenant  # noqa: E501

        :param sub_tenant_id: The sub_tenant_id of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._sub_tenant_id = sub_tenant_id

    @property
    def urn(self):
        """Gets the urn of this FolderResponse.  # noqa: E501

        The Universal Resource Name, unique to this Folder  # noqa: E501

        :return: The urn of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this FolderResponse.

        The Universal Resource Name, unique to this Folder  # noqa: E501

        :param urn: The urn of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._urn = urn

    @property
    def path(self):
        """Gets the path of this FolderResponse.  # noqa: E501

        The (GDS) folder path to this Folder  # noqa: E501

        :return: The path of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FolderResponse.

        The (GDS) folder path to this Folder  # noqa: E501

        :param path: The path of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def acl(self):
        """Gets the acl of this FolderResponse.  # noqa: E501

        The list of directly specified Id(s) that have access to this Folder  # noqa: E501

        :return: The acl of this FolderResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this FolderResponse.

        The list of directly specified Id(s) that have access to this Folder  # noqa: E501

        :param acl: The acl of this FolderResponse.  # noqa: E501
        :type: list[str]
        """

        self._acl = acl

    @property
    def inherited_acl(self):
        """Gets the inherited_acl of this FolderResponse.  # noqa: E501

        The inherited list of Id(s) that have access to this Folder  # noqa: E501

        :return: The inherited_acl of this FolderResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._inherited_acl

    @inherited_acl.setter
    def inherited_acl(self, inherited_acl):
        """Sets the inherited_acl of this FolderResponse.

        The inherited list of Id(s) that have access to this Folder  # noqa: E501

        :param inherited_acl: The inherited_acl of this FolderResponse.  # noqa: E501
        :type: list[str]
        """

        self._inherited_acl = inherited_acl

    @property
    def time_created(self):
        """Gets the time_created of this FolderResponse.  # noqa: E501

        The date & time this Folder was created, in GDS  # noqa: E501

        :return: The time_created of this FolderResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """Sets the time_created of this FolderResponse.

        The date & time this Folder was created, in GDS  # noqa: E501

        :param time_created: The time_created of this FolderResponse.  # noqa: E501
        :type: datetime
        """

        self._time_created = time_created

    @property
    def created_by(self):
        """Gets the created_by of this FolderResponse.  # noqa: E501

        The creator of this Folder  # noqa: E501

        :return: The created_by of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this FolderResponse.

        The creator of this Folder  # noqa: E501

        :param created_by: The created_by of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def time_modified(self):
        """Gets the time_modified of this FolderResponse.  # noqa: E501

        The date & time this Folder was updated, in GDS  # noqa: E501

        :return: The time_modified of this FolderResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._time_modified

    @time_modified.setter
    def time_modified(self, time_modified):
        """Sets the time_modified of this FolderResponse.

        The date & time this Folder was updated, in GDS  # noqa: E501

        :param time_modified: The time_modified of this FolderResponse.  # noqa: E501
        :type: datetime
        """

        self._time_modified = time_modified

    @property
    def modified_by(self):
        """Gets the modified_by of this FolderResponse.  # noqa: E501

        The updator of this Folder  # noqa: E501

        :return: The modified_by of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this FolderResponse.

        The updator of this Folder  # noqa: E501

        :param modified_by: The modified_by of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def metadata(self):
        """Gets the metadata of this FolderResponse.  # noqa: E501

        Metadata about this folder  # noqa: E501

        :return: The metadata of this FolderResponse.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FolderResponse.

        Metadata about this folder  # noqa: E501

        :param metadata: The metadata of this FolderResponse.  # noqa: E501
        :type: object
        """

        self._metadata = metadata

    @property
    def volume_metadata(self):
        """Gets the volume_metadata of this FolderResponse.  # noqa: E501

        Metadata about this folder's volume  # noqa: E501

        :return: The volume_metadata of this FolderResponse.  # noqa: E501
        :rtype: object
        """
        return self._volume_metadata

    @volume_metadata.setter
    def volume_metadata(self, volume_metadata):
        """Sets the volume_metadata of this FolderResponse.

        Metadata about this folder's volume  # noqa: E501

        :param volume_metadata: The volume_metadata of this FolderResponse.  # noqa: E501
        :type: object
        """

        self._volume_metadata = volume_metadata

    @property
    def job_status(self):
        """Gets the job_status of this FolderResponse.  # noqa: E501


        :return: The job_status of this FolderResponse.  # noqa: E501
        :rtype: JobStatus
        """
        return self._job_status

    @job_status.setter
    def job_status(self, job_status):
        """Sets the job_status of this FolderResponse.


        :param job_status: The job_status of this FolderResponse.  # noqa: E501
        :type: JobStatus
        """

        self._job_status = job_status

    @property
    def job_id(self):
        """Gets the job_id of this FolderResponse.  # noqa: E501

        The job identifier for the current folder operation. Currently only being used for the delete folder operation.  # noqa: E501

        :return: The job_id of this FolderResponse.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this FolderResponse.

        The job identifier for the current folder operation. Currently only being used for the delete folder operation.  # noqa: E501

        :param job_id: The job_id of this FolderResponse.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def archive_job_storage_tier(self):
        """Gets the archive_job_storage_tier of this FolderResponse.  # noqa: E501


        :return: The archive_job_storage_tier of this FolderResponse.  # noqa: E501
        :rtype: StorageTier
        """
        return self._archive_job_storage_tier

    @archive_job_storage_tier.setter
    def archive_job_storage_tier(self, archive_job_storage_tier):
        """Sets the archive_job_storage_tier of this FolderResponse.


        :param archive_job_storage_tier: The archive_job_storage_tier of this FolderResponse.  # noqa: E501
        :type: StorageTier
        """

        self._archive_job_storage_tier = archive_job_storage_tier

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
        if not isinstance(other, FolderResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FolderResponse):
            return True

        return self.to_dict() != other.to_dict()
