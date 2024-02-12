from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
soup = BeautifulSoup(html, 'html.parser')

# 등장인물의 이름: 녹색
nameList = soup.find_all('span',{'class':'green'})
for name in nameList:   # 줄바꿈문자(\n)가 있어서 2 줄씩 출력됨
    print(name.string)


# 특정 단어 찾기 : 태그 없이 검색어만으로 'the prince' 검색
# find_all(text='검색어') 또는 string='검색어'
princeList = soup.find_all(text='the prince')
print(princeList)
print(f'the prince count: {len(princeList)}')

