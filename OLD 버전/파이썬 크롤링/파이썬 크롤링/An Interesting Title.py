from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#객체를 만들 때는 두가지 매개변수가 들어감, 첫번째 매개변수는 객체의 근간이 되는 HTML 텍스트이고, 
#두번째 매개변수는 BeautifulSoup가 객체를 만들 때 쓰는 구문분석기이고 직접 지정 할 수 있음.
#책에서는 계속 'html.parser' 계속 사용 할 것이고 'lxml'도 널리 쓰이는 분석기임
#bs = BeautifulSoup(html.read(), 'html.parser')
#bs = BeautifulSoup(html, 'html.parser') # .read() 호출하지 않고 urlopen 반환
bs = BeautifulSoup(html.read(), 'lxml') # pip install lxml로 다운로드, 지저분한 HTML 코드 분석할 때 사용
print(bs.h1)