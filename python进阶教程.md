# 模块

1. 第三方模块
安装命令：pip install 第三方模块名 <br>
常见的第三方模块：requests、pandas、flask、Django
```shell
# 安装后的路径：E:\python\Python311\Lib\site-packages
pip install Django
```
2. 自定义模块
```python

# 文件1 file1.py

def func(executor):
    print(f'{executor}调用 file1中的方法')
    
func('file1')


# 文件2 file2.py
# 导入文件1，把文件1作为模块导入到文件2中
import file1 as f

f.func('file2')

# 此时会打印
#file1调用 file1中的方法
#file2调用 file1中的方法

```

模块和脚本的区分：
1. 脚本：在当前python脚本中运行的叫脚本
2. 模块：导入到其他文件中使用的叫模块
3. `__name__`:  区分python文件
   1. `__name__=__main__`: 作为脚本
   2. `__name__=模块名`: 作为模块

如果测试函数的步骤比较复杂，测试的代码量比较多，注释比较麻烦，就可以增加一个`__name__`的if判断，那么当前文件中的函数测试，作为模块导入时不会执行 <br>
举个例子：<br>
上面file1中，调用了func()函数，在file2中导入file1，执行file2的时候，file1中的函数也会被执行，如果不行在file2中执行的时候，同时在file1中也执行，就可以用上的方式：

```python
# 文件1 file1.py

def func(executor):
    print(f'{executor}调用 file1中的方法')
    
if __name__ == '__main__':
    func('file1')

# 文件2 file2.py
# 导入文件1，把文件1作为模块导入到文件2中
import file1 as f

f.func('file2')

# 此时只会打印
#file2调用 file1中的方法
```

3. 模块导入的方式方法 <br>
import 模块名 ： 导入模块中的所有的数据，在使用的时候，需要带上模块名
```python
import file1 as f

file1.func('file2')
```

from 模块名 import 函数/类名/常量: 导入模块中指定的功能，只能使用指定的功能，其他功能没有导入
```python

# file1中定义的函数
def func(executor):
    print(f'{executor}调用 file1中的方法')

def func1():
    print(f'from导入方式')

# file2中导入函数func1
from file1 import func1

func('file2') # 这里会提示没有这个函数
func1() # 只能执行导入的func1，并且执行的时候可以不带模块名


```

# 包管理
概念： 组织模块的一种方式，包含多个模块和子包的目录 <br>
存放位置：lib/site_packages <br>
创建包：选择工程名或者工程下的文件夹名 -> 右键选择 `python软件包` -> 输入包名 -> 创建包，并且在包下生成一个`_init_.py`的文件，文件为空，但必须存在，如果删除了就会变成文件夹 <br>
导入包语法：
1. import 包名[.子包名].模块名
2. from 包名 import 模块名
3. from 包名.模块名 import 函数名/变量
```python
# from的方式
from pack01.file1 import func1
func1() # 调用函数

# import的方式
import pack01.file1

pack01.file1.func('file2') # 调用函数的时候要使用 包名.模块名.函数名 进行调用
```

# python中的面向对象编程思想
语法格式：
```python
# 定义类
class 类名:
#这里的pass是一个占位符，表示暂时还没实现类的内容，之后再慢慢添加属性和方法；用来创建一个简单的数据容器，可以把它当成“可动态添加属性的结构体”，Python 的类可以动态添加属性
    pass 

# 创建对象
对象名 = 类名()

```
注意点： <br>
1.类名也是标识符的一种，要遵循标识符的规定，且采用大驼峰命名法 <br>
2.创建对象时，类名后一定要加() <br>
3.pass是常用于占位、标记类、或当作动态属性容器

