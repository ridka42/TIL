import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793" 
# 네이버 웹툰에 가우스 전자를 검색

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 가우스 전자의 모든 회차 제목 가져오기
cartoons = soup.find_all('td', class_="title")
title = cartoons[0].a.get_text()
print(title)
# # 0번 인덱스 td 태그 안의 a 태그 안의 텍스
# 링크도 함께 가져오기
link = cartoons[0].a["href"]
print(link)
# /webtoon/detail?titleId=799793&no=50&weekday=mon 앞에가 잘림
print("https://comic.naver.com"+link)
# 모든 회차에 적용하기
for cartoon in cartoons:
  title = cartoon.a.text
  link = "https://comic.naver.com" + cartoon.a['href']
  print(title, link, sep="   ", end="\n")

# 평점 구하기
cartoons = soup.find_all('div', class_="rating_type")
for cartoon in cartoons:
  rate = cartoon.find("strong").get_text() # cartoon의 strong 요소 의 텍스트
  print(rate)

# 평점의 평균
total_rates = 0
cartoons = soup.find_all('div', class_="rating_type")
for cartoon in cartoons:
  rate = cartoon.find("strong").get_text() # cartoon의 strong 요소 의 텍스트
  total_rates += float(rate)
print("전체 점수: ", round(total_rates,2))
print("평균 점수: ", round(total_rates/len(cartoons),3))

# 인터프리터 방식(한줄씩 바로실행-동시통역) / 컴파일 방식(컴터언어로 번역해서 실행-번역본)