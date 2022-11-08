from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("C:/vscode/chromedriver.exe")
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/books"
browser.get(url)

# 모니터 높이 1080 위치로 스크롤 내리고 기다리기
browser.execute_script("window.scrollTo(0,1080)")
# 바탕화면에서 우클릭 디스플레이 설정에서 해상도 확인

# 좀더 밑으로내리기
browser.execute_script("window.scrollTo(0,2080)")

# 화면 가장 아래로 내리기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

# 2초에 한번씩 스크롤 내리기
import time 
interval=2

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복해주기
while True:
    # 스크롤 밑으로 내리기
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    # 로딩대기
    time.sleep(interval)
    
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    
    # 현재 높이와 이전 높이가 같다면(변화가 없다면) 탈출
    if curr_height == prev_height:
        break
    
    prev_height = curr_height
print("스크롤 완료")

# html 정보 가져오기
import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source,"html.parser")

books =soup.find_all("div", class_="Si6A0c ZD8Cqc")

for book in books:
    title = book.find("div", class_="Epkrse ").text
    print(title)