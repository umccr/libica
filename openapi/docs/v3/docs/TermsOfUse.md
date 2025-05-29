# TermsOfUse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms_of_use** | **str** | Terms of Use for a bundle. Supports plain text or HTML. | 
**requires_user_acceptance** | **bool** | Flag indicating whether the Terms of Use should be accepted before using/viewing the bundle. | 
**release_version** | **str** | Version number of the Terms of Use. | [optional] 

## Example

```python
from libica.openapi.v3.models.terms_of_use import TermsOfUse

# TODO update the JSON string below
json = "{}"
# create an instance of TermsOfUse from a JSON string
terms_of_use_instance = TermsOfUse.from_json(json)
# print the JSON string representation of the object
print(TermsOfUse.to_json())

# convert the object into a dict
terms_of_use_dict = terms_of_use_instance.to_dict()
# create an instance of TermsOfUse from a dict
terms_of_use_from_dict = TermsOfUse.from_dict(terms_of_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


