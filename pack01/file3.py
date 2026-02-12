class People:
    # 类属性（Java 中 static 字段）
    code = 'python'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法第一个参数必须是 self
    def func(self):
        print('类中的方法')

    def say_hello(self):
        print(f'Hi {self.name}, i am {self.age} years old.')

    def __str__(self):
        return f'Hi {self.name}, {self.age} years old.'

    def __del__(self):
        print("自动销毁对象")

# 必须上送实例属性
aa = People('aa', 28)
# bb = People('bb', 22)
# print(aa.code, bb.code)
# aa.say_hello()
# bb.say_hello()

# 通过类名.属性名来修改类属性，无法通过实例来修改属性值
# People.code = 'java'
# print(aa.code, bb.code)
# aa.say_hello()
# bb.say_hello()


print(aa)

del aa

print(aa)