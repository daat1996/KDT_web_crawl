# 헤더 저장

# csv file.writerow

import csv
csvFile = open('test.csv','w',encoding='UTF-8')     # 쓰고
try:
    writer = csv.writer(csvFile)
    writer.writerow(('number', 'number+2', '(number+2)^2'))     # 헤더정보 저장

    for i in range(10):
        writer.writerow((i, i+2, pow(i+2,2)))
except Exception as e:
    print(e)
finally:
    csvFile.close()