```python
class People:
    pass

# 创建对象
chao = People()

# python动态添加属性
chao.name = 'chao'
chao.age = 28

print(f'chao.age: {chao.age} , chao.name: {chao.name}')

```
### 1.类的属性
1.1 类属性: 定义在类中的属性，可以通过对象来调用，但不能通过对象来修改，只能通过`类名.属性名`来修改
```python
class People:
    # 类属性（Java 中 static 字段）
    name = 'python'

    # 实例方法第一个参数必须是 self
    def func(self):
        print('类中的方法')


aa = People()
bb = People()
print(aa.name, bb.name) # python python

# 通过类名.属性名来修改类属性，无法通过实例来修改属性值
People.name = 'java'
print(aa.name, bb.name) # java java

```
1.2 实例属性： 必须定义在构造方法中，在创建对象时，自动调用构造方法，用于初始化对象的属性，构造方法的名字是固定的：`__init__(self)`
```python
class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hi {self.name}, i am {self.age} years old.')

# 必须上送实例属性
aa = People('aa', 28)
bb = People('bb', 22)
aa.say_hello() # Hi aa, i am 28 years old.
bb.say_hello() # Hi bb, i am 22 years old.
```
1.3 类的魔术方法
当直接打印类的对象的时候，得到的是对象的地址，可以使用魔术方法`__str__`来定义打印的内容，例如打印当前对象的所有属性
```python
class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #魔术方法
    def __str__(self):
        return f'Hi {self.name}, i am {self.age} years old.' #返回的必须是字符串类型

aa = People('aa', 28)
print(aa) # Hi aa, 28 years old.
``` 

`__del__`：析构函数，用于显示删除对象，对象在调用完成后，如果后续没有指针引用，就会被python的垃圾回收器自动回收销毁，如果希望手动销毁，就可以使用这个函数，当自动销毁时，也会调用这个函数
```python
class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #魔术方法
    def __str__(self):
        return f'Hi {self.name}, i am {self.age} years old.' #返回的必须是字符串类型

    #析构函数
    def __del__(self):
        print('主动对象销毁')

#打印对象
aa = People('aa',28)
print(aa)
#打印结果，这里就自动调用了__del__(self)函数
#Hi aa, 28 years old.
#自动销毁对象

```

## 类的三大特征：封装、继承、多态
1. 封装<br>
目的：隐藏对象的内部细节，仅暴露必要的接口，以提高代码的安全性、可维护性和复用性,在python中，封装主要是通过`访问控制`来实现，包括`通过命名约定和属性装饰器来实现`

1.1 命名约定<br>
不写(public公开的): 普通属性和方法默认就是公开的，外部可以直接访问<br>
_（protected受保护的）：以单英文下划线开头，表示“不建议外部直接访问”，但是python不会阻止访问<br>
__(private私有的)：以双英文下划线开头，表示“不能在外部直接访问”，访问会报错

#### Java vs Python 的核心区别

| 方面    | Java                             | Python                 |
| ----- | -------------------------------- | ---------------------- |
| 编译器检查 | 强制                               | 不强制                    |
| 修饰符   | public/protected/private/default | 无硬性修饰符，仅约定 _ / __      |
| 子类访问  | protected 可访问                    | _ 可访问，__ 名称重整避免直接访问    |
| 封装性   | 真正封装                             | 依赖约定，不强制封装             |
| 语法支持  | 内置                               | 基于命名约定 + Name Mangling |

总结：<br>
Java：`严格封装`，访问控制由语言和编译器强制。<br>
Python：`靠约定`，_ 表示受保护，__ 表示伪私有，`最终可以访问`。<br>
在 Python 中，“我们不应该访问私有变量”更多是一种约定和团队规范，而不是语言限制。<br>
```python
class People:
    def __init__(self, name, age, salary):
        self.name = name # 默认公开的
        self._age = age # 受保护的,通过单下划线约定
        self.__salary = salary #私有的，通过双下划线约定

    def get_salary(self):
        return self.__salary

#创建对象
tom = People('Tom', 28, 40000)
#访问三种类型的属性
print(tom.name)
print(tom._age)  #提示受保护，但是能访问
# print(tom.__salary) #提示没有这个属性，访问报错，而不会编译报错

#通过定义的共有方法访问私有属性
print(tom.get_salary())

#通过__dict__来查看实例中的属性
print(tom.__dict__) #{'name': 'Tom', '_age': 28, '_People__salary': 40000}
```
私有属性设置的原理：通过名称的重整来实现，就是实际上这个名字不叫__salary了，我么可以通过`__dict__`来查看实例中的属性，重整后的名字叫做`_People__salary`，注意这里是单下划线开头，所以我们可以通过重整后的名称访问私有变量的值，但是这是不建议的，这样就会违反python的设计初衷

