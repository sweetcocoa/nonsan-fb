# coding: utf-8
from facepy import GraphAPI


def post_fb(DESIRED_STATUS, POST_IMAGE_URL = None):
    """

    :param DESIRED_STATUS: 포스팅할 메시지.
    :param POST_IMAGE_URL: 포스팅할 사진 (선택사항)
    :return: None
    """
    # 'https://developers.facebook.com/' 에서 2개월 장기 토큰을 생성해야함

    YOUR_ACCESS_TOKEN = "{YOUR_ACCRESS_TOKEN}"
    access_token = YOUR_ACCESS_TOKEN
    apiConnection = GraphAPI(access_token)

    # 포스팅이 안되면 토큰 권한 확인
    # print(apiConnection.get(path="/me/permissions"))

    # 사진 업로드는 있으면 하고 없으면 말고
    if POST_IMAGE_URL is None:
        apiConnection.post(path='me/feed', message=DESIRED_STATUS)
    else:
        print(apiConnection.post(path='me/photos', url=POST_IMAGE_URL, caption=DESIRED_STATUS))