from selenium import webdriver  # 크롬 셀레니움을 불러 온다.
# from selenium.webdriver.common.keys import Keys #

driver = webdriver.Chrome('C:\python38\chromedriver.exe')  # 크롬 드라이버 위치
url = "https://google.com"
driver.get(url)

# #단수와 복수가 있음 's'로 끝나면 복수임
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
#
# #LC20lb DKV0Md
driver.find_elements_by_css_selector('.LC20lb.DKV0Md')[0].click()
