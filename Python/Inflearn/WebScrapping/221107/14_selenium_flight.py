from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')

driver.maximize_window() # 창 최대화

url ="https://flight.naver.com/"
driver.get(url) # url로 이동

# 가는 날 클릭
driver.find_element(By.CLASS_NAME,"tabContent_option__2y4c6.select_Date__1aF7Y").click()


# link text는 a태그에서 가능한듯.

# 일 별로 모두 같은 태그기 때문에 순서로 가져와야함.
# 이번달
driver.find_elements(By.CLASS_NAME,"sc-evZas.dDVwEk.num")[10].click()
driver.find_elements(By.CLASS_NAME,"sc-evZas.dDVwEk.num")[15].click()

# 다음달도 모두 같다. Xpath로 찾아보자.
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[1]/td[5]/button/b').click()
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[9]/div[2]/div[1]/div[2]/div/div[4]/table/tbody/tr[2]/td[5]/button/b').click()

# 제주도 선택하기
# 출발지와 도착지 선택 버튼 클래스 이름이 같다. xpath사용
driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b').click()
driver.find_element(By.CLASS_NAME,"autocomplete_input__1vVkF").send_keys("제주")
driver.find_element(By.CLASS_NAME,"autocomplete_search_item__2WRSw").click()

# 항공권 검색 클릭
driver.find_element(By.CLASS_NAME,"searchBox_search__2KFn3").click()

# 첫 번째 항공권 결과 출력
elem = driver.find_element(By.CLASS_NAME,"domestic_select_schedule__xWQ-K").text
# 못찾는다.

elems = driver.find_elements(By.CLASS_NAME,"domestic_Flight__sK0eA.result")
elems[0].text

# 로딩 기다려주기
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 첫 번째 항공권 정보 엘레먼트가 나올 때 까지 10초 기다리기
# 오류나면 창닫기 안나도 닫기.
# 오류 났을 때만 닫으려면 except:
try:
    elem = WebDriverWait(driver,10).until(ec.presence_of_element_located(By.XPATH,'//*[@id="__next"]/div/div[1]/div[5]/div/div[2]/div[2]/div/button'))
    print(elem.text)
finally:
    driver.quit()