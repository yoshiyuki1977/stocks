import requests
from bs4 import BeautifulSoup
from slacker import Slacker
import json
import csv
import datetime


res = requests.get("https://info.finance.yahoo.co.jp/ranking/?kd=33&mk=1&tm=d&vl=a")
soup = BeautifulSoup(res.text, 'lxml')

#h2s = soup.find_all("h2")

table = soup.find_all("table", {"class":"rankingTable"})[0]
rows = table.find_all("tr")

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

slack.files.upload(f_name, filename="出来高ランキング", filetype="csv", channels="#stock-volume")
