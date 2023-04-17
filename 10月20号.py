# 导包
import requests
import json
import urllib.parse
# 请求地址
url = "https://weibo.com/ajax/side/hotSearch"
# 请求头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}
# 请求网页
response = requests.get(url, headers=headers)
info = response.text
print(info)
# 使用json模块 page为字典类型
page = json.loads(info)
# 字典取值
realtime = page['data']['realtime']
# 列表循环取值
for item in realtime:
    word = item['word']
    category = item['category']
    a = urllib.parse.quote(word)
    word_scheme = item['word_scheme']
    link = 'https://s.weibo.com/weibo?q={}&topic_ad='.format(a)
    print(link)

