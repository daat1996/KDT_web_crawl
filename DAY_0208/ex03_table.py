from bs4 import BeautifulSoup
from urllib.request import urlopen

# 트리이동
#   - 문서내부에서 특정위치를 기준으로 태그를 찾을때 단방향으로 트리 이동

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(html, 'html.parser')

table_tag = soup.find('table', {'id':'giftList'})
print('children 개수: ',len(list(table_tag.children)))    # 아래의 children(자식) 갯수
for child in table_tag.children:
    print(child)
    print('-'*30)
# \n 도 하위 자식으로 포함을 시켜버림


# 자손: descendants
desc = soup.find('table',{'id':'giftList'}).descendants

list_desc = list(desc)
print('descendants 개수: ', len(list_desc))

# for tag in list_desc:
    # print(tag)


# 형제: next_siblings 속성
#   - 임의의 행을 선택하고 next_siblings을 선택하면, 모든 형제(테이블의 다음행들을 모두 선택)
#   - s를 빼면(next_sibling) 단수를 찾음
for sibling in soup.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)

# 형제: previous_siblings
#   - 선택된 행 이전의 항목들을 선택
for sibling in soup.find('tr',{'id':'gift2'}).previous_siblings:
    print(sibling)


# 문자열 마지막에 whitespace('\n', '\r'등)가 있는 경우
# 해당 whitespace를 next_sibling으로 반환

sibling1 = soup.find('tr', {'id':'gift3'}).next_sibling
print('siblings:', sibling1)
print(ord(sibling1))    # ord(문자): 문자의 Unicode 정수를 리턴


# 트리 이동 : 부모 다루기
# parent 사용
style_tag = soup.style
print(style_tag.parent)


img1 = soup.find('img',{'src':'../img/gifts/img1.jpg'})
text = img1.parent.previous_sibling.get_text()
# parent: 부모 tag를 먼저 검색(<td>) -> previous_sibling:부모 태그의 이전형제 태그 검색
# -> get_text(): 태그 내부의 문자열 반환
print(text)


