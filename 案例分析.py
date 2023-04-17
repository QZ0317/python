# 搜索打开网页端微博，获取微博热搜(名字等信息)
# 联系目的
# 1.使用requests库或者selenuim库请求网页信息
# 2.根据返回内容选择恰当的数据解析方法解析数据
# 3.将数据春初到mongodb数据库

# 导包
import requests
import json
import urllib.parse
# 请求地址
url = ''
# 请求头
headers = {

}