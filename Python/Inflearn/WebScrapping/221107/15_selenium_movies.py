import requests
from bs4 import BeautifulSoup as bs

url = "https://play.google.com/store/books?hl=ko&gl=US"
res = requests.get(url)
res.raise_for_status() # 에러 체크
soup = bs(res.text)