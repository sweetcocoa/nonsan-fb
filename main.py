# coding: utf-8
from nonsan_parser import get_military_address
from fb_poster import post_fb
from datetime import datetime

ENTER_DATE = "20171026"  # 훈련소에 입소한 날짜
BIRTHDAY = "940513"  # 찾을 사람 생일
NAME = "최종호"  # 찾을 사람 이름

mail_address = """
.
훈련소 주소 : http://www.katc.mil.kr/katc/community/children.jsp
.
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
.
소스 코드 : https://github.com/sweetcocoa/nonsan-fb
"""

def get_todays_message():
    DESIRED_STATUS = ""
    today = datetime.today()
    if today.month == 10 and today.day == 23:
        DESIRED_STATUS = """업로드할 메시지
        줄바꿈 포함
        """
    elif today.month == 10 and today.day == 31:
        DESIRED_STATUS = """[논산봇]안녕하세요, 저는 저번 주에 한 달짜리 논산병영캠프에 입소했고, 주소가 나왔어요.
이 프로그램에 문제가 없다면 아마 아래에 제 소속이 표시되었을거에요. 하지만 이건 입소 전에 테스트를 해볼 수가 없으니 어찌 되었을 지 모르겠네요. 
(최악의 경우는 잘못된 소속을 긁어와서 적는건데 그러지만은 않았길)
혹시 제대로 주소가 안찍혔다면 입소일 20171026 / 생일 940513 으로 훈련소 홈페이지에서 조회하실 수 있어요.
아무튼 안에서 심심해하고있을 저를 위해 편지를 써주신다면 아마 큰 힘이 될 것 같습니다. 보내실 때 답장 받을 주소도 꼭 적어주세요. 
사제 우표를 많이 사왔는데 편지가 안오면 어쩌지.. 아 집에가고싶다.
"""
    elif today.month == 11 and today.day == 6:
        DESIRED_STATUS = """[논산봇]안녕하세요. 벌써 11월이 되었군요. 정말 시간이 안 가네요. 지겹습니다. 어라, 어제 월급이 들어왔어요. 부자가 되었습니다. 
한 달 동안 돈을 안쓰고 모은 덕에 편지를 보내주신 분들에게 밖에서 맛있는 밥을 사드릴 수 있다는 생각에 설레네요.  
요즘 재밌는 일 뭐가 있나요. 고급시계 신영웅 떡밥이라든지 검정분홍이 컴백했다든지 하는 가슴뛰고 설레는 이야기가 아니어도 좋습니다. (물론 이 이야기들은 꼭 알려주세요. 꼭이요) 
소소한 잡담도 보내주세요. 인터넷으로도 보낼 수 있나봐요. 아 집에가고싶다.
"""
    elif today.month == 11 and today.day == 12:
        DESIRED_STATUS = """[논산봇]이제 3주차에 접어들었습니다. 밖에서 무서워했던것과 달리 여기도 사람 사는 곳이다보니 생각보다 살만하 
.
긴 무슨 이 메시지를 써둘 때는 입소 전이므로 이 글이 올라올 때의 저는 어떻게 됐을지 모를 일입니다. 주로 신체활동과 담쌓고 지낸 지난 23년에 대한 반성을 하고 있습니다.
언제나 아무말이나 편지로 해주시면 감사하겠습니다. 아 집에가고싶다.
"""
    else:
        exit()

    return DESIRED_STATUS


if __name__ == "__main__":
    DESIRED_STATUS = get_todays_message()
    my_military, image_path = get_military_address(ENTER_DATE=ENTER_DATE, BIRTHDAY=BIRTHDAY, NAME=NAME)  # 교육연대 / 중대 / 소대 / 교번 / 생년월일 / 이름 / 사진파일 주소
    DESIRED_STATUS = DESIRED_STATUS + '\n' + my_military + "\n" + mail_address

    today = datetime.today()
    if today.month == 10 and today.day == 31:
        pass
    else:
        image_path = None

    # post_fb(DESIRED_STATUS=DESIRED_STATUS, POST_IMAGE_URL=image_path)
    print(DESIRED_STATUS)
