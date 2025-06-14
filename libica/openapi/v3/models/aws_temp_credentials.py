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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class AwsTempCredentials(BaseModel):
    """
    AwsTempCredentials
    """ # noqa: E501
    access_key: StrictStr = Field(description="The S3 access key.", alias="accessKey")
    secret_key: StrictStr = Field(description="The S3 secret key.", alias="secretKey")
    session_token: StrictStr = Field(description="The S3 session token.", alias="sessionToken")
    region: StrictStr = Field(description="The S3 region.")
    bucket: StrictStr = Field(description="The S3 bucket name.")
    object_prefix: StrictStr = Field(description="The S3 object prefix these temporary credentials will give access to.", alias="objectPrefix")
    server_side_encryption_algorithm: Optional[StrictStr] = Field(default=None, description="Used to specify the type of server-side encryption (SSE) to be used on the object provider. This value is used to determine the Amazon S3 header \"x-amz-server-side-encryption\" value. For example, specify \"AES256\" for SSE-S3, or \"AWS:KMS\" for SSE-KMS. By default if none is specified, \"AES256\" will be used.", alias="serverSideEncryptionAlgorithm")
    server_side_encryption_key: Optional[StrictStr] = Field(default=None, description="Used to specify the server-side encryption key that might be associated with the specified server-side encryption algorithm. This value can be the AWS KMS arn key, to be used for the Amazon S3 header \"x-amz-server-side-encryption-aws-kms-key-id\" value. Value will be ignored if encryption is \"AES256\"", alias="serverSideEncryptionKey")
    __properties: ClassVar[List[str]] = ["accessKey", "secretKey", "sessionToken", "region", "bucket", "objectPrefix", "serverSideEncryptionAlgorithm", "serverSideEncryptionKey"]

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
        """Create an instance of AwsTempCredentials from a JSON string"""
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
        # set to None if server_side_encryption_algorithm (nullable) is None
        # and model_fields_set contains the field
        if self.server_side_encryption_algorithm is None and "server_side_encryption_algorithm" in self.model_fields_set:
            _dict['serverSideEncryptionAlgorithm'] = None

        # set to None if server_side_encryption_key (nullable) is None
        # and model_fields_set contains the field
        if self.server_side_encryption_key is None and "server_side_encryption_key" in self.model_fields_set:
            _dict['serverSideEncryptionKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AwsTempCredentials from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "accessKey": obj.get("accessKey"),
            "secretKey": obj.get("secretKey"),
            "sessionToken": obj.get("sessionToken"),
            "region": obj.get("region"),
            "bucket": obj.get("bucket"),
            "objectPrefix": obj.get("objectPrefix"),
            "serverSideEncryptionAlgorithm": obj.get("serverSideEncryptionAlgorithm"),
            "serverSideEncryptionKey": obj.get("serverSideEncryptionKey")
        })
        return _obj


