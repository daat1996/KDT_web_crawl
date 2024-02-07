from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.daangn.com/hot_articles')
bs = BeautifulSoup(html.read(), 'html.parser')

print(bs.h1)        # 해당 url에서 첫번째 h1 태그를 반환
print(bs.h1.string.strip())     # 태그 내부의 텍스트만 반환

html_example = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BeautifulSoup 활용</title>
</head>
<body>
    <h1 id="heading">Heading 1</h1>
    <p>Paragraph</p>
     <span	class="red">BeautifulSoup	Library	Examples!</span>
    <div id="link">
        <a class="external_link", href="www.google.com">google</a>

        <div id="class1">
            <p id="first">class1's first paragraph</p>
            <a class="exteranl_link", href="www.naver.com">naver</a>

            <p id="second">class1's second paragraph</p>
            <a class="internal_link", href="/pages/page1.html">Page1</a>
            <p id="third">class1's third paragraph</p>
        </div>
    </div>
    <div id="text_id2">
        Example page
        <p>g</p>
    </div>
    <h1 id="footer">Footer</h1>
</body>
</html>
'''

soup = BeautifulSoup(html_example, 'html.parser')

print(soup.title)       # <title>태그 전체를 가져옴
print(soup.title.string)        # <title>태그의 텍스트만 리턴
print(soup.title.get_text())        # .string, .text(예전 버전)와 동일한 기능

print(soup.title.parent)        # 해당 태그를 포함하고 있는 부모(<head> 태그 출력)

print(soup.body)

print(soup.h1)      # 동일한 태그가 여러개 있는 경우, 첫 번째 요소를 추출
print(soup.h1.string)

print(soup.a)
print(soup.a.string)
print(soup.a['href'])
print(soup.a.get('href'))


print(soup.find('div',{'id':'text_id2'}))

div_text = soup.find('div',{'id':'text_id2'})
print(div_text.text)

href_link = soup.find('a', {'class':'internal_link'})   # 딕셔너리 형태
href_link = soup.find('a', class_ = 'internal_link')        # class_ 사용: class는 파이썬 예약어

print(href_link)
print(href_link['href'])
print(href_link.get('href'))
print(href_link.text)

# 내부의 모든 속성 가져오기 : attrs

print('href_link.attrs: ',href_link.attrs)      # <a>태그 내부의 모든 속성 출력
print('class 속성값: ', href_link['class'])        # class 속성의 value 출력

print('values():', href_link.attrs.values())        # 모든 속성들의 값 추ㄹ력

values = list(href_link.attrs.values())         # dictionary 값들을 리스트로 변경
print('values[0]: {0}, values[1]: {1}'.format(values[0],values[1]))


# href 속성의 값 검색
href_value = soup.find(attrs={'href': 'www.google.com'})    # 태그 생략 가능
href_value = soup.find('a', attrs={'href': 'www.google.com'})

print('href_value: ', href_value)
print(href_value['href'])   # 속성['href']의 값
print(href_value.string)


# span 태그의 속성 가져오기
span_tag = soup.find('span')

print('span_tag: ', span_tag)
print('attrs: ',span_tag.attrs)
print('value: ',span_tag.attrs['class'])
print('text', span_tag.string)


# 모든 div 태그를 검색 (리스트형태로 반환)
div_tags = soup.find_all('div')
print('div_tags length: ', len(div_tags))

for div in div_tags:
    print('-----------------------------------------------')
    print(div)

# 모든 <a> 태그 검색 및 속성 보기
links = soup.find_all('a')
print()
for alink in links:
    print(alink)
    print(f"url:{alink['href']}, text: {alink.string}")
    print()


# a태그에서 2개의 class 속성값 검색
link_tags = soup.find_all('a', {'class':['external_link', 'internal_link']})
print(link_tags)

p_tags = soup.find_all('p', {'id':['first','third']})
for p in p_tags:
    print(p)


# select() 함수 - find_all()과 유사
# select_one() 함수 = find()과 유사
# but, select_one()은 직접 하위경로지정
head = soup.select_one('head')
print(head)
print('head.text:', head.text.strip())

h1 = soup.select_one('h1')  # 첫 번째 <h1>태그 선택
print(h1)

# <h1>태그의 id검색 : 'footer'인 항목 추출
print()
footer = soup.select_one('h1#footer')
print(footer)

# 클래스 이름 검색: 태그.클래스 이름
class_link = soup.select_one('a.internal_link')
print(class_link)

print(class_link.string)
print(class_link['href'])


# 계층적 하위 태그 접근#1
# (상위태그> 하위태그) 형식으로 접근 : 태그가 단계적으로 존재할 때
link1 = soup.select_one('div#link > a.external_link')
print(link1)
# find()함수와 비교
link_find = soup.find('div', {'id':'link'})
external_link = link_find.find('a',{'class':'external_link'})   # 이미 find로 찾은 link_find에서 find()사용해야함
print('find external_link: ', external_link)

# 계층적 하위 태그 접근#2: 공백으로 하위 태그 선언
# (상위태그 하위태그) 형식으로 접근 : 자손 관계의 하위태그
link2 = soup.select_one('div#class1 p#second')
print(link2)
print(link2.string)


# select() - 모든 태그를 다 찾는 함수
# 모든 <h1> 태그 검색
h1_all = soup.select('h1')
print('h1_all', h1_all)
# 모든 url 링크 검색
url_links = soup.select('a')
for link in url_links:
    print(link['href'])

# <div id="class1"> 내부의 모든 url 검색
div_urls = soup.select('div#class1 > a')

print(div_urls)
print(div_urls[0]['href'])
# <div id="class1"> 내부의 모든 <a>태그는 자손 관계 - 공백으로 구분가능
div_urls2 = soup.select('div#class1 a')

print(div_urls2)


# 여러 항목 검색하기
# <h1>태그의 id가 'heading'과 'footer'를 모두 검색 : , 로 나열
h1 = soup.select('#heading, #footer')
print(h1)

# <a>태그의 class 이름이 'external_link'와 'internal_link' 모두 검색
url_links = soup.select('a.external_link, a.internal_link')
print(url_links)