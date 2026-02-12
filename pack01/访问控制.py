# class People:
#     def __init__(self, name, age, salary):
#         self.name = name # 默认公开的
#         self._age = age # 受保护的,通过单下划线约定
#         self.__salary = salary #私有的，通过双下划线约定
#
#     def get_salary(self):
#         return self.__salary

#创建对象
# tom = People('Tom', 28, 40000)
#访问三种类型的属性
# print(tom.name)
# print(tom._age)  #提示受保护，但是能访问
# print(tom.__salary) #提示没有这个属性，访问报错，而不会编译报错

#通过定义的共有方法访问私有属性
# print(tom.get_salary())
#
# print(tom.__dict__)
#
#


# class A:
#     name = '爷爷的属性'
#
#     def f(self):
#         print('爷爷中的方法')
#
#
# class B(A):
#     # name = '父类的属性'
#
#     def f(self):
#         print('父类中的方法')
#
#
# class C(B):
#     pass
#
#
# # 创建对象
# c = C()
# print(c.name)
# print(C.__mro__)

# class Person:
#     def __init__(self, name, age, gender, height, weight):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.height = height
#         self.weight = weight
#
#     def get_info(self):
#         print(self.name, self.age, self.gender, self.height, self.weight)
#
# class Student(Person):
#     def __init__(self, name, age, gender, height, weight, idd, score, profession):
#         # 通过  super().方法名()  进行重写
#         super().__init__(name, age, gender, height,weight)
#         self.idd = idd
#         self.score = score
#         self.profession = profession
#
#     def get_info(self):
#         super().get_info()
#         print(self.idd, self.score, self.profession)
#
# aa = Student('aa',28,'男', 183.0, 160, 20240101, 150, '软件工程')
# aa.get_info()

# class A:
#     def method(self):
#         print("A.method")
#
# class B(A):
#     def method(self):
#         # super().method()  # 调用下一个 MRO 类（C）
#         print("B.method")
#
# class C(A):
#     def method(self):
#         # super().method()  # 调用 A
#         print("C.method")

# mro顺序: 本应该是B,但是B的method方法主动调用了父类A的method方法, 所以显示调用A的method
# class D(B, C):
#     pass
#
# print(D.__mro__) # (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# d = D()
# d.method()  # 输出取决于 MRO 顺序（此处输出 B.method）
#
# class Animal:
#     def make_sound(self):
#         print("动物叫")
#
# class Dog:
#     def make_sound(self):
#         print('汪汪汪')
#
# class Cat:
#     def make_sound(self):
#         print('喵喵喵')
#
# # 定义一个接口|方法
#
# def sound(animal):
#     animal.make_sound()
#
# # 调用
# cat = Cat()
# dog = Dog()
# sound(cat)
# sound(dog)

class Company:
    # 类属性
    name = '有限责任公司'

    # 类方法, 使用注解进行指定
    @classmethod
    def desc(cls):
        print(f'类内查看引用 {id(cls)}')


# c = Company()
print(Company.name)  # 有限责任公司
Company.desc() # 类的引用 1681426523744
print(f'类外查看引用:{id(Company)}')