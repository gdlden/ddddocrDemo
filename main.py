import ddddocr
import sys
import base64




def convert_png(captcha_value):
    image = captcha_value.split(",")[1]     #只需要captcha_value中“base64”后面的
    img = base64.b64decode(image)           #将base64转换成图片
    with open('captcha.png','wb') as f:     #打开图片
        f.write(img)                        #保存图片
 
    #利用ddddocr识别验证码图片上的字符
    ocr = ddddocr.DdddOcr(show_ad=False)                 #实例化对象
    code = ocr.classification(img)          #识别图片上的字符
    return code
code = convert_png(sys.argv[1])
print(code)