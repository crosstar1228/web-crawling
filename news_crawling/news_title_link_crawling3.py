# 여러 페이지 크롤링하기
from ast import keyword
import requests
from bs4 import BeautifulSoup
import pyautogui

# keyword = input("검색어 입력 고고!>>>") #input
keyword = pyautogui.prompt("검색어 입력 고고!>>>")
def search_with_pages(n):
    for m, i in enumerate(range(1,n*10,10)):
        print(f"{m+1}번 페이지 결과입니다.---------------------------------------")
        resp = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_pge&query={keyword}&start={i}") # keyword를 input으로 받음
    

        html = resp.text
        # print(html)

        soup = BeautifulSoup(html,"html.parser")
        # 선택자에 해당하는 모든 것들을 link로 담아온다!
        links = soup.select('.news_tit')
        # print(links) #list 형태로 담겨져 있음
        for link in links: #각 link는 <a>내용 </a> 의 html
            title = link.text # 태그 안에 텍스트요소 가져온다! -> 제목
            url = link.attrs['href'] # href=""의 속성값을 가져온다. -> 링크
            print(title, url) # 제목, 링크 크롤링 완료!


if __name__=="__main__":
    search_with_pages(3)