import csv
import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup


#URLの指定
html = urlopen("https://info.finance.yahoo.co.jp/ranking/?kd=33&mk=1&tm=d&vl=a")
bsObj = BeautifulSoup(html, "html.parser")

#テーブルを指定
table = bsObj.findAll("table",{"class":"rankingTable"})[0]
rows = table.findAll("tr")

now = datetime.datetime.now()
#先に年月日を付けたファイルを生成
f_name = "volume_{0:%Y%m%d%H%M%S}.csv".format(now)
#作成したcsvファイルを開いて、書き込む
csvFile = open(f_name, 'wt', newline = '', encoding = 'utf-8')
writer = csv.writer(csvFile)

try:
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td' , 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvFile.close()
