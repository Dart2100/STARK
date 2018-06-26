#!/usr/bin/env python3


class CarlaSettings(object):

    def __init__(self, **kwargs):
        self.name = 'Mike'
        self.height = 189
        self.age = 20

    def set(self, **kwargs):
        print(kwargs)  # kwargs为dict
        print(kwargs.items())  # dict.items() 即将单独的key:value组合成一个个的小tuple，便于调用；类似的dict.keys() dict.values()
        for key, value in kwargs.items():
            if not hasattr(self, key):  # hasattr(object,key)判断self是否具有key属性
                print("Error:", key)
            else:
                setattr(self, key, value)  # setattr(object,key,value)将self的key属性修改为value
                print("Done")


car = CarlaSettings()
car.set(name="Jone", age=20, home="China")

'''
python的函数传递
    run(*kw)   kw为tuple
    run(**kw)  kw为dict
'''

# 同类的还有 getattr(object,key)  delattr(object,key)
# 接上
getattr(car, 'name')  # >>'Mike'
getattr(car, 'height')  # >>189

delattr(object, key)  # 注：该操作将直接删除object的key属性
delattr(car, 'age')  # 此操作后car将没有age属性了
