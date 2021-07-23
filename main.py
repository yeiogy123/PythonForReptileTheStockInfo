# coding=utf-8
import json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
def main():
    start_date = input("請輸入起始日期(ex:2021年7月20日)")
    end_date = input("請輸入結束日期(ex:2021年/7月/21日)")
    r = Request("https://cn.investing.com/equities/apple-computer-inc-historical-data", headers={"User-Agent": "Mozilla/5.0"})
    c = urlopen(r).read()
    soup = BeautifulSoup(c, "html.parser")
    name = soup.findAll("div", {"id": "results_box"})[0].findAll('thead')
    result = soup.findAll("div", {"id": "results_box"})[0].findAll('tbody')
    status = name[0].findAll("tr")
    row = result[0].findAll("tr")
    table_label = status[0].findAll("th")
    start_bug = False
    for i in range(0, len(row)):
        output_status = True
        table_data = []
        table_head = row[i].findAll("td")
        stop = False
        for j in range(0, len(table_head)):
            if table_head[j].text == end_date:
                start_bug = True
            if start_bug:
                table_data.append(table_label[j].text)
                table_data.append(table_head[j].text)
                json_output = json.dumps(table_data, ensure_ascii=False)
            if table_head[j].text == start_date:
                stop = True
        print(json_output)
        if not start_bug:
            output_status = False
        if not output_status:
            break
main()