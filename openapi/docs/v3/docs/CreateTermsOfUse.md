# CreateTermsOfUse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms_of_use** | **str** | Terms of Use for a bundle. Supports plain text or HTML. | 
**requires_user_acceptance** | **bool** | Flag indicating whether the Terms of Use should be accepted before using/viewing the bundle. | 
**release_version** | **str** | Version number of the Terms of Use. | 
**reset_acceptance_records** | **bool** | Do you want to reset the acceptance records. | 

## Example

```python
from libica.openapi.v3.models.create_terms_of_use import CreateTermsOfUse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTermsOfUse from a JSON string
create_terms_of_use_instance = CreateTermsOfUse.from_json(json)
# print the JSON string representation of the object
print(CreateTermsOfUse.to_json())

# convert the object into a dict
create_terms_of_use_dict = create_terms_of_use_instance.to_dict()
# create an instance of CreateTermsOfUse from a dict
create_terms_of_use_from_dict = CreateTermsOfUse.from_dict(create_terms_of_use_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


