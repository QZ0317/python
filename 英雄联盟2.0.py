import requests
import json
import csv
# 请求图片地址
img_link = 'https://game.gtimg.cn/images/lol/act/img/skin/big'
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
        # 需要把信息写入csv文件
        # write = csv.writer(f)
        # # write.writerow(['id', 'name', 'enname'])
        # write.writerow(li)
        # 拼接图片地址
        # img = img_link + heroId + '000.jpg'
        # print(type(heroId))
        print(heroId, name, alias)
        # 把图片写入本地
        # --------------------
        # 获取每个英雄的第一个皮肤，并写入文件
        # res = requests.get(img)   # 请求图片地址
        # if res.status_code == 200:
        #     # 写入图片(视频) 二进制
        #     with open(f'img/{name}.jpg', 'wb') as f:
        #         f.write(res.content)
        # ----------------------
# https://game.gtimg.cn/images/lol/act/img/skin/big1000.jpg
# https://game.gtimg.cn/images/lol/act/img/skin/big2000.jpg
#         获取每个英雄多个皮肤并保存
        for k in range(10):
            # img = img_link + heroId + '%03d' % k + '.jpg'  # '%03d' % k  [000-009]
            # 拼接一个英雄多张皮肤
            if k <= 9:
                img = img_link + heroId + '00' + str(k) + '.jpg'
                # 请求图片地址
            else:
                img = img_link + heroId + '0'+ str(k) + '.jpg'
            res = requests.get(img, headers= header)
            if res.status_code == 200:  # 判断是否请求成功
                with open(f'img/{alias}' + str(k) + '.jpg', 'ab') as f:
                    f.write(res.content)  # 二进制写入图片信息
            pass