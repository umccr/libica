"""
Usage:
    export ICAV2_ACCESS_TOKEN=$(yq '.access-token' ~/.icav2/.session.ica.yaml)
    cd examples
    python create_cwl_pipeline.py

Debug:
    Uncomment debug flag at Line 30
    export ICAV2_ACCESS_TOKEN=blah
    cd examples
    python create_cwl_pipeline.py

Check:
    Check created CWL pipeline using CLI as follows
    icav2 projectpipelines list | grep libica
"""

import os
import uuid
from importlib.metadata import version
from pathlib import Path

import libica
from libica.openapi.v2 import Configuration
from libica.openapi.v2.api import project_pipeline_api

icav2_access_token = os.environ['ICAV2_ACCESS_TOKEN']
ica_url = "https://ica.illumina.com/ica/rest"

configuration = Configuration(
    host=ica_url,
    access_token=icav2_access_token,
    form_filename_basename=False,  # See use case https://github.com/umccr-illumina/libica/issues/74
)
# configuration.debug = True  # uncomment to debug API call logging

if __name__ == '__main__':

    print(f"libica-{version('libica')}")
    print("-" * 64)

    workflow_package = "tabix-workflow__0.2.6__1677025399"

    workflow_files = [
        workflow_file
        for workflow_file in (Path(workflow_package)).rglob("*")
        if workflow_file.is_file()
    ]

    workflow_file = list(filter(lambda x: x.name == "workflow.cwl", workflow_files))[0]
    params_xml_file = list(filter(lambda x: x.name == "params.xml", workflow_files))[0]
    tool_files = list(filter(lambda x: x.name not in ["workflow.cwl", "params.xml"], workflow_files))

    relative_dir_fd = os.open(str(Path(workflow_package)), os.O_RDONLY)


    def cwl_file_opener(cwl_file_path, flags):
        return os.open(cwl_file_path, flags, dir_fd=relative_dir_fd)


    with libica.openapi.v2.ApiClient(configuration) as api_client:
        api_instance = project_pipeline_api.ProjectPipelineApi(api_client)

        project_id = "9c20aeb0-f780-4e9a-ac42-739b30ed91f3"  # icav2 projects list
        analysis_storage_id = "6e1b6c8f-f913-48b2-9bd0-7fc13eda0fd0"  # icav2 analysisstorages list

        code = f"libica__{workflow_package.replace('.', '-')}__{str(uuid.uuid4())}"
        description = "Testing create CWL Pipeline using libica"

        parameters_xml_file = open(params_xml_file.relative_to(Path(workflow_package)), "rb", opener=cwl_file_opener)

        workflow_cwl_file = open(workflow_file.relative_to(Path(workflow_package)), "rb", opener=cwl_file_opener)

        tool_cwl_files = [
            open(tool_file.relative_to(Path(workflow_package)), "rb", opener=cwl_file_opener)
            for tool_file in tool_files
        ]

        try:
            api_response = api_instance.create_cwl_pipeline(
                project_id=project_id,
                code=code,
                description=description,
                workflow_cwl_file=workflow_cwl_file,
                parameters_xml_file=parameters_xml_file,
                analysis_storage_id=analysis_storage_id,
                tool_cwl_files=tool_cwl_files
            )

            print(api_response)

        except libica.openapi.v2.ApiException as e:
            raise ValueError("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)
