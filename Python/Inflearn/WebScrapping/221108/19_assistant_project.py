import requests
from bs4 import BeautifulSoup as bs

# 날씨 가져오기
def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_jum&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    res = requests.get(url)
    res.raise_for_status() # 에러 체크
    soup = bs(res.text,'html.parser')
    
    # 현재 온도
    curr_tems = soup.find("div",class_="temperature_text").find_all("strong")
    curr_tem=[]
    for c in curr_tems:
        curr_tem.append(c.text)
    curr_tem= curr_tem[0]

    # 날씨 설명
    curr_info = soup.find("p", class_="summary").text
    curr_info = curr_info.split("  ")[1].strip()+", "+curr_info.split("  ")[0]

    # 미세먼지
    dust1= soup.find("ul","today_chart_list").find_all("span","txt")[0].text
    # 초미세먼지
    dust2= soup.find("ul","today_chart_list").find_all("span","txt")[1].text

    # 최저 기온
    low_tem = soup.find("span","lowest").text
    # 최고 기온
    high_tem = soup.find("span","highest").text

    # 오전 강수확률
    morning_rain = soup.find_all("span","rainfall")[0].text
    # 오후 강수확률
    afternoon_rain = soup.find_all("span","rainfall")[1].text

    print(curr_tem, f"({low_tem} / {high_tem})")
    print(curr_info)
    print(f"미세먼지 {dust1}")
    print(f"초미세먼지 {dust2}")
    print(f"오전 강수확률 {morning_rain} / 오후 강수확률 {afternoon_rain}")
    print("\n")
    
    
    
# 언론사별 뉴스 가져오기
def news():
    print("[언론사별 뉴스]")
    url = "https://news.naver.com/?viewType=pc"
    res = requests.get(url)
    res.raise_for_status() # 에러 체크
    soup = bs(res.text,'html.parser')
    
    news_list=soup.find_all("a","cjs_news_a _cds_link _editn_link",limit=3) # 3개만
    
    for i,news in enumerate(news_list):
        # 뉴스 기사 제목
        title = news.find("div","cjs_t").text.strip()
        # 링크
        link = news['href']
        print(f"{i+1}. {title}\n(링크 : {link})")
    print("\n")


# IT 뉴스 가져오기
def IT_news():
    print("[IT 뉴스]")
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
    
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = bs(res.text,'html.parser')

    news_list = soup.find("ul","type06_headline").find_all("li",limit=3) # 3개만
    for i,news in enumerate(news_list):
        idx=0
        # img 태그가 있는지 확인
        img = news.find("img")
        # 있으면 인덱스는 1
        if img:
            idx=1
            
        #  뉴스 제목
        title = news.find_all("a")[idx].text.strip()
        # 뉴스 링크
        link = news.find_all("a")[idx]['href']
        # 뉴스 설명
        info = news.find("span","lede").text
        print(f"{i+1}. {title}\n {info}\n(링크 : {link})")

    
        
if __name__ == "__main__":
    scrape_weather() # 오늘의 날씨 정보 가져오기
    news() # 언론별 뉴스
    IT_news() # 아이티 뉴스
    # 직접 실행 할땐 함수 실행 
    # 호출 실행할 땐 실행 안됨
    
