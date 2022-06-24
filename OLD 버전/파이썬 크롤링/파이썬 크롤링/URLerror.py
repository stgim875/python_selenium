from urllib.request import urlopen
from urllib.request import HTTPError
from urllib.request import URLError

try:
    html = urlopen('http://www.pythonscrapingthisurldoesnotextist.com')
except HTTPError as e:
    print(e)
except URLError as e:
    print('The sever could not be found')
else:
    print('It Worked!')
    #print(bs.nonExistentTag)
    #print(bs.nonExistenTag.someTag)