1.2 使用@property装饰器把方法当当成属性来使用，实现更优雅的封装（Getter/Setter）<br>
1️⃣把一个方法当成属性访问（无需括号）
```python
class People:
    @property
    def age(self):
        return 18

# 返回方法
p = People()
print(p.age) #像访问属性一样访问方法，不需要使用括号：p.age()
```

2️⃣@property + setter 实现可控写入
例如，在赋值时进行参数校验

java写法
```java
public class Person{
    private int age;
    
    public setAge(int age){
        if(age < 0) throw new IllegalArgumentException();
        this.age = age;
    }

}
```
python写法
```python
class Person:
    def __init__(self):
        self._age = 0
    
    @property  # getter方法
    def age(self):
        return self.age

    @age.setter #setter方法
    def age(self,age):
        if age < 0:
            raise ValueError("年龄不能为负")
        else:
            self._age = age

#创建对象
p = Person()
p.age = 18  # setter自动触发，像属性赋值一下调用方法赋值
print(p.age)  # 自动调用 getter，像属性一样调用方法获取值
```
3️⃣@property 常见应用场景

数据校验（如年龄、价格不能为负数）

延迟加载（属性用到时才计算）

把计算属性伪装成字段（如 BMI）

保留 API 不变的同时修改内部逻辑

4️⃣总结

一句话解释，@property = 用方法伪装成属性，让 getter/setter 更 Pythonic。

## 单继承
概念：一个子类（派生类）继承一个父类（基类） <br>
作用：通过继承，子类可以复用父类的代码，减少代码的冗余和提高代码的可维护性；父类中的私有属性是无法被子类继承的 <br>
格式：
```python
class 父类名:
    pass

class 子类名(父类名):
    pass

# 例如：

class Person:
    name = "父类的属性"

    def way(self):
        print('父类的方法')

class Student(Person):

    # 重写父类的方法
    def way(self):
        print('子类中的方法')

s = Student()
s.way()
print(s.name)
```

新式类和经典类：<br>
python3之后都是新式类<br>
经典类不支持魔术方法和继承的传递性<br>
```python
#python3.0之前类的定义
class 类名:  #经典类
    pass

class 类名(): #经典类
    pass

class 类名(object): #新式类
    pass

#python3.0之后上面的定义方式都是新式类
    
```

单继承的顺序 -> 继承的传递性
```python

class A:
    name = '爷爷的属性'
    
    def f(self):
        print('爷爷中的方法')

class B(A):
    name = '父类的属性'
    
    def f(self):
        print('父类中的方法')

class C(B):
    pass

# 创建对象
c = C()
print(c.name) # 打印父类的属性

# 注释掉父类中的name属性
print(c.name) # 打印爷爷的属性

#查看类的继承链，通过 类名.__mro__ 进行查看
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>), 解读：C继承B，B继承A

```
    
### 方法重写
作用：子类在父类方法的基础上进行修改<br>
注意点：参数格式、参数位置要一致，重写的方法会覆盖父类的方法<br>
方法重写的实现方法：
1) 同名方法的覆盖
```python
class Person:
    name = "父类的属性"

    def way(self):
        print('父类的方法')

class Student(Person):

    # 重写父类的方法
    def way(self):
        print('子类中的方法')

s = Student()
s.way()
print(s.name)
```
2) super().方法名() --> 推荐,注意：这里没有self
```python
class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def get_info(self):
        print(self.name, self.age, self.gender, self.height, self.weight)

class Student(Person):
    def __init__(self, name, age, gender, height, weight, idd, score, profession):
        # 通过  super().方法名()  进行重写
        super().__init__(name, age, gender, height,weight)
        self.idd = idd
        self.score = score
        self.profession = profession

    def get_info(self):
        super().get_info()
        print(self.idd, self.score, self.profession)

aa = Student('aa',28,'男', 183.0, 160, 20240101, 150, '软件工程')
aa.get_info()

# 打印效果和下面的一样
```
3) 父类名.方法名(self)， 这里有个self  ，不推荐，这样更复杂，直接使用super().方法名()即可，和java类似
```python
#使用场景：子类在继承父类数据时，子类需要用到父类中较多的数据时
class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def get_info(self):
        print(self.name, self.age, self.gender, self.height, self.weight)

class Student(Person):
    def __init__(self, name, age, gender, height, weight, idd, score, profession):
        # 通过  父类名.方法名(self)  给父类传递数据
        Person.__init__(self, name, age, gender, height, weight)
        self.idd = idd
        self.score = score
        self.profession = profession

    def get_info(self):
        # 调用父类的方法
        Person.get_info(self)
        print(self.idd, self.score, self.profession)

aa = Student('aa',28,'男', 183.0, 160, 20240101, 150, '软件工程')
aa.get_info()
# 打印如下：
# 这是调用父类方法打印的：aa 28 男 183.0 160
# 这是子类方法打印的 20240101 150 软件工程
```
## 多继承和多态
子类拥有一个父类叫单继承，拥有多个父类叫多继承
格式：
```python
class 类名(父类1,父类2,...)
    pass
```
1. 多继承有同名方法时，搜索方法时会先按照`__mro__`的输出结果，按照`从左往右`的顺序查找，先在哪个父类中找到了，就用哪个父类的<br>
2. 如果在当前类(子类)的方法中找到了，就直接执行，不再搜索
3. 如果找到最后一个类(object)还没找到，程序就会报错

