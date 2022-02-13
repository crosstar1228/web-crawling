# 검색하기

import requests
from bs4 import BeautifulSoup

resp = requests.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%BD%94%EB%A1%9C%EB%82%98")
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


