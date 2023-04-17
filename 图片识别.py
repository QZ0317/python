# 导入模块
import pytesseract
from PIL import Image
# 打开图片mode可以忽略，如果要给mode = 'r'
# 将图像文件转化为实例
# img = Image.open('1.png')
# # 识别英语
# # 得到图像中的英文进行输出
# info = pytesseract.image_to_string(img)
# print(info)

# 识别中文
# 使用pytesseract库提取文本信息
# long = 'chi_sim'简体中文，long = 'chi_tra'
# img = Image.open('gushi.png')
# text = pytesseract.image_to_string(img, lang='chi_sim')
# print(text)

# 识别数字
# 打开图片得到图片实例
img = Image.open('2.png')
# 对于数字chi_sim或是默认英文都可以得到结果
text = pytesseract.image_to_string(img, lang='chi_sim')
print(text)

# 利用pytesseract识别出验证码
# -psm 7 为识别模式
# -c tessedit_char_whitelist=1234567890 的意思是 识别纯数字(0-9)
# code = pytesseract.image_to_string(img, lang="eng", config='-psm 7 -c tessedit_char_whitelist=1234567890')
# print(code)
