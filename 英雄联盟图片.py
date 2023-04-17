import requests
import json
import csv
# 请求图片地址
# 请求地址
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?v=22'
# 请求头信息
header= {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}
# 使用requests请求
response = requests.get(url, headers=header)
res = response.text
# 使用json转换为字典类型
res = json.loads(res)
# print(type(res))
# 字典取值
hero = res['hero']
# 循环从列表中取出所有的英雄
with open('lianmeng.csv', 'a+', newline='') as f:
    for he in hero:
        heroId = he['heroId']
        name = he['name']
        alias = he['alias']
        li = [heroId, name, alias]
        write = csv.writer(f)
        # write.writerow(['id', 'name', 'enname'])
        write.writerow(li)
    # 需要把信息写入csv文件