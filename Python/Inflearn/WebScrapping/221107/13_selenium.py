
from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')

# 1. 네이버로 가기
driver.get("https://www.naver.com/")

# 2. 로그인 버튼 클릭
elem = driver.find_element(By.CLASS_NAME,"link_login")
elem.click()

# 3. id와 pw 입력
driver.find_element(By.ID,"id").send_keys("first_id")
driver.find_element(By.ID,"pw").send_keys("wrong_password")

# 4. 로그인 버튼 클릭
driver.find_element(By.CLASS_NAME,"btn_login").click()

# 5. id를 새로 입력
driver.find_element(By.ID,"id").send_keys("second_id")
# first_id 뒤에 새 아이디가 붙여서 입력됨.
# 지우고 입력해보자
driver.find_element(By.ID,"id").clear()
driver.find_element(By.ID,"id").send_keys("second_id")

# 6. html 정보 출력
print(driver.page_source)

# 7. 브라우저 종료
driver.quit()
# delay 넣기
import time
time.sleep(1)



