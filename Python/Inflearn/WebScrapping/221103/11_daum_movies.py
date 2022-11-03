# url 에서 연도만 바꿔주면 될 것 같다!
# 이미지를 다운 받으려면?

import requests
from bs4 import BeautifulSoup

# res = requests.get("https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=2018%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84")
# res.raise_for_status()

# soup = BeautifulSoup(res.text,"lxml")

# images = soup.find_all("img",class_="thumb_img")

# for image in images:
#     print(image['src'])
# 앞에 http가 없는 경우

# for image in images:
#     img_url = image['src']
#     if img_url.startswith("//"):
#         img_url ="https:"+ img_url
#     print(img_url)

# 사진 다운받기
# for i, image in enumerate(images):
#     img_url = image['src']
#     if img_url.startswith("//"):
#         img_url ="https:"+ img_url
#     print(img_url)

#     img_res = requests.get(img_url)
#     img_res.raise_for_status()

#     # 파일 이름은 movie1, movie2,,,
#     # 이미지는 바이너리
#     with open("movie{}.jpg".format(i+1),"wb") as f:
#         f.write(img_res.content)
#         정보의 컨텐트를 쓴다.
#     1~30위까지의 사진을 모두 가져왔다.

# 5위 까지만 가져오기. 
# for i, image in enumerate(images):
#     img_url = image['src']
#     if img_url.startswith("//"):
#         img_url ="https:"+ img_url
#     print(img_url)

#     img_res = requests.get(img_url)
#     img_res.raise_for_status()

#     # 파일 이름은 movie1, movie2,,,
#     # 이미지는 바이너리
#     with open("movie{}.jpg".format(i+1),"wb") as f:
#         f.write(img_res.content)
#     # 상위 5개만
#     if i >= 4:
#         break

# 최근 5년간의 상위 5개가져오기.
for year in range(2017,2022):
    url= "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text,"lxml")

    images = soup.find_all("img",class_="thumb_img")

    for i, image in enumerate(images):
        img_url = image['src']
        if img_url.startswith("//"):
            img_url ="https:"+ img_url
        print(img_url)

        img_res = requests.get(img_url)
        img_res.raise_for_status()

    # 파일 이름을 변경(연도가 돌아갈때마다 인덱스가 겹쳐서 덮어쓰기 되기때문)
        with open("movie_{}_{}.jpg".format(year,i+1),"wb") as f:
            f.write(img_res.content)

        if i >= 4:
            break
