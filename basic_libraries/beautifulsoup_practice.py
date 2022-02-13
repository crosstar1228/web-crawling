import requests
from bs4 import BeautifulSoup

# 요청을 통해 response 받음
response = requests.get("https://www.naver.com/")
# naver에서 html 줌
html = response.text
# 수프 완성!
soup = BeautifulSoup(html, 'html.parser') # html, parser

# 수프로부터 하나 골라서
word = soup.select_one('#NM_set_home_btn') # '네이버를 시작페이지로' 내용의 id를 입력하였음 +(#은 CSS 입력자)
# 텍스트로 출력
print(word.text)


