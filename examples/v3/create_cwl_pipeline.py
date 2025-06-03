"""
Use Case:
    Consider we have the following CWL workflow folder structure.

        $ tree tabix-workflow__0.2.6__1677025399
        tabix-workflow__0.2.6__1677025399
        ├── params.xml
        ├── tools
        │   └── tabix
        │       └── 0.2.6
        │           └── tabix__0.2.6.cwl
        └── workflow.cwl

    We wish to create the pipeline in ICA Flow while maintaining the workflow folder hierarchy structure.
    See the use case https://github.com/umccr/libica/issues/74

    In this case, we wish to organise at root level - params.xml, workflow.cwl
    Then, inside into subdirectory - tools/tabix/0.2.6/tabix__0.2.6.cwl

Usage:
    export ICAV2_ACCESS_TOKEN=$(icav2 tokens create)
    cd examples
    python create_cwl_pipeline.py

Check:
    You can check the example CWL pipeline created using this way via CLI as follows
        icav2 projects enter 'development'
        icav2 projectpipelines list | grep libica
"""

import os
import uuid
from importlib.metadata import version
from pathlib import Path

from libica.openapi.v3 import Configuration, ApiClient, ApiException, ProjectPipelineApi

configuration = Configuration(
    host="https://ica.illumina.com/ica/rest",
    access_token=os.environ['ICAV2_ACCESS_TOKEN'],
)
# configuration.debug = True  # uncomment to debug API call logging


if __name__ == '__main__':

    print(f"libica-{version('libica')}")
    print("-" * 64)

    project_id = "ea19a3f5-ec7c-4940-a474-c31cd91dbad4"  # icav2 projects list
    analysis_storage_id = "6e1b6c8f-f913-48b2-9bd0-7fc13eda0fd0"  # icav2 analysisstorages list

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


    with ApiClient(configuration) as api_client:
        api_instance = ProjectPipelineApi(api_client)

        code = f"libica__{workflow_package.replace('.', '-')}__{str(uuid.uuid4())}"
        description = "Testing create CWL Pipeline using libica v3"

        parameters_xml_file = open(params_xml_file.relative_to(Path(workflow_package)), "rb", opener=cwl_file_opener)

        workflow_cwl_file = open(workflow_file.relative_to(Path(workflow_package)), "rb", opener=cwl_file_opener)

        tool_cwl_files = []
        for tool_file in tool_files:
            file_instance = open(tool_file.relative_to(Path(workflow_package)), "rb", opener=cwl_file_opener)
            tool_cwl_files.append((file_instance.name, file_instance.read()))

        # In v3 SDK, basically we need to prepare the data structure such that
        #
        #       tuple("params.xml", bytes<FileContent>)
        #       tuple("workflow.cwl", bytes<FileContent>)
        #       [tuple("tools/tabix/0.2.6/tabix__0.2.6.cwl", bytes<FileContent>)]
        #
        # Uncomment the following to debug / observe
        #
        # print((parameters_xml_file.name, parameters_xml_file.read()))
        # print((workflow_cwl_file.name, workflow_cwl_file.read()))
        # print(tool_cwl_files)

        try:
            api_response = api_instance.create_cwl_pipeline(
                project_id=project_id,
                analysis_storage_id=analysis_storage_id,
                code=code,
                description=description,
                parameters_xml_file=(parameters_xml_file.name, parameters_xml_file.read()),
                workflow_cwl_file=(workflow_cwl_file.name, workflow_cwl_file.read()),
                tool_cwl_files=tool_cwl_files,
            )

            print(api_response)

        except ApiException as e:
            raise ValueError("Exception when calling ProjectPipelineApi->create_cwl_pipeline: %s\n" % e)
