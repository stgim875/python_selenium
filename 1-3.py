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
# #
# elem.send_keys(Keys.RETURN)

# # '더이상 표시할 콘텐츠가 없습니다.' 나올 때까지 스크롤 하면서 결과 더 보기 클릭하는 방법
# SCROLL_PAUSE_TIME = 0.5

# # Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         try:
#             driver.find_element_by_css_selector(".mye4qd").click()
#         except:
#             break
#     last_height = new_height

# # 반복문을 사용하여 이미지를 다운로드
# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

# count = 1
# for images in images:
#     try:
#         images.click()
#         time.sleep(3)
#         imUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
#         urllib.request.urlretrieve(imUrl, str(count) + ".jpg")
#         count = count + 1
#     except:
#         pass

# driver.close()
