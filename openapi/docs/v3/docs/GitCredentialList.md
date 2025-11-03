# GitCredentialList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[GitCredential]**](GitCredential.md) |  | 
**next_page_token** | **str** | The cursor to request the next page. For offset-based paging the value is an empty string. | [optional] 
**remaining_records** | **int** | The number of records remaining (used in cursor based pagination) | [optional] 
**total_item_count** | **int** | The total number of records matching the search criteria (used in offset based pagination) | [optional] 

## Example

```python
from libica.openapi.v3.models.git_credential_list import GitCredentialList

# TODO update the JSON string below
json = "{}"
# create an instance of GitCredentialList from a JSON string
git_credential_list_instance = GitCredentialList.from_json(json)
# print the JSON string representation of the object
print(GitCredentialList.to_json())

# convert the object into a dict
git_credential_list_dict = git_credential_list_instance.to_dict()
# create an instance of GitCredentialList from a dict
git_credential_list_from_dict = GitCredentialList.from_dict(git_credential_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


