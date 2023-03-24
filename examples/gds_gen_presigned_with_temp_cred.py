"""
Dependency:
    pip install libica boto3

Usage:
        export ICA_ACCESS_TOKEN=...
        export ICA_BASE_URL=...
    Then
        python gds_gen_presigned_with_temp_cred.py

Issue:
    For some reason, all DRAGEN analysis output files were uploaded to GDS
    with _forced_ MIME ContentType - binary/octet-stream.
    This makes the file to get downloaded when opening a html report in
    inline browser through GDS File PreSigned URL response.

    ica files get gds://<VOLUME>/analysis_data/SBJ00000/umccrise/40230225cbe90c80/[SNIP]_cancer_report.html -ojson | jq '.type, .presignedUrl'

        NOTE:
            binary/octet-stream
            [...]&response-content-type=binary%2Foctet-stream&[...]

    export AWS_PROFILE=ica-temp-cred
    aws s3api head-object --bucket <GDS_BUCKET> --key <GDS_PREFIX>/analysis_data/SBJ00000/umccrise/40230225cbe90c80/[SNIP]_cancer_report.html --no-cli-pager
    {
        "AcceptRanges": "bytes",
        "LastModified": "2023-02-25T19:47:08+00:00",
        "ContentLength": 14790206,
        "ETag": "\"444444444e1834566286f11fb34ca9f7-11\"",
        "ContentType": "binary/octet-stream",                <<<--- HERE _wrong_ MIME ContentType
        "ServerSideEncryption": "AES256",
        "Metadata": {},
        "StorageClass": "INTELLIGENT_TIERING"
    }
"""
import os
from importlib.metadata import version

import boto3
from botocore.exceptions import ClientError

from libica.openapi import libgds
from libica.openapi.libgds import FileResponse, AwsS3TemporaryUploadCredentials

ica_access_token = os.environ['ICA_ACCESS_TOKEN']
ica_base_url = os.getenv('ICA_BASE_URL', "https://aps2.platform.illumina.com")

gds_configuration = libgds.Configuration(
    host=ica_base_url,
    api_key={
        'Authorization': ica_access_token
    },
    api_key_prefix={
        'Authorization': "Bearer"
    },
)

if __name__ == '__main__':

    print(f"libica-{version('libica')}")
    print("-" * 64)

    with libgds.ApiClient(gds_configuration) as api_client:

        files_api = libgds.FilesApi(api_client)
        try:

            resp: FileResponse = files_api.update_file(
                file_id='fil.a420c3d4fbc84eadd19d08d9fddc8a4d',
                include='objectStoreAccess',
            )

            cred: AwsS3TemporaryUploadCredentials = resp.object_store_access.aws_s3_temporary_upload_credentials
            # print(cred)

            expiration = 3600

            s3_client = boto3.client(
                's3',
                aws_access_key_id=cred.access_key_id,
                aws_secret_access_key=cred.secret_access_key,
                aws_session_token=cred.session_token,
                region_name=cred.region,
            )

            signed_url = s3_client.generate_presigned_url(
                'get_object',
                Params={
                    'Bucket': cred.bucket_name,
                    'Key': cred.key_prefix,
                    'ResponseContentType': 'text/html',
                    'ResponseContentDisposition': 'inline',
                },
                ExpiresIn=expiration)

            print(signed_url)

        except libgds.ApiException as e:
            print(f"Exception when calling get_files: \n{e}")

        except ClientError as e:
            print(e)


# See also gds_app_script.py
