from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


local_List, name_List, addr_List, num_List = ([],[],[],[])
number = 1
for page in range(1,52):
    html = urlopen(f'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={page}&sido=&gugun=&store=')
    soup = BeautifulSoup(html, 'html.parser')
    tbody = soup.find('tbody')
    shop_list = tbody.find_all('tr')
    for shop in shop_list:
        # print('-'*30)
        tests = shop.find_all_next('td')
        local=shop.select_one('td.noline.center_t').text
        # print(local.text)
        name=shop.select_one('td.center_t a').text
        # print(name.text)
        address=tests[3].text
        # print(address)
        num = tests[5].text
        print(f'[{number:3}]: 매장이름: {name}, 지역: {local}, 주소: {address}, 전화번호: {num}')
        local_List.append(local)
        name_List.append(name)
        addr_List.append(address)
        num_List.append(num)
        number += 1


# print(len(local_List))
print(f'전체 매장 수: {len(name_List)}')
# print(len(addr_List))
# print(len(num_List))

DP = pd.DataFrame(name_List, columns=['매장이름'])
DP['위치(시,구)'] = local_List
DP['주소'] = addr_List
DP['전화번호'] = num_List

DP.to_csv('hollys_branches.csv',encoding='utf-8-sig',index=False)
print('hollys_branches.csv 파일 저장 완료')
# 약 10초 소모


