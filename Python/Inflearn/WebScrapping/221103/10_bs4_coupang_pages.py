
import requests
import re
from bs4 import BeautifulSoup

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36","Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}

# for i in range(1,6):
#     # 페이지에 i를 넣어줌
#     print("페이지 : ",i)
#     url ="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
#     res = requests.get(url, headers=header)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")


#     items = soup.find_all("li",class_=re.compile("^search-product"))

    # for item in items:
    #     icon = item.find("img",class_="badge-ico badge-coupick")
    #     if icon:
    #         print("<광고상품 제외합니다.>")
    #         continue

    #     name = item.find('div',class_="name").text 

    #     if "Apple" in name:
    #         print("<apple 상품 제외합니다.>")
    #         continue

    #     price = item.find("strong",class_="price-value") 
    #     if price:
    #         price = price.text
    #     else:
    #         price = "<가격 없음>"


    #     rate = item.find("em",class_="rating") 
    #     if rate:
    #         rate = rate.text

    #     else:
    #         rate = "<평점 없는 상품 제외합니다.>"
    #         continue

    #     rate_c = item.find("span",class_="rating-total-count") 
    #     if rate_c:
    #         rate_c = rate_c.text[1:-1]
        
    #     else:
    #         rate = "<평점 없는 상품 제외합니다.>"
    #         continue
        
    #     if float(rate)>4.5 and int(rate_c)>50: 
    #         print("제품명: ",str(name).strip())
    #         print("가격: ", price)
    #         print("평점: ", rate)
    #         print("평점 수: ", rate_c)

# 정리하고 링크 추가하기
for i in range(1,6):

    url ="https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
    res = requests.get(url, headers=header)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")


    items = soup.find_all("li",class_=re.compile("^search-product"))

    for item in items:
        icon = item.find("img",class_="badge-ico badge-coupick")
        if icon:
            continue

        name = item.find('div',class_="name").text 

        if "Apple" in name:
            continue

        price = item.find("strong",class_="price-value") 
        if price:
            price = price.text
        else:
            price = "<가격 없음>"

        rate = item.find("em",class_="rating") 
        if rate:
            rate = rate.text

        else:
            rate = "<평점 없는 상품 제외합니다.>"
            continue

        rate_c = item.find("span",class_="rating-total-count") 
        if rate_c:
            rate_c = rate_c.text[1:-1]
        
        else:
            rate = "<평점 없는 상품 제외합니다.>"
            continue
        link = item.find('a',class_="search-product-link")['href']
        # 앞부분이 잘림

        if float(rate)>4.5 and int(rate_c)>50: 
            print("제품명: ",str(name).strip())
            print("가격: ", price)
            print("평점: ", rate)
            print("평점 수: ", rate_c)
            print("링크: ", "https://www.coupang.com/"+link)
            print("-"*80) # 줄긋기
