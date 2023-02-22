"""
Usage:
    Either
        Have your AWS_PROFILE set up and use the credentials to ICA
    Or
        export ICA_ACCESS_TOKEN=...
        export ICA_BASE_URL=...
    Then
        python gds.py
"""
from libica.app import gds


def get_gds_presigned_url():
    is_success, val = gds.presign_gds_file(file_id="fil.{NUMBER}", volume_name="development",
                                           path_="somePath",
                                           presigned_url_mode="inline")

    if is_success:
        print('PresignedUrl:', val)

    if not is_success:
        print('e:', val)


if __name__ == '__main__':
    get_gds_presigned_url()
