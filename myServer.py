import flask
import ddddocr
import base64
from flask import request
import json
from flask import jsonify


def json_resp(code=100, msg='操作成功', data=None):
    return jsonify({'status': code, 'message': msg, 'data': data})
# 创建一个服务
server=flask.Flask(__name__)

@server.route('/login',methods=['get','post'])
def login():
    label=request.values.get('label')
    length=len(label)
    result=f"{label}的长度为{length}"
    return result
@server.route('/randomData/getImageCode',methods=['get','post'])
def convert_png():
    captcha_value=request.get_json()
    jsonstr = captcha_value.get('base64Image')
    # print(jsonstr)
    image = jsonstr.split(",")[1]     #只需要captcha_value中“base64”后面的
    img = base64.b64decode(image)           #将base64转换成图片
    with open('captcha.png','wb') as f:     #打开图片
        f.write(img)                        #保存图片
    #利用ddddocr识别验证码图片上的字符
    ocr = ddddocr.DdddOcr(show_ad=False)                 #实例化对象
    code = ocr.classification(img)
     # 业务处理 ...

    return json_resp(data=code)     #识别图片上的字符
    return code
if __name__ =='__main__':
    server.run(debug=True,port=8889,host="0.0.0.0")
#  0.0.0.0表示不管几个网卡，任何ip都可以访问

