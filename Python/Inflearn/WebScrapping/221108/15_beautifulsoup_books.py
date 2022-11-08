import requests
from bs4 import BeautifulSoup as bs

url = "https://play.google.com/store/books"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    ,"Accept-Language":"ko-KR,ko" #한글 페이지 달라
    }
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러 체크
soup = bs(res.text,'html.parser')

books = soup.find_all("div",class_="ULeU3b neq64b")
print(len(books))
# 0이 뜸 

with open("books.html",'w',encoding="utf8") as f:
    # f.write(res.text) # 보기 너무 힘들다.
    f.write(soup.prettify()) # 좀더 정돈된 형태
    # 파일에서 책 이름을 검색 해도 안뜬다.
    # 브라우저로 열어보면?
    # 검색해서 들어간 창과 약간 다르다. (접속하는 사람의 HEADERs 정보에 따라 다르게 뜨는데 이 창이 디폴트)
    # 헤더를 추가해주자.
    
# 제목만 출력해보자.
for book in books:
    title = book.find("div", attrs={"class":"Epkrse tAO7hf "}).get_text()
