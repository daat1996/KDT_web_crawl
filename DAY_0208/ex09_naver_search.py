from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

query = 'ChatGPT'
url = f'https://search.naver.com/search.naver?where=view&sm=tab_jum&query={query}'

# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

blog_results = soup.select('a.title_link')

for blog_title in blog_results:
    title = blog_title.text
    link = blog_title['href']
    print(f'{title}, [{link}]')