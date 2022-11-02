import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# url의 html 문서를 lxml 파서를 통해 정보를 가져옴

# print(soup.title)
# # title 태그 정보를 가져옴
# print(soup.title.text)
# # title 태그의 텍스트만 가져옴
# print(soup.a)
# # 첫번째 a태그 정보를 가져옴
# print(soup.a.attrs)
# # a 태그의 속성과 속성값들을 가져옴
# print(soup.a["href"])
# # a 태그의 특정 속성의 속성값을 가져옴

# # 대상 페이지에 관해 잘 모를 때는?
# # 특정 요소를 가져오고 싶을 때
# soup.find("a")
# # soup에서 첫 번째 a태그
# print(soup.find("a",attrs={"class":"Nbtn_upload"}))
# # 클래스이름이 Nbtn_upload인 a태그의 정보를 가져옴
# print(soup.find(attrs={"class":"Nbtn_upload"}))
# # 클래스이름이 Nbtn_upload인 태그의 정보를 가져옴
# # 현재는 웹툰 올리기가 하나기 때문에 하나만 뜸. 태그 종류를 안적어줘도됨.


# # 인기급상승 웹툰 1위부터 10위까지 가져오기
# rank1 = soup.find("li",attrs={"class":"rank01"})
# print(rank1.a)
# # soup.a 와 같은 원리.
# # li 요소 안의 a태그를 찾는 것
# print(rank1.a.text)

# rank1 값에서 rank2로 넘어가기 (형제요소)
rank1 = soup.find("li",attrs={"class":"rank01"})
print(rank1.a.get_text())
print(rank1.next_sibling) # 개행문자 때문에 한칸은 공백일 수 있다.
print(rank1.next_sibling.next_sibling) # rank1의 다음 다음 형제 요소
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.get_text())
rank2 = rank3.previous_sibling.previous_sibling  # rank3의 이전 이전 형제요소
print(rank2.get_text())

# rank1의 부모요소로 넘어가기
print(rank1.parent) # ol 태그 1부터10위 까지 전부 가져옴

# 개행문자가 있을 수 도 있고 없을 수 도 있기 때문에 애매하다.
rank2 = rank1.find_next_sibling("li")
# rank1 기준 다음 형제요소 중 li태그만 찾기
print(rank2.get_text())

rank3 = rank2.find_next_sibling("li")
# rank2 기준 다음 형제요소 중 li태그만 찾기
print(rank3.get_text())

rank2 = rank3.find_previous_sibling("li")
# rank3 기준 이전 형제요소 중 li태그만 찾기
print(rank2.get_text())


# 한번에 다른 형제요소들을 모두 가져오고 싶을 때
print(rank1.find_next_siblings("li"))
# rank1 기준 다음 형제요소 중 li 태그 모두 가져오기
# rank1은 포함 안됨

# a태그중 text가 비즈니스 여친-36화 인 a 태그 찾기
webtoon = soup.find('a', text="비즈니스 여친-36화")
print(webtoon)
# text는 여는 태그와 닫는 태그 사이의 텍스트