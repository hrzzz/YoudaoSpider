import json
import requests
from tkinter import *


def main(content):
    # 复制url，记得去掉'_o'
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 构造请求头
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.121Safari / 537.36',
        'Host': 'fanyi.youdao.com'
    }
    # 构造请求参数
    parameter = {
        'i': content,
        'from': 'zh-CHS',
        'to': 'zh-CHS',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15519651381700',
        'sign': '6e08c6764da13606b9fce21863bfc064',
        'ts': '1551965138170',
        'bv': '33a62fdcf6913d2da91495dad54778d1',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false'
    }
    res = requests.get(url, params=parameter, headers=headers)
    if res.status_code == 200:
        # print(res.text)
        # 化为json数据处理
        data = json.loads(res.text)
        return data["translateResult"][0][0]["tgt"]
    else:
        print("网页请求失败")


# 接下来都是GUI了
root = Tk()
root.title("zz词典")
root.geometry("320x250")
root.resizable(width=False, height=True)
# 第一排输入框 输入查询的内容
# 左边是一个标签
l1 = Label(root, text='查询内容', bg="yellow", font=(12), height=1, width=8)
l1.place(x=20, y=20)
var1 = StringVar()
input_text = Entry(root, textvariable=var1)
input_text.place(x=100, y=20)

# 第二排显示框 显示查询的结果
# 左边是一个标签
l2 = Label(root, text='查询结果', bg="yellow", font=(12), height=1, width=8)
l2.place(x=20, y=60)
var2 = StringVar()
output_text = Entry(root, textvariable=var2)
output_text.place(x=100, y=60)


# 调用youdao函数，传进要翻译的内容
def func():
    words = var1.get()
    if words:
        result = main(words)
        var2.set(result)


# 添加一个按钮
b = Button(root, text="查询", command=func)
b.place(x=170, y=100)

root.mainloop()