## 继承的菱形问题
Python 中的菱形问题（Diamond Problem）是多继承场景下的一个经典问题，主要出现在类继承结构形成菱形时（即`一个子类继承自两个有共同基类的父类`）。以下是其核心原理、问题表现及解决方案的总结：

1. 菱形问题的定义与结构
继承结构：
基类 A，两个父类 B 和 C 均继承自 A，子类 D 同时继承 B 和 C，形成如下菱形结构：
```text
    A
   / \
  B   C
   \ /
    D
```

问题表现：
当 D 调用 A 中的方法时，若 B 和 C 都重写了该方法，Python 需决定从 B 还是 C 的路径继承该方法，可能导致方法调用冲突或重复执行

2. 问题产生的原因<br>
方法解析顺序（MRO） ：<br>
Python 通过 `C3线性化算法` 确定方法调用顺序（即 `__mro__` 属性）。若 MRO 未合理规划，可能导致基类方法被多次调用或逻辑混乱

示例代码：
```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        print("B.method")

class C(A):
    def method(self):
        print("C.method")

class D(B, C):
    pass

d = D()
d.method()  # 输出取决于 MRO 顺序（此处输出 B.method）
```
此时 D.__mro__ 为 (D, B, C, A, object)，因此优先调用 B.method

3. 解决方案<br>
(1) 显式调用父类方法<br>
使用 super() 函数按 MRO 顺序调用父类方法，避免重复执行：
```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        super().method()  # 调用下一个 MRO 类（C）
        print("B.method")

class C(A):
    def method(self):
        super().method()  # 调用 A
        print("C.method")
```
此时 D().method() 会依次执行 A → C → B 的方法

(2) 调整继承顺序<br>
通过改变子类的继承顺序影响 MRO：
```python
class D(C, B):  # MRO 变为 (D, C, B, A, object)
    pass
```
此时 d.method() 优先调用 C.method

(3) 避免菱形结构<br>
重构代码，使用 组合替代继承 或 单一继承，减少多继承的复杂性

4. 实际应用建议
优先使用 super() ：确保多继承时父类方法按预期顺序调用。<br>
检查 __mro__ ：通过 print(D.__mro__) 确认方法解析顺序。<br>
谨慎设计继承：菱形结构在框架或复杂系统中可能有用，但需明确设计意图

**总结**<br>
菱形问题的本质是 多继承方法调用的二义性，Python 通过 MRO 和 super() 提供了解决方案。理解 C3 算法和合理规划继承结构是避免问题的关键
。若需进一步优化代码，可参考设计模式（如 Mixin）替代多继承。

