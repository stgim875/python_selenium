#관련 라이브러리를 불러오는 코드
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # keys를 사용하는 명령어 사용할 경우
from selenium.webdriver.common.by import By  # (BY.xxx, 요소명)을 사용해야한다.
import time  # 대기 시간을 사용할 경우(필수)
import urllib.request  # 어떠한 경로를 사용해야 하는 경우 사용(이미지, 다운로드 등)

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# webdriver 라이브러이를 불러와서 driver 변수에 담는다.
driver = webdriver.Chrome(options=options)

# webdriver를 이용하여 google 홈페이지로 이동한다.
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

# 구글 검색창을 찾는 코드(class 또는 name 요소로 검색창을 찾는다)
# elem = driver.find_element_by_name("q")
elem = driver.find_element(By.NAME, "q")

# 구글 입력창에 "검색어를 입력하는 코드"
elem.send_keys("강아지")

# 검색어 입력 후, 엔터키를 누른다.
elem.send_keys(Keys.RETURN)

# 이미지를 반복적으로 다운로드하는 코드로 변경
# for in 문으로 코드 변경하기
images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

# 

# 이미지들중에 각각 개별 이미지를 하나씩 뽑아서 for 문 안에다 넣고 이 이미지를 클릭하도록한다.
for image in images:
    image.click()
    time.sleep(5)
    imgUrl = driver.find_element(
        By.CSS_SELECTOR, ".n3VNCb.KAlRDb").get_attribute("src")
    urllib.request.urlretrieve(imgUrl, "test.jpg")
