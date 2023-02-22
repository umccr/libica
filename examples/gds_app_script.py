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
from libica.app import gds


def get_gds_presigned_url():
    is_success, val = gds.presign_gds_file(
        file_id="fil.7a02239fb56f4f8ac22508d98cef9222",
        volume_name="development",
        path_="/reference-data/genomes/hg38/hg38.fa",
        presigned_url_mode="inline",  # default is Attachment mode
    )

    if is_success:
        print('PresignedUrl:', val)

    if not is_success:
        print('e:', val)


if __name__ == '__main__':
    get_gds_presigned_url()
