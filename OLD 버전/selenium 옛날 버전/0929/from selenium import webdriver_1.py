from selenium import webdriver
path = "C:\python38\chromedriver.exe"    #ex. C:/downloads/chromedriver.exe
driver = webdriver.Chrome(path) #조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다.
driver.implicitly_wait(3) # 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
#driver.get('http://192.168.102.202:9999/') #IMA url에 접근한다.
driver.get('https://nid.naver.com/nidlogin.login') #네이버 로그인 화면에 접근한다.
driver.find_element_by_name('id').send_key('marie875th')
driver.find_element_by_name('pw').send_key('@rokmc875th#')