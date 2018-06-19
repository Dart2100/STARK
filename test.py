#!/user/bin/env python3
# -*- encoding:utf-8 -*-
# 序列化的目的是为了各个程序之间的数据传输，比如格式化成xml等格式；json与python搭配较好；

import json

# 序列化dict
d = dict(name="Mike", age=20)
f = json.dumps(d)  # f 即为序列化后的字符串

cf = json.loads(f)  # cf = d


# 序列化class -- 需定义转换dict函数
class Person(object):  # 定义class
    def __init__(self, name, age):
        self.name = name
        self.age = age


def todict(self):  # 定义转换函数
    return {
        'name': self.name,
        'age': self.age
    }


s = Person("Mike", 20)
f = json.dumps(s, default=todict)  # default= 不可省略   f即为序列化后的字符串

# 将json转化为class需要两步
#       1 使用json.loads()将json转换成dict
#       2 将dict转化成class ---自定义函数
d = json.loads(f)

def dict_class(d):
    return Person(d['name'], d['age'])

ss = dict_class(d)  # ss即为json:f转化成的class
print(ss)
