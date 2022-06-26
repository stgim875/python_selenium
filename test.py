#관련 라이브러리를 불러오는 코드
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # keys를 사용하는 명령어 사용할 경우
from selenium.webdriver.common.by import By # (BY.xxx, 요소명)을 사용해야한다.
import time # 대기 시간을 사용할 경우(필수)
import urllib.request  # 어떠한 경로를 사용해야 하는 경우 사용(이미지, 다운로드 등)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# webdriver 라이브러이를 불러와서 driver 변수에 담는다.
driver = webdriver.Chrome(options=options)

# webdriver를 이용하여 google 홈페이지로 이동한다.
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

# 구글 검색창을 찾는 코드(class 또는 name 요소로 검색창을 찾는다)
# elem = driver.find_element_by_name("q")
elem= driver.find_element(By.NAME, "q")

# 구글 입력창에 "검색어를 입력하는 코드"
elem.send_keys("강아지")

# 검색어 입력 후, 엔터키를 누른다.
elem.send_keys(Keys.RETURN)

# 여러 이미지 일 경우 element는 "s"가 붙은 elements를 선택한다.
# class 요소명에 빈 공간이 있는 경우 . 으로 연결? 해줘야한다. "rg_i Q4LuWd" > ".rg_i.Q4LuWd"
# 리스트 형식으로 출력되는 이미지 또는 내용일 경우 리스트 개념을 적용한다.
driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")[0].click()

# 이미지를 선택하고 모든 이미지가 출력될 때까지 대기
time.sleep(5)

# 여러 이미지 중에서 한가지 이미지를 선택하기 때문에 element를 선택한다.
# 전체 코드를 한번 print로 감싸주고 나서 실행을 하면 터미널에 이미지 경로가 출력된다.
# print(driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb").get_attribute("src"))
# 이전 코드를 image 라는 변수에 담는다.
imgUrl = driver.find_element(By.CSS_SELECTOR, ".n3VNCb.KAlRDb").get_attribute("src")
# imgUrl 변수를 괄호안에() 넣어준다, 그리고 파일명을 test로 지정해준다.
urllib.request.urlretrieve(imgUrl, "test.jpg")