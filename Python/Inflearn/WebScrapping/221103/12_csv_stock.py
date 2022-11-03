import csv # csv 파일로 저장하려고
import requests
from bs4 import BeautifulSoup

url ="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=" # 뒤에 페이지 추가

# 1~50
# for p in range(1,2):
#     res = requests.get(url + str(p))
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text,"lxml")

#     data_rows = soup.find("table",class_='type_2').find("tbody").find_all("tr")
#     # 종목들

#     for row in data_rows:
#         columns = row.find_all("td") # 종목별 현재가 전일비 등락율 등 정보 들
#         data = [column.get_text() for column in columns]
#         print(data)
#     # 공백과 줄바꿈이 많다.

# # csv 파일에 저장하기

# filename = "시가총액 1-200.csv"
# f= open(filename, "w", encoding="utf-8-sig", newline="")
# # newline="" 안하면 종목 하나 사이에 빈줄이 생김
# # 엑셀에서 한글깨지면 utf-8-sig 로 인코딩
# writer = csv.writer(f)

# for p in range(1,2):
#     res = requests.get(url + str(p))
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text,"lxml")

#     data_rows = soup.find("table",class_='type_2').find("tbody").find_all("tr")

#     for row in data_rows:
#         columns = row.find_all("td") 
#         if len(columns) <= 1: # 의미없는 data skip
#             continue
#         data = [column.get_text().strip() for column in columns]#공백제거
#         print(data)
#         writer.writerow(data)
#         # data는 list 형식 한줄씩 들어간다.

# 컬럼명 입력하기
filename = "시가총액 1-200.csv"
f= open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# tab으로 구분된 data가 리스트로 title에 들어감
writer.writerow(title)
# list 형태로 입력해야함.


for p in range(1,2):
    res = requests.get(url + str(p))
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")

    data_rows = soup.find("table",class_='type_2').find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td") 
        if len(columns) <= 1: # 의미없는 data skip
            continue
        data = [column.get_text().strip() for column in columns]#공백제거
        print(data)
        writer.writerow(data)
        # data는 list 형식 한줄씩 들어간다.