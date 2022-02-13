# pip install openpyxl 로 라이브러리 설치
import openpyxl

#1) 엑셀파일 생성
wb = openpyxl.Workbook()

#2) worksheet 생성
ws = wb.create_sheet('좋아하는 여자')

#3) 데이터 추가하기

