from urllib.request import urlopen
from bs4 import BeautifulSoup


url = 'https://search.naver.com/search.naver?query=%EB%8C%80%EA%B5%AC+%EB%82%A0%EC%94%A8'
html = urlopen(url)
soup = BeautifulSoup(html,'html.parser')
main_pack = soup.select_one('div#main_pack')    # main 시작
weather = main_pack.select_one('section.sc_new.cs_weather_new._cs_weather')
title = weather.find('div',{'class':'title_area _area_panel'})

print(f"현재 위치: {title.find('h2', {'class': 'title'}).text}")
print(f"현재 온도: {weather.select_one('div.temperature_text').text}")
print(f"날씨 상태: {weather.find('span', {'class': 'weather before_slash'}).text}")
air_list = weather.select('ul.today_chart_list > li.item_today')
print(len(air_list))
for air in air_list:
    print(air.text)