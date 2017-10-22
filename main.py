# coding: utf-8
from nonsan_parser import get_military_address
from fb_poster import post_fb
from datetime import datetime

ENTER_DATE = "20171026"  # 훈련소에 입소한 날짜
BIRTHDAY = "940513"  # 찾을 사람 생일
NAME = "최종호"  # 찾을 사람 이름

mail_address = """
ㆍ23연대 : [33012] 충남 논산시 연무읍 사서함 76-8호 
   ☎ 041)740- 6322 
ㆍ25연대 : [33012] 충남 논산시 연무읍 사서함 76-9호
   ☎ 041)740-6522 
ㆍ26연대 : [33012] 충남 논산시 연무읍 사서함 76-10호 
   ☎ 041)740-6622 
ㆍ27연대 : [33012] 충남 논산시 연무읍 사서함 76-11호 
   ☎ 041)740-6722 
ㆍ28연대 : [33012] 충남 논산시 연무읍 사서함 76-12호 
   ☎ 041)740-6822 
ㆍ29연대 : [33012] 충남 논산시 연무읍 사서함 76-13호
   ☎ 041)740-6922 
ㆍ30연대 : [33012] 충남 논산시 연무읍 사서함 76-14호
   ☎ 041)740-6422 
"""

def get_todays_message():
    DESIRED_STATUS = ""
    today = datetime.today()
    if today.month == 10 and today.day == 23:
        DESIRED_STATUS = """업로드할 메시지
        줄바꿈 포함
        """
    elif today.month == 10 and today.day == 31:
        DESIRED_STATUS = """주소가 나왔어요"""
    elif today.month == 11 and today.day == 6:
        DESIRED_STATUS = """입소 2주일 지남
        ㄷㄷ
        """
    elif today.month == 11 and today.day == 12:
        DESIRED_STATUS = """주말에 심심하면 편지라도 한 통
        """
    elif today.month == 11 and today.day == 16:
        DESIRED_STATUS = """
        헉 이제 일주일남았다 마지막편지 ㄱ
        """
    else:
        exit()

    return DESIRED_STATUS


if __name__ == "__main__":
    DESIRED_STATUS = get_todays_message()
    my_military, image_path = get_military_address(ENTER_DATE=ENTER_DATE, BIRTHDAY=BIRTHDAY, NAME=NAME)  # 교육연대 / 중대 / 소대 / 교번 / 생년월일 / 이름 / 사진파일 주소

    DESIRED_STATUS = DESIRED_STATUS + '\n' + my_military + "\n" + mail_address

    # post_fb(DESIRED_STATUS=DESIRED_STATUS, POST_IMAGE_URL=image_path)
    print(DESIRED_STATUS)
