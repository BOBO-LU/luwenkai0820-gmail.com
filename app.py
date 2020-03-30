"""
只能抓取列表，還無法抓取每項資料的詳細資訊
折扣只有降價，沒有紀錄其他優惠
"""


import csv
import re #regular expresion

from urllib.request import urlopen
from bs4 import BeautifulSoup

weburl = "http://www.coolpc.com.tw/evaluate.php" #放網址的地方 如果是檔案就這樣寫"file:web.html"
bsObj = BeautifulSoup(urlopen(weburl), "html5lib")

pattern = '↪' #用來過濾網頁中的子項目

for cells in bsObj.find("tbody", {"id": "tbdy"}).findAll("td"):

	if ((len(cells.text) == 1 or len(cells.text) == 2 )and (cells.text != "\n") and (cells.text != "\n\n") ):#換csv檔案
		out = cells.text.split() #用split來刪掉特殊空白字元 EX:\xa0、\t、\n，只會剩下數字

		if ( len(out) >= 1): #只有1到30個項目，用來過濾空cells(被前一行刪掉了)
			filename = "weboutput"+cells.text+".csv"
			f = open(filename, "w", encoding = 'utf-8-sig', newline = "")
			print("輸出:"+filename)#印出檔案名字，之後要放到第一層for裡面

	for item in cells.findAll("option"):
		print(item.text)
		check = re.findall(pattern, item.text)

		if ( check == ['↪' ]): #移除換行字符
			continue
		elif ( item.text == ""): #移除空行
			continue
		else: 
			final = item.text.split(",")
			if ( len(final) == 2 ): #指輸入有物品和價格，要最後在處理
				final[1] = re.sub("^\$.*↘$|熱賣|◆|★|↓.*↓|[ ]|(\$.*↘)|\s|\W|[\u4E00-\u9FFF]|[\uFF41-\uFF5A]|[\uFF21-\uFF3A]|[^0-9]", "", final[1])
				if ( final[1] != ""):#地二格有東西在輸入
					csv.writer(f, delimiter =',').writerow(final)
					
f.close()
