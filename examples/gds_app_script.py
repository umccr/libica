"""
Usage:
    Either
        Have your AWS_PROFILE set up and use the credentials to ICA
    Or
        export ICA_ACCESS_TOKEN=...
        export ICA_BASE_URL=...
    Then
        python gds_app_script.py
"""
from importlib.metadata import version

from libica.app import gds


def get_gds_presigned_url():
    is_success, val = gds.presign_gds_file(
        file_id="fil.7a02239fb56f4f8ac22508d98cef9222",
        volume_name="development",
        path_="/reference-data/genomes/hg38/hg38.fa",
        presigned_url_mode="inline",  # default is Attachment mode
    )

    if is_success:
        print('\n', val)
    else:
        print('e:', val)


def get_gds_presigned_url_with_override():
    success, value = gds.presign_gds_file_with_override(
        file_id="fil.a420c3d4fbc84eadd19d08d9fddc8a4d",
        expiration="3600",
        response_content_type="text/html",
        response_content_disposition="inline",
    )

    if success:
        print('\n', value)
    else:
        print('e:', value)


if __name__ == '__main__':
    print(f"libica-{version('libica')}")
    print("-" * 64)
    get_gds_presigned_url()
    print("-" * 64)
    get_gds_presigned_url_with_override()
