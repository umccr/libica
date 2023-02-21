# libica.app

## Using [App Package](https://umccr-illumina.github.io/libica/libica/app/index.html)

> NOTE: `libica.app` package contains reusable modules that are based on use cases around UMCCR [Data Portal backend](https://github.com/umccr/data-portal-apis), [Workflows automation and orchestration](https://github.com/umccr/data-portal-apis/tree/dev/docs/pipeline) implementations. Hence, it may be a specific domain logic implementation. However, it may still be reusable for your use cases. Starter examples are as follows.

### App for ICA v2

See [pilotapp.py](https://github.com/umccr-illumina/libica/blob/main/examples/pilotapp.py)

Example: `ProjectDataOps` app to list project files, download a file, etc...

```python
from contextlib import closing

from libica.app import AppHelper
from libica.app.dataops import ProjectDataOps
from libica.openapi.v2 import ApiClient
from libica.openapi.v2.model.project_data import ProjectData

# --- Use AppHelper to build SDK API client

app_helper = AppHelper(debug=False)
project_id = app_helper.get_icav2_cli_session_project_id()

cli_session_api_client: ApiClient = app_helper \
    .build_icav2_configuration_with_cli_session() \
    .get_icav2_api_client()

# --- Construct ProjectDataOps from dataops module

project_dataops = ProjectDataOps(project_id=project_id, api_client=cli_session_api_client)

# --- List all files under given project's folder

# If you do not cd into the folder, it will list all files under the project
project_dataops.cd("/test_folder/")

for item in project_dataops.list_files():
    project_data: ProjectData = item
    print((
        project_data.data.id,  # fil.<ID> (or) fol.<ID>
        project_data.data.details.path,
        project_data.data.details.data_type,
        project_data.data.details.name,
        project_data.data.details.status,
        project_data.data.details.file_size_in_bytes,
        project_data.data.details.time_created,
    ))

# --- Download csv file from given project and file path

file_path = "/test_folder/SampleSheet.csv"
print(f"Downloading {file_path} from project_id {project_id}")
project_dataops.cd(file_path=file_path)
ntf = project_dataops.download_file()
with closing(ntf) as cf:
    with open(cf.name, 'r') as f:
        for line in f.readlines():
            print(line)
```

For more, see PyDoc: 
- https://umccr-illumina.github.io/libica/libica/app/dataops.html

### App for ICA v1

Example: Configuration Object Builder

```python
from libica.app import configuration
from libica.openapi import libgds

gds_config = configuration(
  lib=libgds,  # pass in library of interest e.g. libwes, libtes, etc 
  secret_name=["FROM_AWS_SECRET_MANAGER_THAT_STORE_ICA_ACCESS_TOKEN"],
  base_url="https://use1.platform.illumina.com",  # overwrite if not https://aps2.platform.illumina.com
  debug=False,  # True if you like to debug API calls, False by default anyway, just for demo
)

with libgds.ApiClient(gds_config) as api_client:
    ...
```

Example: Listing Files from GDS

```python
from typing import List

from libica.app import gds
from libica.openapi import libgds

vol, path = gds.parse_path("gds://development/some/folder/path/")
files: List[libgds.FileResponse] = gds.get_file_list(volume_name=vol, path=path)

for file in files:
  print(f"{file.name}, {file.volume_name}, {file.path}, {file.presigned_url}")
```
