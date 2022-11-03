# 404 뜨는 이유: 페이지에서 접속자를 판별 (데스크탑인지/ 모바일인지 등)
# 인간이 아니라고 판단 했을 때 접근을 차단할 수 있음

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers) # 현재는 오류 안뜸
res.raise_for_status()
with open("nadocoding.html",'w',encoding='utf-8') as f:
  f.write(res.text)

  # 오류가 뜬다고 가정
  # 나의 user agnet 확인 (크롬과 엣지로 접속 할 때 달라짐)
  # 복사. headers 추가