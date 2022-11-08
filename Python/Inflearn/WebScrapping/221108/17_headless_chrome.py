from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.headless = True

# headless chrome은 정보가 날아갈 수도 있기 때문에 user agent를 설정해준다.
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")

# 백그라운드에서 창을 띄울 크기 정하기
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome("C:/vscode/chromedriver.exe", options=options)

# user agent 페이지 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
browser.get(url)
id= browser.find_element(By.ID,"detected_value")

browser.get_screenshot_as_file("user agent.png")
print(id.text)

    
    