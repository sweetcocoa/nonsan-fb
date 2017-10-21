# coding: utf-8
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



def get_military_address(ENTER_DATE, BIRTHDAY, NAME):
    """
    :param ENTER_DATE: "20171026"  # 훈련소에 입소한 날짜
    :param BIRTHDAY: "980101"  # 찾을 사람 생일
    :param NAME: "김철수"  # 찾을 사람 이름
    :return: 교육연대 / 중대 / 소대 / 교번 / 생년월일 / 이름 / 사진 주소
    """
    browser = webdriver.Chrome()
    browser.get("http://www.katc.mil.kr/katc/community/children.jsp")
    enter_date = browser.find_element_by_id("search_val1")
    enter_date.send_keys(ENTER_DATE, Keys.TAB)
    birthday = browser.find_element_by_id("birthDay")
    birthday.send_keys(BIRTHDAY, Keys.TAB)
    name = browser.find_element_by_id("search_val3")
    name.send_keys(NAME, Keys.RETURN)
    time.sleep(15)