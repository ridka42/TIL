import requests
res = requests.get("http://naver.com") # link에 접속해서 html정보를 가져온다.
print("응답코드 : ", res.status_code) # 200 이면 정상

res = requests.get("http://nadocodding.tistory.com")
print("응답코드 : ", res.status_code) # 404 접근 권한 없음-> 이 방법으론 스크래핑 불가능

if res.status_code == requests.codes.ok:
  print("정상입니다.")
else:
  print("문제가 생겼습니다. [에러코드", res.status_code,"]")

res.raise_for_status() # 정상이면 그냥 진행 아니면 오류 생성
print("웹 스크래핑을 진행합니다.")

res = requests.get("http://google.com")
res.raise_for_status() 
# 보통 이렇게 두 줄 사용

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf-8") as f:
  f.write(res.text) # my google파일을 열어보면 구글페이지가 뜬다.(스타일은 다름)