from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv

# 브라우저 생성
browser = webdriver.Chrome(r'C:\chromedriver.exe')

# 웹사이트 열기
browser.get('https://www.naver.com')
browser.implicitly_wait(2) # 브라우저가 늦게 열릴 경우 클릭을 5초 기다렸다 하게 하는 명령어

# 쇼핑 메뉴 클릭
browser.find_element_by_css_selector('a.nav.shop').click()
time.sleep(2) #브라우저 열릴 떄 까지 기다림

# 검색창 클릭
search = browser.find_element_by_css_selector('input.co_srh_input._input')
search.click()

# 검색어 입력
search.send_keys('의자')
search.send_keys(Keys.ENTER)

#동적 HTML 을 다루기 위한 무한 스크롤 명령어

# javascript 명령어인 window.scrollY 를 입력 및 실행
# before_h 는 첫 스크롤 높이를 의미
before_h = browser.execute_script("return window.scrollY")

while True:
    # 맨 아래로 스크롤 내림 (html의 body마다 멈춤) 
    # css 선택자로 body 선택하고 키보드의 end 키 클릭
    browser.find_element_by_css_selector("body").send_keys(Keys.END)

    # 스크롤 사이 페이지 로딩 시간
    time.sleep(1)

    # 스크롤 후 높이
    after_h = browser.execute_script("return window.scrollY")

    if after_h == before_h:
        break

    before_h = after_h


with open(r"C:\Users\crosstar\OneDrive - 고려대학교\Desktop\practice_crosstar\practice-crawling\selenium_shopping_crawling\data.csv", 'w', encoding='CP949', newline='') as f:
    csvWriter = csv.writer(f)

    items = browser.find_elements_by_css_selector("div.basicList_info_area__17Xyo")

    for item in items:
        # class = basicList_link__1MaTN
        name = item.find_element_by_css_selector(".basicList_link__1MaTN").text
        #class = price_num__2WUXn
        try:
            price = item.find_element_by_css_selector(".price_num__2WUXn").text
        except:
            "판매 중단"
        # price = item.find_element_by_css_selector(".basicList_price_area__1UXXR")
        # 태그에 해당하는 정보가 어떤 식으로 나와있는지에 유의!
        link = item.find_element_by_css_selector(".basicList_link__1MaTN").get_attribute("href")

        print(name, price, link)
        csvWriter.writerow([name, price, link])
