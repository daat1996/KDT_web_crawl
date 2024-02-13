import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BeautifulSoup(html, 'html.parser')
# 두 테이블 중 먼저 나온 테이블사용
table= bs.find_all('table',{'class': 'wikitable'})[0]
rows = table.find_all('tr')

csvFile = open('editors.csv', 'wt', encoding='utf-8')       # t: text mode
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.find_all(['th', 'td']):
            print(cell.text.strip())
            csvRow.append(cell.text.strip())
        writer.writerow(csvRow)
finally:
    csvFile.close()


