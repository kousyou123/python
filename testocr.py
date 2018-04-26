
 #需要修改环境变量
import pytesseract
from PIL import Image
 
# 打开图像：英文
image = Image.open("g.jpg")
 
# OCR识别：lang默认英文
text = pytesseract.image_to_string(image)
 
# 打印识别后的文本
print(text)
 
# 我是分割线
print("*" * 30)
 
# 打开图像：中文
image = Image.open("d.jpg")
 
# OCR识别：lang指定中文
text = pytesseract.image_to_string(image, lang = 'chi_sim')
 
# 打印识别后的文本
print(text)