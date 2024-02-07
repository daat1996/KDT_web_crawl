import requests
from bs4 import BeautifulSoup

url = 'http://www.naver.com'

html = requests.get(url)
print('html.encoding:', html.encoding)
print(html.text)

soup = BeautifulSoup(html.text, 'html.parser')

print()
print('h1.string:', soup.h1.string)