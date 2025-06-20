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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from libica.openapi.v3.models.analysis_base_space_data_details import AnalysisBaseSpaceDataDetails
from libica.openapi.v3.models.analysis_s3_data_details import AnalysisS3DataDetails
from typing import Optional, Set
from typing_extensions import Self

class AnalysisInputExternalData(BaseModel):
    """
    AnalysisInputExternalData
    """ # noqa: E501
    url: StrictStr
    type: Annotated[str, Field(strict=True)]
    mount_path: Optional[StrictStr] = Field(default=None, description="The mount path is the location where the input file will be located on the machine that is running the pipeline. The use of a relative path is encouraged, but an absolute path is also allowed. The path should end with the file name, which may differ from the original input data.", alias="mountPath")
    s3_details: Optional[AnalysisS3DataDetails] = Field(default=None, alias="s3Details")
    basespace_details: Optional[AnalysisBaseSpaceDataDetails] = Field(default=None, alias="basespaceDetails")
    __properties: ClassVar[List[str]] = ["url", "type", "mountPath", "s3Details", "basespaceDetails"]

    @field_validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"s3|http|basespace", value):
            raise ValueError(r"must validate the regular expression /s3|http|basespace/")
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
        """Create an instance of AnalysisInputExternalData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of s3_details
        if self.s3_details:
            _dict['s3Details'] = self.s3_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of basespace_details
        if self.basespace_details:
            _dict['basespaceDetails'] = self.basespace_details.to_dict()
        # set to None if mount_path (nullable) is None
        # and model_fields_set contains the field
        if self.mount_path is None and "mount_path" in self.model_fields_set:
            _dict['mountPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnalysisInputExternalData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "url": obj.get("url"),
            "type": obj.get("type"),
            "mountPath": obj.get("mountPath"),
            "s3Details": AnalysisS3DataDetails.from_dict(obj["s3Details"]) if obj.get("s3Details") is not None else None,
            "basespaceDetails": AnalysisBaseSpaceDataDetails.from_dict(obj["basespaceDetails"]) if obj.get("basespaceDetails") is not None else None
        })
        return _obj


