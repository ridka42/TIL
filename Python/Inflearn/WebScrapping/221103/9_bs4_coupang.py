# 페이지1에서 2로 넘어가는 순간 주소가 복잡해짐
# html method : 서버에 요청하면 응답을 해주는데 요청에 포함되는 것 중 하나
# get 방식 : 어떤 내용을 누구나 볼 수 있게 url에 담겨줌
# https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%E
# B%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&
# sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&
# listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&
# rating=0&page=5&rocketAll=false&searchIndexingToken=1=6&backgroundColor=
# 속성=값& 으로 여러개가 들어갈 수 있다. -> 값들을 원하는대로 변경하면서 페이지 요청
# 한번 전송할 때 보낼 수 있는 데이터 양에 제한이 있다.

# post 방식 : url이 아닌 html 메시지 바디에 숨겨서 보내줌
# 아이디나 비밀번호 등은 숨겨서 보내줌. get에 비해서는 안전
# 크기 제한이 없다. 게시판 글이나 파일 업로드 등 개인정보들은 post 방식
# 
# 쿠팡은 get 방식
# 
import requests
import re
from bs4 import BeautifulSoup

url ="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=6&backgroundColor="
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url, headers=header)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")


# items = soup.find_all("li",class_=re.compile("^search-product"))
# # li 태그 중 class 이름이 search-product 로 시작하는 모든 것(광고제품 포함)
# print(items[0].find('div',class_="name").text)
# 에러!! 

# user agent로 사람이 하는거처럼 변경해준다. headers 추가.

items = soup.find_all("li",class_=re.compile("^search-product"))
# li 태그 중 class 이름이 search-product 로 시작하는 모든 것(광고제품 포함)
# print(items[0].find('div',class_="name").text)

# for item in items:
#     name = item.find('div',class_="name").text # 제품명
#     price = item.find("strong",class_="price-value").text # 가격
#     rate = item.find("em",class_="rating") # 평점
#     rate_c = item.find("span",class_="rating-total-count").text # 평점 수
#     print(name,price,rate,rate_c)

# # 평점이 없는 상품 때문에 rate와 rate_c에 값이 없는 오류가 생김.
# 평점 없는 경우를 만들어준다.
# for item in items:
#     name = item.find('div',class_="name").text # 제품명
#     price = item.find("strong",class_="price-value").text # 가격


#     rate = item.find("em",class_="rating") # 평점
#     if rate:
#         rate = rate.text
#     else:
#         rate = "평점 없음"

#     rate_c = item.find("span",class_="rating-total-count") # 평점 수
#     if rate_c:
#         rate_c = rate_c.text
#     else:
#         rate_c = "평점 없음"
#     print(name,price,rate,rate_c)


# 광고가 붙은 제품은 제외한다.

# for item in items:
#     icon = item.find("img",class_="badge-ico badge-coupick")
#     if icon:
#         print("<광고상품 제외합니다.>")
#         continue

#     name = item.find('div',class_="name").text # 제품명

#     price = item.find("strong",class_="price-value") # 가격
#     if price:
#         price = price.text
#     else:
#         price = "<가격 없음>"

#     rate = item.find("em",class_="rating") # 평점
#     if rate:
#         rate = rate.text
#     else:
#         rate = "<평점 없음>"

#     rate_c = item.find("span",class_="rating-total-count") # 평점 수
#     if rate_c:
#         rate_c = rate_c.text
#     else:
#         rate_c = "<평점 수 없음>"

#     print(name,price,rate,rate_c)

# 평점이 4.5이상, 리뷰가 100개 이상인 제품만.
# for item in items:
#     icon = item.find("img",class_="badge-ico badge-coupick")
#     if icon:
#         print("<광고상품 제외합니다.>")
#         continue

#     name = item.find('div',class_="name").text # 제품명
#     price = item.find("strong",class_="price-value") # 가격
#     if price:
#         price = price.text
#     else:
#         price = "<가격 없음>"

#     rate = item.find("em",class_="rating") # 평점
#     if rate:
#         rate = rate.text

#     else:
#         rate = "<평점 없는 상품 제외합니다.>"
#         continue

#     rate_c = item.find("span",class_="rating-total-count") # 평점 수
#     if rate_c:
#         rate_c = rate_c.text
#         rate_c =rate_c[1:-1] # rate_c에는 괄호가 있음
#     else:
#         rate = "<평점 없는 상품 제외합니다.>"
#         continue
    
#     if float(rate)>4.5 and int(rate_c)>50: 
#         print(name,price,rate,rate_c)

# 맥북은 제외하고 싶다.
# 이름에서 apple이 들어가면 제외해준다.
for item in items:
    icon = item.find("img",class_="badge-ico badge-coupick")
    if icon:
        print("<광고상품 제외합니다.>")
        continue

    name = item.find('div',class_="name").text # 제품명

    if "Apple" in name:
        print("<apple 상품 제외합니다.>")
        continue

    price = item.find("strong",class_="price-value") # 가격
    if price:
        price = price.text
    else:
        price = "<가격 없음>"


    rate = item.find("em",class_="rating") # 평점
    if rate:
        rate = rate.text

    else:
        rate = "<평점 없는 상품 제외합니다.>"
        continue

    rate_c = item.find("span",class_="rating-total-count") # 평점 수
    if rate_c:
        rate_c = rate_c.text
        rate_c =rate_c[1:-1] # rate_c에는 괄호가 있음
    else:
        rate = "<평점 없는 상품 제외합니다.>"
        continue
    
    if float(rate)>4.5 and int(rate_c)>50: 
        print("제품명: ",str(name).strip())
        print("가격: ", price)
        print("평점: ", rate)
        print("평점 수: ", rate_c)