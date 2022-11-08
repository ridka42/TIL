import requests
from bs4 import BeautifulSoup as bs

url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status() # 에러 체크
soup = bs(res.text,'html.parser')

titles = soup.find_all("dt",class_="tit_base")
# for title in titles:
#     print(title.text)
    
address_t = titles[0].text
num_t = titles[1].text
size_t = titles[2].text
envir_t = titles[3].text
convi_t = titles[4].text

address = soup.find("div",class_="address_type").text
num = soup.find("dd",class_="cont").text
size = soup.find("span",class_="f_l").text

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome("C:/vscode/chromedriver.exe")
url = "https://search.daum.net/search?w=tot&DA=UME&t__nil_searchbox=suggest&sug=&sugo=15&sq=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4&o=1&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
browser.get(url)
browser.maximize_window()


envirs = browser.find_element(By.XPATH,'//*[@id="estateColl"]/div[2]/div/div[2]/div[2]/dl[4]')
envirs = envirs.find_elements(By.TAG_NAME,"a")
envir = []
for e in envirs:
    envir.append(e.text)

convis = browser.find_element(By.XPATH,'//*[@id="estateColl"]/div[2]/div/div[2]/div[2]/dl[5]/dd')
convis = convis.find_elements(By.TAG_NAME,"a")
convi = []
for c in convis:
    convi.append(c.text)

print(f"{address_t} : {address}")
print(f"{num_t} : {num}")
print(f"{size_t} : {size}")
print(f"{envir_t} : {envir}")
print(f"{convi_t} : {convi}")