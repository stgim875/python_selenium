from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# # webdriver_manager를 설치하여 항상 최신 버전으로 자동으로 업데이트 하기
# from webdriver_manager.chrome import ChromeDriverManager

# 항상 최신 webdriver.Chrome 설치하기
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()  # 크롬 드라이버 실행하기
url = 'https://google.com'
driver.get(url)

driver.find_element_by_css_selector('.gLFyfgsfi').send_keys('파이썬')


# 단수와 복수가 있음 's'로 끝나면 복수임
# driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('파이썬')
# driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)
