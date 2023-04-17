# 1.正则表达式

#导包
import re
def zhengze():
    s = '阅读数1000，点赞数9999,阅读数1000'
    # match方法 ,从头匹配
    obj = re.match('读数\d', s)
    if obj:
        # print(obj.group())
        pass
    #search方法 只匹配一个
    obj1 = re.search('阅读数\d', s)
    if obj1:
        print('search方法：'+obj1.group())
        pass
    # findall()方法 返回的是一个列表 #\d和\d+的区别
    res = re.findall('阅读数\d+', s)
    if res:
        print('findall方法：'+str(res))

# zhengze() #方法的调用


# 2.xpath 复习
# //任意位置、 /前面元素是后面元素的父亲 、
# text()获取文本信息、@获取属性信息
# 案例：包牛牛站点首页商品信息(商品名字，商品价格，商品链接)
# http://www.bao66.cn/web/
from lxml import html
import requests
def get_xpath():
    #请求地址
    url = 'http://www.bao66.cn/web/'
    #请求头
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    }
    #请求网页
    response = requests.get(url, headers=header)
    #指定编码格式
    response.encoding = 'utf-8'
    #获取网页源码文本信息
    info = response.text
    # print(info)
    #文档树对象
    page = html.etree.HTML(info)
    #使用xpath方法进行解析
    #获取当前页面所有的商品列表
    bag_li = page.xpath('//ul[@class="product_box"]/li')
    #使用循环获取单个商品
    for item in bag_li:
        bag_name = item.xpath('.//p[@class="code"]/a/text()')
        if bag_name:
            bag_name = bag_name[0]
        else:
            bag_name = ''
        bag_price = item.xpath('//a[@class="price"]/b/text()')
        if bag_price:
            bag_price = bag_price[0]
        else:
            bag_price = ''
        bag_link = item.xpath('.//p[@class="code"]/a/@href')
        if bag_link:
            bag_link = bag_link[0]
        else:
            bag_link = ''
        print(bag_name, bag_price, bag_link)
        pass
    pass
# get_xpath()

#3.json模块
#四个方法：json.loads(),json.load(),json.dumps(),json.dump()
# 案例：抖音热搜
# http://www.bao66.cn/web/
import json
import requests
def get_json():
    #请求地址
    url = 'https://www.douyin.com/aweme/v1/web/page/data/?device_platform=webapp&aid=6383&channel=channel_pc_web&module_count=2&spider=0&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=106.0.0.0&browser_online=true&engine_name=Blink&engine_version=106.0.0.0&os_name=Windows&os_version=10&cpu_core_num=4&device_memory=8&platform=PC&downlink=1.95&effective_type=4g&round_trip_time=50&webid=7156035619695986211&msToken=3BqUSVQEAyXdwsOQPPtMo7VhGveMq7VsGKnQz615YZFoxGb-WsVZzlLte0GlTEzeaN9B3e9rMU5TGpbB9LNH-LGWLySWyYbKtIPgzszgTn95eP7l-cBO&X-Bogus=DFSzswVOz7xANHQbS/1kWl9WX7re'
    # 请求头
    headers= {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'referer': 'https://www.douyin.com/discover',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }
    res = requests.get(url, headers=headers)
    #指定编码
    res.encoding = 'utf-8'
    info = res.text
    # print(info)
    #使用json模块
    page = json.loads(info)
    #字典取值
    module_list = page['module_list']
    #遍历列表
    for module in module_list:
        title = module['title']  #详细信息自己解析
        print(title)
def get_json2():
    url = 'https://www.douyin.com/aweme/v1/web/hot/search/list/?device_platform=webapp&aid=6383&channel=channel_pc_web&detail_list=1&source=6&pc_client_type=1&version_code=170400&version_name=17.4.0&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=zh-CN&browser_platform=Win32&browser_name=Chrome&browser_version=106.0.0.0&browser_online=true&engine_name=Blink&engine_version=106.0.0.0&os_name=Windows&os_version=10&cpu_core_num=4&device_memory=8&platform=PC&downlink=1.95&effective_type=4g&round_trip_time=50&webid=7156035619695986211&msToken=3BqUSVQEAyXdwsOQPPtMo7VhGveMq7VsGKnQz615YZFoxGb-WsVZzlLte0GlTEzeaN9B3e9rMU5TGpbB9LNH-LGWLySWyYbKtIPgzszgTn95eP7l-cBO&X-Bogus=DFSzswVOxAUANHQbS/1kWl9WX7JI'
    # 请求头
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'referer': 'https://www.douyin.com/discover',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin'
    }
    res = requests.get(url, headers=headers)
    # 指定编码
    res.encoding = 'utf-8'
    info = res.text
    # print(info)
    # 使用json模块
    page = json.loads(info)
    # 字典取值
    word_list = page['data']['word_list']
    # 遍历列表
    for module in word_list:
        title = module['word']  # 拿到热搜词
        print(title)
    pass


get_json2()
