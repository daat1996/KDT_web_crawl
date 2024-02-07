from urllib.request import urlopen
from bs4 import BeautifulSoup

# 사이트 주소 가져와서 url 오픈
url = 'https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168'

# # print(html.read())
# soup = BeautifulSoup(html, 'html.parser')
# # print(html.read())  # 이거 read 형식이었냐
#
# # print(soup)
#
# # ul 태그의 id:seven-day-forecast-list 갖는 결과 추출
# ul = soup.find('ul',{'id':'seven-day-forecast-list'})
# # print(ul)
#
# # <p>에서 나오는 class:'period-name','short-desc','temp' 1개씩 필요
# # 근데 'temp'는 첫 리스트에 없으니 예외처리(except)
# tombs_list = ul.find_all('div',{'class':'tombstone-container'})
# print(len(tombs_list))

def scraping_use_find(html):
    html=urlopen(html)
    soup = BeautifulSoup(html.read(), 'html.parser')
    ul = soup.find('ul', {'id': 'seven-day-forecast-list'})
    tombs_list = ul.find_all('div', {'class': 'tombstone-container'})
    print('--------------------------------------')
    print('[find 함수 사용]')
    print(f"총 tombstone-container 검색 개수 : {len(tombs_list)}")
    for tombs in tombs_list:
        print('--------------------------------------'*2)
        print(f"[Period]: {tombs.find('p',{'class':'period-name'}).text}")
        print(f"[short desc]: {tombs.find('p',{'class':'short-desc'}).text}")
        try:
            print(f"[Temperature]: {tombs.find('p',{'class':'temp'}).text}")
        except:
            print(f"[Temperature]: none ")
        print(f"[Image desc]: {tombs.find('img')}")


def scraping_use_select(html):
    html = urlopen(html)
    soup = BeautifulSoup(html.read(), 'html.parser')
    ul = soup.select_one('ul#seven-day-forecast-list'   )
    tombs_list = ul.select('div.tombstone-container')
    print('--------------------------------------')
    print('[select 함수 사용]')
    print(f"총 tombstone-container 검색 개수 : {len(tombs_list)}")
    for tombs in tombs_list:
        print('--------------------------------------' * 2)
        print(f"[Period]: {tombs.select_one('p.period-name').text}")
        print(f"[short desc]: {tombs.select_one('p.short-desc').text}")
        try:
            print(f"[Temperature]: {tombs.select_one('p.temp').text}")
        except:
            print(f"[Temperature]: none ")
        print(f"[Image desc]: {tombs.select_one('img')}")


scraping_use_find(url)
scraping_use_select(url)

