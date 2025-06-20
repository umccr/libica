# coding: utf-8

"""
    ICA Rest API

    This API can be used to interact with Illumina Connected Analytics.<br> <h2>Authentication</h2> <p> Authentication to the  API can be done in multiple ways:<br> <ul><li>For the entire API, except for the POST /tokens endpoint: API-key + JWT</li> <li>Only for the POST /tokens endpoint: API-key + Basic Authentication</li></ul> </p> <p> <h4>API-key</h4> API keys are managed within the Illumina portal where you can manage your profile after you have logged on. The API-key has to be provided in the X-API-Key header parameter when executing API calls to ICA. In the background, a JWT will be requested at the IDP of Illumina to create a session. A good practice is to not use the API-key for every API call, but to first generate a JWT and to use that for authentication in subsequent calls.<br> </p> <p> <h4>JWT</h4> To avoid using an API-key for each call, we recommend to request a JWT via the POST /tokens endpoint  using this API-key. The JWT will expire after a pre-configured period specified by a tenant administrator through the IAM console in the Illumina portal. The JWT is the preferred way for authentication.<br>A not yet expired, still valid JWT could be refreshed using the POST /tokens:refresh endpoint.<br>Refreshing the JWT is not possible if the JWT was generated by using an API-key.<br> </p> <p> <h4>Basic Authentication</h4> Basic authentication is only supported by the POST /tokens endpoint for generating a JWT. Use \"Basic base64encoded(emailaddress:password)\" in the \"Authorization\" header parameter for this authentication method. In case having access to multiple tenants using the same email-address, also provide the \"tenant\" request parameter to indicate what tenant you would like to request a JWT for. </p> <p> <h2>Compression</h2> If the API client provides request header 'Accept-Encoding' with value 'gzip', then the API applies GZIP compression on the JSON response. This significantly reduces the size and thus the download time of the response, which results in faster end-to-end API calls. In case of compression, the API also provides response header 'Content-Encoding' with value 'gzip', as indication for the client that decompression is required. </p> 

    The version of the OpenAPI document: 3
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from libica.openapi.v3.models.application import Application
from libica.openapi.v3.models.metadata_model import MetadataModel
from libica.openapi.v3.models.project_tag import ProjectTag
from libica.openapi.v3.models.region import Region
from libica.openapi.v3.models.storage_bundle import StorageBundle
from libica.openapi.v3.models.storage_configuration import StorageConfiguration
from typing import Optional, Set
from typing_extensions import Self

class Project(BaseModel):
    """
    Project
    """ # noqa: E501
    id: StrictStr
    time_created: datetime = Field(alias="timeCreated")
    time_modified: datetime = Field(alias="timeModified")
    owner_id: StrictStr = Field(alias="ownerId")
    tenant_id: StrictStr = Field(alias="tenantId")
    tenant_name: Optional[StrictStr] = Field(default=None, alias="tenantName")
    urn: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=2000)]] = Field(default=None, description="The URN of the project. The format is urn:ilmn:ica:\\<type of the object\\>:\\<ID of the object\\>#\\<optional human readable hint representing the object\\>. The hint can be omitted, in that case the hashtag (#) must also be omitted.")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    active: StrictBool = Field(description="Indicates whether the project is active or hidden.")
    base_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the project is base enabled.", alias="baseEnabled")
    short_description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=4000)]] = Field(default=None, alias="shortDescription")
    information: Optional[StrictStr] = Field(default=None, description="Information about the project. Note that the value of this field can be arbitrary large.")
    region: Region
    billing_mode: StrictStr = Field(description="The billing mode of the project. It determines who pays for the costs linked to the project.", alias="billingMode")
    data_sharing_enabled: Optional[StrictBool] = Field(default=None, description="Indicates whether the Data and Samples created in this Project can be linked to other Projects.", alias="dataSharingEnabled")
    tags: ProjectTag
    storage_bundle: Optional[StorageBundle] = Field(default=None, alias="storageBundle")
    self_managed_storage_configuration: Optional[StorageConfiguration] = Field(default=None, alias="selfManagedStorageConfiguration")
    analysis_priority: Optional[StrictStr] = Field(default=None, description="Indicates the priority given to a project and its analyses within a single tenant. Note that for a PUT call, when not providing a value for this attribute (null value or absent attribute), the persisted value will not change.", alias="analysisPriority")
    metadata_model: Optional[MetadataModel] = Field(default=None, alias="metadataModel")
    application: Optional[Application] = None
    project_owner: Optional[StrictStr] = Field(default=None, description="projectOwner is the current project owner, ownerId is the original project creator. These can be different because you can transfer ownership of a project.", alias="projectOwner")
    __properties: ClassVar[List[str]] = ["id", "timeCreated", "timeModified", "ownerId", "tenantId", "tenantName", "urn", "name", "active", "baseEnabled", "shortDescription", "information", "region", "billingMode", "dataSharingEnabled", "tags", "storageBundle", "selfManagedStorageConfiguration", "analysisPriority", "metadataModel", "application", "projectOwner"]

    @field_validator('billing_mode')
    def billing_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PROJECT', 'TENANT']):
            raise ValueError("must be one of enum values ('PROJECT', 'TENANT')")
        return value

    @field_validator('analysis_priority')
    def analysis_priority_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LOW', 'MEDIUM', 'HIGH']):
            raise ValueError("must be one of enum values ('LOW', 'MEDIUM', 'HIGH')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Project from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of region
        if self.region:
            _dict['region'] = self.region.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # override the default output from pydantic by calling `to_dict()` of storage_bundle
        if self.storage_bundle:
            _dict['storageBundle'] = self.storage_bundle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of self_managed_storage_configuration
        if self.self_managed_storage_configuration:
            _dict['selfManagedStorageConfiguration'] = self.self_managed_storage_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of metadata_model
        if self.metadata_model:
            _dict['metadataModel'] = self.metadata_model.to_dict()
        # override the default output from pydantic by calling `to_dict()` of application
        if self.application:
            _dict['application'] = self.application.to_dict()
        # set to None if tenant_name (nullable) is None
        # and model_fields_set contains the field
        if self.tenant_name is None and "tenant_name" in self.model_fields_set:
            _dict['tenantName'] = None

        # set to None if urn (nullable) is None
        # and model_fields_set contains the field
        if self.urn is None and "urn" in self.model_fields_set:
            _dict['urn'] = None

        # set to None if base_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.base_enabled is None and "base_enabled" in self.model_fields_set:
            _dict['baseEnabled'] = None

        # set to None if short_description (nullable) is None
        # and model_fields_set contains the field
        if self.short_description is None and "short_description" in self.model_fields_set:
            _dict['shortDescription'] = None

        # set to None if information (nullable) is None
        # and model_fields_set contains the field
        if self.information is None and "information" in self.model_fields_set:
            _dict['information'] = None

        # set to None if data_sharing_enabled (nullable) is None
        # and model_fields_set contains the field
        if self.data_sharing_enabled is None and "data_sharing_enabled" in self.model_fields_set:
            _dict['dataSharingEnabled'] = None

        # set to None if analysis_priority (nullable) is None
        # and model_fields_set contains the field
        if self.analysis_priority is None and "analysis_priority" in self.model_fields_set:
            _dict['analysisPriority'] = None

        # set to None if metadata_model (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_model is None and "metadata_model" in self.model_fields_set:
            _dict['metadataModel'] = None

        # set to None if application (nullable) is None
        # and model_fields_set contains the field
        if self.application is None and "application" in self.model_fields_set:
            _dict['application'] = None

        # set to None if project_owner (nullable) is None
        # and model_fields_set contains the field
        if self.project_owner is None and "project_owner" in self.model_fields_set:
            _dict['projectOwner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "timeCreated": obj.get("timeCreated"),
            "timeModified": obj.get("timeModified"),
            "ownerId": obj.get("ownerId"),
            "tenantId": obj.get("tenantId"),
            "tenantName": obj.get("tenantName"),
            "urn": obj.get("urn"),
            "name": obj.get("name"),
            "active": obj.get("active"),
            "baseEnabled": obj.get("baseEnabled"),
            "shortDescription": obj.get("shortDescription"),
            "information": obj.get("information"),
            "region": Region.from_dict(obj["region"]) if obj.get("region") is not None else None,
            "billingMode": obj.get("billingMode"),
            "dataSharingEnabled": obj.get("dataSharingEnabled"),
            "tags": ProjectTag.from_dict(obj["tags"]) if obj.get("tags") is not None else None,
            "storageBundle": StorageBundle.from_dict(obj["storageBundle"]) if obj.get("storageBundle") is not None else None,
            "selfManagedStorageConfiguration": StorageConfiguration.from_dict(obj["selfManagedStorageConfiguration"]) if obj.get("selfManagedStorageConfiguration") is not None else None,
            "analysisPriority": obj.get("analysisPriority"),
            "metadataModel": MetadataModel.from_dict(obj["metadataModel"]) if obj.get("metadataModel") is not None else None,
            "application": Application.from_dict(obj["application"]) if obj.get("application") is not None else None,
            "projectOwner": obj.get("projectOwner")
        })
        return _obj


