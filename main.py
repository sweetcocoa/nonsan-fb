# coding: utf-8
from nonsan_parser import get_military_address
from fb_poster import post_fb

ENTER_DATE = "20171026"  # 훈련소에 입소한 날짜
BIRTHDAY = "980101"  # 찾을 사람 생일
NAME = "김철수"  # 찾을 사람 이름
DESIRED_STATUS = "업로드할 메시지"

NotImplemented_return = get_military_address(ENTER_DATE=ENTER_DATE, BIRTHDAY=BIRTHDAY, NAME=NAME)  # 교육연대 / 중대 / 소대 / 교번 / 생년월일 / 이름 / 사진파일 주소
post_fb(DESIRED_STATUS=DESIRED_STATUS)

# post_msg.send_keys("your_message")
# ActionChains(browser).key_down(Keys.CONTROL).send_keys(Keys.RETURN).perform();
