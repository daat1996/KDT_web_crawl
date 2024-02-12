import pandas as pd


DP = pd.read_csv('hollys_branches.csv', encoding='utf-8-sig')
# print(DP)

# print(DP['주소'].info())

# city = '대구 북구'
while True:
    city = input('검색할 매장의 도시를 입력하세요: ')
    if city == 'quit':
        print('종료 합니다.')
        break
    print('-'*20)
    i = 0
    test1 = DP['위치(시,구)'].str.contains(city)
    print(f'검색된 매장 수: {sum(test1)}')
    print('-'*20)
    j = 1
    for address in DP['위치(시,구)'].tolist():       # series를 리스트 형태로
        if city in address:
            print(f'[{j:3}]:{DP.iloc[i].tolist()[2:4]}')
            j += 1
        i += 1
    print('-' * 20)