### super()含义解析
先看下面的代码示例
```python
class A:
    def method(self):
        print("A.method")

class B(A):
    def method(self):
        super().method()  # 调用 C.method（因为 MRO 中 B 的下一个是 C）
        print("B.method")

class C(A):
    def method(self):
        super().method()
        print("C.method")

class D(B, C):
    pass

d = D()
d.method()
```
首先,在B的method方法中先调用了`super().method() -> A的method方法`,然后下面一行代码是`print("B.method")`, D(B,C)的继承顺序是从左到右，即B->C，但是B的method方法中手动调用了super.method()，即A的method方法，所以先打印A的method方法中的内容，在调用完A的method方法后,并没有执行`print("B.method") `,而是执行了C中的method方法,并且在C的method方法中也调用了A的method方法
,但是并没有打印`A.method`，最终打印结果如下：
```text
A.method
C.method
B.method
```
**这是为什么呢？**<br>
super().方法名()：含义是调用下一个类中的指定方法，而不是简单的调用的父类的指定方法，
具体顺序可以看`__mro__`打印的结果，先注释掉`super().method()`，打印结果如下：
```text
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
缩写：D -> B -> C -> A
```
当调用B的method方法时，遇到`super().method()`，所以就直接调用下一个类中的method()方法，即C中的method()方法，然后在C的method()方法中又调用了
`super().method()`，所以会调用A的method()方法，即`打印A.method`, 然后根据方法的回调链路，就是调用`C的print("C.method")`，接下来是`B的print("B.method")`

## 多态
Java 和 Python 的多态机制虽然都遵循面向对象编程的“一个接口，多种实现”原则，常说java的多态是父类引用指向子类对象，java的多态通过继承、接口和方法重写，python的多态则是通过方法重写和鸭子类型（无需显式继承或接口）。
```javascript
#多态举例
class Animal {
    void makeSound() { System.out.println("Animal sound"); }
}
class Dog extends Animal {
    @Override
    void makeSound() { System.out.println("Bark"); }
}
public class Main {
    public static void main(String[] args) {
        Animal a = new Dog();  // 父类引用指向子类对象
        a.makeSound();  // 输出 "Bark"（动态绑定）
    }
}
```
python多态举例
```python
class Animal:
    def make_sound(self):
        print("Animal sound")

class Dog:
    def make_sound(self):  # 无需显式继承
        print("Bark")

# 定义一个方法(接口)
def animal_sound(animal):
    animal.make_sound()  # 鸭子类型：只要有 make_sound 方法即可

dog = Dog()
animal_sound(dog)  # 输出 "Bark"
```
看起来像父类引用指向子类对象，但实际上，Dog和Anaimal没有指定继承关系，只是有相同的方法，这个叫做鸭子类型，俗语就是：如果一个动物看起来像鸭子，游起来像鸭子，叫起来像鸭子，那么它就是鸭子

## 方法总结分类
之前学过了属性分类：类属性：定义在类里面的属性，实例属性：定义在狗仔方法中的属性 <br>

方法也分为好几类：

1. 类方法
> 绑定给类的方法，第一个参数必须是cls，表示为类的引用，使用类名调用类方法
```python
class Company:
    # 类属性,
    name = '有限责任公司'

    # 类方法, 使用注解进行指定
    @classmethod
    def desc(cls):
        print(f'类内查看引用 {id(cls)}')


print(Company.name)  # 有限责任公司
Company.desc() # 类内查看引用 2252116736832
print(f'类外查看引用:{id(Company)}') # 类外查看引用:2252116736832

```

使用场景: <br>
类属性属于类本身而非实例，所有实例共享同一份数据。常见场景包括：<br>
a. 共享全局状态,例如统计实例数量、存储公共配置（如默认参数、全局开关）<br>
b. 常量定义<br>
c. 默认配置管理 ,所有实例共享同一配置，修改类属性即可全局生效<br>

类方法通过cls参数操作类自身，主要场景包括：<br>
a. 替代构造函数（工厂模式）<br>
b. 修改或获取类级别的状态（如重置计数器、更新全局配置）<br>
c. 支持继承多态,`子类调用类方法时，cls自动指向子类`，确保行为正确扩展<br>
d. 类级别工具方法,执行与类相关但不依赖实例的逻辑（如数据校验、单例模式）<br>
e. 工厂模式、单例模式的核心实现手段<br>
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # 代替构造函数
    @classmethod
    def from_string(cls, s):  # 从字符串构造
        name, age = s.split(",")
        return cls(name, int(age))

########################################3

class Animal:
    @classmethod
    def create(cls):  # 子类调用时返回子类实例
        return cls()

class Dog(Animal):
    pass

dog = Dog.create()  # 创建的是Dog实例
```

2. 构造方法
> 在创建对象时自动执行的方法, `__init__()`

3. 实例方法
> 绑定给对象的方法，第一个参数必须是self，表示为对象的引用

4. 静态方法
> 谁也没有绑定，独立的功能函数

