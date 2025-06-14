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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from libica.openapi.v3.models.project_tag import ProjectTag
from typing import Optional, Set
from typing_extensions import Self

class CreateProject(BaseModel):
    """
    CreateProject
    """ # noqa: E501
    name: Annotated[str, Field(min_length=1, strict=True, max_length=255)]
    short_description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=4000)]] = Field(default=None, alias="shortDescription")
    information: Optional[StrictStr] = Field(default=None, description="Information about the project. Note that the value of this field can be arbitrary large.")
    project_owner_id: Optional[StrictStr] = Field(default=None, description="Owner of the project. Defaults to the current user.", alias="projectOwnerId")
    region_id: StrictStr = Field(description="The region of the project. All data and pipeline executions will reside in this region.", alias="regionId")
    billing_mode: StrictStr = Field(description="The billing mode of the project. It determines who pays for the costs linked to the project.", alias="billingMode")
    data_sharing_enabled: StrictBool = Field(description="Indicates whether the Data and Samples created in this Project can be linked to other Projects.", alias="dataSharingEnabled")
    tags: Optional[ProjectTag] = None
    storage_bundle_id: StrictStr = Field(alias="storageBundleId")
    metadata_model_id: Optional[StrictStr] = Field(default=None, alias="metadataModelId")
    storage_configuration_id: Optional[StrictStr] = Field(default=None, description="An optional storage configuration id to have self managed storage.", alias="storageConfigurationId")
    storage_configuration_subfolder: Optional[StrictStr] = Field(default=None, description="An optional subfolder that determines the object prefix of your self managed storage.  If not used, you will not be able to use this storage configuration for any future projects.", alias="storageConfigurationSubfolder")
    analysis_priority: Optional[StrictStr] = Field(default='MEDIUM', description="Indicates the priority given to a project and its analyses within a single tenant, where MEDIUM is the default value.", alias="analysisPriority")
    __properties: ClassVar[List[str]] = ["name", "shortDescription", "information", "projectOwnerId", "regionId", "billingMode", "dataSharingEnabled", "tags", "storageBundleId", "metadataModelId", "storageConfigurationId", "storageConfigurationSubfolder", "analysisPriority"]

    @field_validator('name')
    def name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"[a-zA-Z][a-zA-Z0-9_\s-]*", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z][a-zA-Z0-9_\s-]*/")
        return value

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
        """Create an instance of CreateProject from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of tags
        if self.tags:
            _dict['tags'] = self.tags.to_dict()
        # set to None if short_description (nullable) is None
        # and model_fields_set contains the field
        if self.short_description is None and "short_description" in self.model_fields_set:
            _dict['shortDescription'] = None

        # set to None if information (nullable) is None
        # and model_fields_set contains the field
        if self.information is None and "information" in self.model_fields_set:
            _dict['information'] = None

        # set to None if project_owner_id (nullable) is None
        # and model_fields_set contains the field
        if self.project_owner_id is None and "project_owner_id" in self.model_fields_set:
            _dict['projectOwnerId'] = None

        # set to None if metadata_model_id (nullable) is None
        # and model_fields_set contains the field
        if self.metadata_model_id is None and "metadata_model_id" in self.model_fields_set:
            _dict['metadataModelId'] = None

        # set to None if storage_configuration_id (nullable) is None
        # and model_fields_set contains the field
        if self.storage_configuration_id is None and "storage_configuration_id" in self.model_fields_set:
            _dict['storageConfigurationId'] = None

        # set to None if storage_configuration_subfolder (nullable) is None
        # and model_fields_set contains the field
        if self.storage_configuration_subfolder is None and "storage_configuration_subfolder" in self.model_fields_set:
            _dict['storageConfigurationSubfolder'] = None

        # set to None if analysis_priority (nullable) is None
        # and model_fields_set contains the field
        if self.analysis_priority is None and "analysis_priority" in self.model_fields_set:
            _dict['analysisPriority'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateProject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "shortDescription": obj.get("shortDescription"),
            "information": obj.get("information"),
            "projectOwnerId": obj.get("projectOwnerId"),
            "regionId": obj.get("regionId"),
            "billingMode": obj.get("billingMode"),
            "dataSharingEnabled": obj.get("dataSharingEnabled"),
            "tags": ProjectTag.from_dict(obj["tags"]) if obj.get("tags") is not None else None,
            "storageBundleId": obj.get("storageBundleId"),
            "metadataModelId": obj.get("metadataModelId"),
            "storageConfigurationId": obj.get("storageConfigurationId"),
            "storageConfigurationSubfolder": obj.get("storageConfigurationSubfolder"),
            "analysisPriority": obj.get("analysisPriority") if obj.get("analysisPriority") is not None else 'MEDIUM'
        })
        return _obj


