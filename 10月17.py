import requests
from lxml import html
import pymysql

url = 'https://ke.qq.com/course/list?mt=1001&st=2064'
header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

}
response = requests.get(url, headers=header)
response.encoding = 'utf-8'

page = html.etree.HTML(response.text)
b = page.xpath('//div[@class="course-list"]//a')

conn = pymysql.connect(host='localhost', user='root', password="123456", database='jd', port=3306)
cursor = conn.cursor()
dict1 = {}

for q in b:
    wz = q.xpath('.//div/h3/@title')
    lj = q.xpath('.//@href')
    lja = "https://ke.qq.com" + lj[0]

    dict1["a1"] = wz[0]
    dict1["a2"] = lja
    print(dict1)
    data = {k: "'" + v + "'" for k, v in dict1.items()}
    aa = f'INSERT INTO kecheng(name1, res1) VALUES ({(dict1["a1"])}, {(dict1["a2"])})'
    cursor.execute(aa)
    conn.commit()





# lj = page.xpath('//div[@class="course-list"]//a/@href')  # 链接
# wz = page.xpath('//div[@class="course-list"]//a/div/h3/@title')  # 文字信息
# lj1 = []
# for i in lj:
#     a = "https://ke.qq.com" + i
#     lj1.append(a)
#
#
# print(lj1, wz)
#
