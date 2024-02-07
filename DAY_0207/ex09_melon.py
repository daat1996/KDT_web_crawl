from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup


# 샘플코드 1
# urllib.error.HTTPError: HTTP Error 406: Not Acceptable 발생

melon_url= 'http://www.melon.com/chart/index.htm'
# HTTP request 패킷 생성 :Request()
urlrequest = Request(melon_url, headers={'User-Agent':'Mozilla/5.0'})

html = urlopen(urlrequest)

soup = BeautifulSoup(html.read().decode('utf-8'), 'html.parser')
print(soup)