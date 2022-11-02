import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday" # 네이버 요일별 웹툰 페이지
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# 네이버 웹툰 전체 목록 가져오기
cartoons = soup.find_all('a', class_='title')
# findall : class 속성인 title인 모든 a태그
# find : class 속성인 title인 첫 번째 a태그
# class_='title' : attr={"class":"title"}과 같은 기능

for cartoon in cartoons:
  print(cartoon.get_text())

