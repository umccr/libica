# TermsOfUseAcceptance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accepted** | **bool** | Are the terms of use accepted | 
**first_acceptance_date** | **datetime** | Date of the first time the terms of use were accepted. | 
**version_terms_of_use_first_accept** | **str** | Version of the first accepted Terms of Use. | 
**last_acceptance_date** | **datetime** | Date of the last time the terms of use were accepted. | [optional] 
**version_terms_of_use_last_accept** | **str** | Version of the last accepted Terms of Use. | [optional] 

## Example

```python
from libica.openapi.v3.models.terms_of_use_acceptance import TermsOfUseAcceptance

# TODO update the JSON string below
json = "{}"
# create an instance of TermsOfUseAcceptance from a JSON string
terms_of_use_acceptance_instance = TermsOfUseAcceptance.from_json(json)
# print the JSON string representation of the object
print(TermsOfUseAcceptance.to_json())

# convert the object into a dict
terms_of_use_acceptance_dict = terms_of_use_acceptance_instance.to_dict()
# create an instance of TermsOfUseAcceptance from a dict
terms_of_use_acceptance_from_dict = TermsOfUseAcceptance.from_dict(terms_of_use_acceptance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


