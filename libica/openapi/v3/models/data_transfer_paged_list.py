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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from libica.openapi.v3.models.data_transfer import DataTransfer
from typing import Optional, Set
from typing_extensions import Self

class DataTransferPagedList(BaseModel):
    """
    DataTransferPagedList
    """ # noqa: E501
    items: List[DataTransfer]
    next_page_token: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=2000)]] = Field(default=None, description="The cursor to request the next page. For offset-based paging the value is an empty string.", alias="nextPageToken")
    remaining_records: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The number of records remaining (used in cursor based pagination)", alias="remainingRecords")
    total_item_count: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, description="The total number of records matching the search criteria (used in offset based pagination)", alias="totalItemCount")
    __properties: ClassVar[List[str]] = ["items", "nextPageToken", "remainingRecords", "totalItemCount"]

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
        """Create an instance of DataTransferPagedList from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item_items in self.items:
                if _item_items:
                    _items.append(_item_items.to_dict())
            _dict['items'] = _items
        # set to None if next_page_token (nullable) is None
        # and model_fields_set contains the field
        if self.next_page_token is None and "next_page_token" in self.model_fields_set:
            _dict['nextPageToken'] = None

        # set to None if remaining_records (nullable) is None
        # and model_fields_set contains the field
        if self.remaining_records is None and "remaining_records" in self.model_fields_set:
            _dict['remainingRecords'] = None

        # set to None if total_item_count (nullable) is None
        # and model_fields_set contains the field
        if self.total_item_count is None and "total_item_count" in self.model_fields_set:
            _dict['totalItemCount'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataTransferPagedList from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "items": [DataTransfer.from_dict(_item) for _item in obj["items"]] if obj.get("items") is not None else None,
            "nextPageToken": obj.get("nextPageToken"),
            "remainingRecords": obj.get("remainingRecords"),
            "totalItemCount": obj.get("totalItemCount")
        })
        return _obj


