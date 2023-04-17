import requests
from lxml import html
url = 'https://ke.qq.com/course/list'
start_url ='https://ke.qq.com/course/list'

header = {
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 请求地址
response = requests.get(start_url,headers = header)
# 指定相应编码格式
response.encoding ='utf-8'
# 建立文档数对象
page = html.etree.HTML(response.text)
# 使用xpath进行解析.
div_qz = page.xpath('//div[@class="course-list"]/div')
for item in div_qz:
    name = item.xpath('.//@class="kc-course-card-name"]/@title')
    link = item.xpath('.//a[@class="kc-course-card js-report-link kc-list-course-card kc-course-card-column"]/@href')
    if len(name) > 0:
        name = name[0]
    else:
        name = ''
    if len(link) > 0:
        link = start_url + link[0]
    else:
        link = ''
    print(name,link)
# 将数据插入mysql
