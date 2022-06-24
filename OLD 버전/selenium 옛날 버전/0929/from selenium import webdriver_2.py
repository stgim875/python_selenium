#-*- coding: utf-8 -*- 
from selenium import webdriver
driver = webdriver.Chrome('C:\python38\chromedriver.exe') #크롬 드라이버 실행하기
driver.implicitly_wait(3) #암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
#driver.get("http://192.168.102.202:9999/") #IMA url에 접근한다.
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com") #네이버 로그인 화면에 접근한다.
#driver.find_element_by_name('id').send_keys('marie875th')
#driver.find_element_by_name('pw').send_keys('@rokmc875th#')
#driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()