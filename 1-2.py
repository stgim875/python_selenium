from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
#
elem = driver.find_element_by_name("q")
#
elem.send_keys("조코딩")
#
elem.send_keys(Keys.RETURN)

driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()

# 이미지가 로딩되는 시간을 지정
time.sleep(3)

# 큰 이미지의 src 주소를 가져와서 찍어주는 print() 이미지
# print(driver.find_element_by_css_selector(".n3VNCb").get_attribute("src"))

# 큰 이미지를 선택하고 여기에 큰 이미지의 src 주소를 가져와야 함
imUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
# src 주소의 이미지를 다운로드
urllib.request.urlretrieve(imUrl, "test.jpg")

driver.close()
