# 变量
```python

#输出函数，可以一次输出多个值，可以使用sep指定分隔符
print("一","二","三",sep= '|')

#end的用法是在输出了hello 后拼接 1，然后再输出第二个hello，再拼接 2
print("hello", end= "1")
print("hello", end= "2")
print("hello", end= "3")

# python定义变量时不需要指定明确的变量类型，同一个变量可以多次赋值，并且可以是不同类型的值，不会重新开辟空间，而是直接修改值
a = 1
print(a)
#
a = 66.6
print(a)
#
a= "hello"
print(a)

# 数值类型：int-整数, float-浮点类型, bool-布尔类型
bool(1) # 将数字转换为bool值,1-True/0-False，注意bool值的True和False都是首字母大写的
print(True+1)  #bool值也是可以直接参与计算的
print(False+1)

# complex-复数,就是复杂的数字类型
#格式：a +bj
com = 5+6j
print(com) # 打印结果(5+6j)

# 字符串类型 -- str，就是被引号包围的数据
name = 'zhangsna'

# 注意：数值型不需要加引号，加了引号就变成字符串了

```

# 占位符精度控制
1.占位符方式
```python
#默认是6位小数
num = 15.987221
#保留两位小数，输出是15.99，除了格式化，默认效果是四舍五入
print("% .2f" % num) 
```
变量类型判断：
```python

i = 'test' 

if isinstance(i, str):
        print(i)

#多类型判断
isinstance(i, (int, float, str))

```


2.**f** 格式化方式
```python
num = 15.987221
print(f"{num:.2f}") #这个也是保留两位小数，也是默认四舍五入
```
3.round(变量,位数)
```python
num = 15.987221
round(num,2) #保留两位小数，输出的类型是浮点数，也是默认四舍五入
```
4.format(变量,位数)
```python
num = 15.987221
print(format(num,'.2f')) #这里实际上输出的是字符串类型的，也是默认四舍五入
```

# 输入函数
语法：变量 = input('提示信息：')<br>
作用：用来接收用户在控制台的输入的数据<br>
在python中，Input功能会等待用户输入，输入的任何形式的数据都是`字符串类型`，在java中用的是`
Scanner scanner = new Scanner(System.in);`所以两个数字的字符串相加不是做加法，而是拼接
```python
score = input('请输入分数：')
print(score, type(score))    # 99 , <class 'str'>
```
类型转换：<br>
int() : 将字符串引号包裹的整数或者浮点类型转换为整数<br>
float():将引号包裹的浮点数或者整数转换为float类型的数据,如果是整数，转换的浮点类型数会有一位小数0

# 算术运算符

加减乘除（+ - * /）<br>
取整除(//) ：两数相除以后取整数部分<br>
取余数(%)：两数相除后取小数部分<br>
幂(**)：取一个数的n次方

注意：这里需要知道优先级，最常见的就是先乘除后加减，这里的乘除、取整除、取余数，这四个优先级是同级，这个时候就按照先后顺序（从左往右），最高级就是幂运算了<br>
`幂 > 乘 除 取整除 取余数 > 加 减`

# 比较运算符

这里就是  and  or  not  <br>
注意：在比较数字的时候，只要`非0非空就是真（True）`，所以 1 是真，10是真，100也是真
```python
# 这里打印的不是True，而是2，因为and是全为真才是真，所以会比较到2这个位置，此时比较完了，是真，所以打印2
print(10 and 2)
# 这里同理，10是真，还是会比较到0这个位置，发现是假，就返回0
print(10 and 0)

# 这里的or就是或，一真即真，比较到10为真，就直接打印了10
print(10 or 0)
# 这里比较0为假，但是后面还有数，所以会比较10，为真，所以打印10
print(0 or 10)

#这个就更形象了，由于是and，所以这里比较了15 比较10 ，然后比较到了0，此时为假就结束了，打印了0
print(15 and 10 and 0 and None)
```

# bool()函数总结
布尔值为False时：**为零为空** <br>
为零：整数零、浮点数零、复数零<br>
为空：字符串、空列表、空元组<br>


# if判断
语法结构：<br>
```python
"""
if 判断条件: (这里有个冒号)
    如果为True就执行这里的代码
else:
    如果为False就执行这里的代码

"""
# 下面是双分支
num = 15
if num > 15:
    print("大于15")
else:
    print("小于等于15")

# 下面是多分支
num = 15
if num > 15:
    print("大于15")
elif num == 15:
    print("等于15")
else:
    print("小于15")

#下面是嵌套if
if num > 15:
    if num > 20:
        print("大于20")
    else:
        print("15到20之间")
elif num == 15:
    print("等于15")
else:
    print("小于15")
```

# 循环

1. while循环

```python
"""
语法结构：
while 变量值满足条件:
    循环体（满足条件时执行）
    改变条件变量
"""

n = 1
while n < 10:
    print(n)
    n += 1 # 这里注意下，python没有 n ++ 这种写法

```
2. for循环
```python

for i in range(0,10):
    print(f"{i}")

```
这里可以了解下range函数:<br>
原型：range(start, end, step)<br>
作用：生成指定范围的整数<br>
start：计数开始的位置，默认从0开始<br>
end：计数结束的位置<br>
step：步长，默认为1<br>
range的实际范围是左闭右开的区间 [start,end)<br>

# 字符串编码

**1 ASCII编码:128位，十进制0~127<br>**
ord():将字符转换成ASCII编码中，对应的十进制数字#chr():将ASCII编码中，对应的十进制数字转换成字符<br>
```python
print(ord('A')) # 65
print(ord('t')) #116
print(chr(110)) #'n'
```

**2 GB2312/GBK编码<br>**
GB2312:用于解决简体中文的编码<br>
GBK:在GB2312的基础上扩展繁体中文，以及亚洲文字<br>

**3 Unicode国际字符编码标准**

类型:
UTF-8:可变长度编码，兼容ASCII，最常用<br>
UTF-16:使用2或4字节  <br>
UTF-32:固定4字节<br>

**4 编码解码函数<br>**
编码函数 char.encode()
```python
from numpy import char
char.encode(encoding='编码方式（默认UTF-8）',error = '编码错误的处理方式')

#编码错误的处理方式
#      strict:严格模式，遇到无法编码的字符时，代码报错，默认
#      replace:遇到无法编码的字符时,用?替换
#      ignore：遇到无法编码的字符时，忽略或者跳过继续编码其他字符

```

# 字符串的常见操作
在java的字符串中，不可直接通过下标获取字符，除非转换为字符数组，但是在python中，可以直接通过下标获取字符。python中字符串的下标是从0开始依次按顺序向后分配，并且还分为正向索引和负向索引（从右向左）。
除此之外还有切片，就是从字符串中间段一段，`切片`语法：[start:end:step]，结果就是[start,end)经典的`包前不包后`
并且除了正向切片，也有负向切片，`切片过程中超出范围不会报错`<br>
正向切片：步长 > 0 ,从左向右切片<br>
负向切片：步长 < 0， 从右向左切片
```python
# 下面字符串的正向索引是 0 1 2 3 4， 负向索引是 -5 -4 -3 -2 -1
str = 'hello'
print(f'{str[0]}')
print(f'{str[-5], str[-1]}')

# 打印结果 he
print(f'{str[0:2]}') # 步长默认1
print(f'{str[::]}') # 截取整个字符串
print(f'{str[::-1]}') #负向切片，输出的时候是倒序切片 -> olleh

# 可以通过len()获取字符串长度
print(f'{str[len(str)-1]}')
```
#### 操作函数
1) 字符串.strip('需要去除的首位字符')，如果没有指定，默认去除的是空格
2) 字符串.lstrip('需要去除的首部字符')，这个是去除首部的指定字符，如果没有指定，默认去除的是空格
3) 字符串.rstrip('需要去除的尾部字符')，这个是去除尾部的指定字符，如果没有指定，默认去除的是空格
```python
str = '+hello+'
print(str.strip('+').strip()) #显示去除首尾的+号，然后去除首尾的空格
```
4) 字符串.split(分隔符,分隔次数)，通过指定字符分隔字符串，得到的是一个列表 ,默认以空白字符串作为分隔点，默认全部分隔完
5) 字符串.replace(旧字符，新字符，替换次数)，通过新字符替换旧字符,也可指定替换次数，默认全部替换
```python

str = 'hello world study python' 
print(str.split()) # ['hello' ,'world' ,'study','python'] 默认以空白字符串作为分隔点，默认全部分隔完
print(str.strip(' ', 1)) # ['hello', 'world study python'] 只分割了一次

print(str.replace(' ','|')) #hello|world|study|python ,用竖杠替换空格
print(str.replace(' ','|',1)) #hello|world study python  ,用竖杠替换空格但是只替换一次

```
6) '连接符'.join(可迭代对象)，将可迭代对象中的字符串元素，通过指定的连接符组合成字符
```python
lst = ['hello' ,'world' ,'study','python'] #列表中的元素必须是字符串，否则会报错
s = ' '.join(lst) #把列表中的元素用空格连接起来
print(s) #得到的结果就是字符串类型
```
7) 字符串.find(查找的元素)，查找元素所在的位置，返回下标，如果不存在返回-1
8) 字符串.index(查找的元素)，查找元素所在的位置，返回下标，如果不存在会报错
9) 字符串.lower(),字符串转换为小写，同理还有upper()
10) 字符串.title(),把字符串每个单词的首字母转换为大写
11) 字符串.islower(),判断字符串中的字符是否都是小写
12) 字符串.isupper(),判断字符串中的字符是否都是大写
13) 字符串.istitle(),判断字符串中的每个单词是否都是大写开头
14) 字符串.startswith('字符'),判断字符串是否已指定字符开头
15) 字符串.endswith('字符'),判断字符串是否已指定字符结尾
16) 字符串.isdigit(),判断字符串是否是整数 
17) 字符串.isalpha(), 判断字符串是否为纯字符组成
18) 字符串.any(),只要有一个字符满足要求就是True

# 列表相关操作

列表(list)一种非常灵活的数据类型，是有序可重复的，可以存不同类型的一系列数据，格式：变量名 = [数据1，数据2，数据3] <br>
为什么python的列表可以存不同的数据类型，java不可以? <br>
1.java是静态强类型，编译器就需要确定类型，实现类型安全<br>
2.python是动态弱类型，运行时才决定类型，可混放任意对象 <br>
3.列表是有序的，这里的有序是下标有序，也可以进行切片，也存在`正向索引（从左往右，从0开始，步长大于0）和负向索引（从右往左，从-1开始，步长小于0） 🌟🌟` <br>
4.这里列表看起来和字符串功能一样，但是实际上字符串的底层并不是列表，而是紧凑不可变的Unicode字符序列（连续内存），支持下标和切片是因为实现了序列协议，而且切片是在复制创建新字符串<br>


**成员运算符<br>**
in: 如果元素在列表中，返回True <br>
not in: 如果元素不在列表中，返回True <br>
```python
# 定义列表
lst1 = [100, 101.1,'test', True]
lst2 = list.list()

#获取列表元素个数: len(列表)
print(len(lst1))

#成员运算符
print( 666 in lst1)
print(666 not in lst1)

#遍历列表
for i in lst1:
    print(i)
    
#打印列表,可直接使用print打印
print(lst1)

```
**列表元素操作：增删改**

1. 修改元素：列表[索引] = 新数据
2. 增加元素：
   1. 在指定位置插入元素：列表.insert(索引,新元素)，一次只能插入一个元素
   2. 在列表尾部添加元素：列表.append(新元素)，一次只能追加一个元素 
   3. 在列表中添加多个元素：列表.extend(可迭代对象)，可迭代对象包括字符串、列表等。如果是用这个方法添加的迭代对象是字符串，那么最终添加到列表中的是单个字符

3. 删除元素
   1. 通过索引值删除元素：`del 列表[索引值]` 、 `列表.pop[索引值]`，可以使用正向和反向的索引
   2. 删除列表：`del 列表名`
   3. del和pop的区别在于，pop只能删除元素，del还可以删除列表
   4. 使用索引值删除元素的时候，一定不能超出列表索引范围，否则会报错
   5. 删除指定元素：`列表.remove(元素)`，删除元素不存在，代码会报错，存在多个满足条件的元素，只会删除第一个元素
   6. 清空列表：`列表.clear()`

```python
lst = [100,101.1,'test', True]
lst.extend('python')
print(lst) # [100, 101.1, 'test', True, 'p', 'y', 't', 'h', 'o', 'n']

#场景题：如果列表中某个元素重复出现好几次，要如何全部删除？
lst2 = [100,101.1,'test', 100,True,100]
print(lst2) #[100, 101.1, 'test', 100, True, 100]
cnt = lst2.count(100)
for i in range(cnt):
    lst2.remove(100) 
print(lst2) #[101.1, 'test', True]
```

**列表元素操作：查询**
1. 通过len(列表)获取列表元素个数，列表索引范围：[0,len(列表)-1] 
2. 计算列表中元素出现的次数: `列表.count(元素)`
3. 获取列表中指定元素的索引值：`列表.index(元素)`，如果查找的元素不存在会直接报错。

**列表元素操作：排序**
1. 对整数列表排序，默认进行从小到大排序：列表.sort() 
2. 对字符串列表进行排序，默认根据字符串元素长度从小到大排序 ：`列表.sort(key=len)`, 如果想从大到小排序，就用 `列表.sort(key=len,reverse=True)`
3. 单独的排序函数：sorted(列表)
   1. sorted(数字列表, reverse=True) 数字列表从大到小排序
   2. sorted(字符串列表,key=len, reverse=True)字符串列表中元素长度从大到小排序

# 元组（tuple）
特点：元组是一个不可变的数据类型，不能对元组进行修改、删除、增加
用途：适合存储不应该被修改的数据

```python
# 定义空元组
tu = ()
print(tu, type(tu)) # ()  class=tuple

#元组中存放单个元素，元素后必须加逗号！🌟🌟🌟
tu1 = ('python')
tu2 = (15)
print(type(tu1), type(tu2)) # class = str , class = int, 当使用()包围单个数据时，并不是元组

tu3 = (15,)
print(tu3, type(tu3)) # (15,), class = tuple

```

1. 元组是有序的，所以可以进行索引和切片，同样也有正向索引（从左往右，从0开始）和负向索引（从右往左，从-1开始）
2. 元组也是可迭代对象，可使用for循环进行遍历


# 字典
概念：是一种可变数据，可以存放任意的数据类型，以键值对的形式存放 <br>
格式：dict = {键1:值1, 键2:值2}<br>
特点：字典以键值对存储、key的唯一性(如果是相同的key，新值会替换旧值)、key必须是不可变数据类型(数值型、字符串、元组)<br>

```python
# 定义空字典
dct = {}
dct1 = dict()

dct2 = {'name':'deng', 'age':18, 'sex':'男'}
# 通过key获取值
print(dct2['name'])
print(dct2['age'])
```

字典元素的查找
1. 通过key查找value: 字典[key]，如果用于查找的key在字典中不存在，则会报错 ： keyError
2. 字典.get(key)，如果用于查找的key在字典中不存在，不会报错，返回None
3. 字典.keys()，取出所有的key，返回的是可迭代对象，不是列表
4. 字典.values()，取出所有的values，返回的是可迭代对象，不是列表
5. len(字典)，获取字典中键值对的数量

字典元素的修改
1. 字典[旧key] = 新值，如果key不存在，会直接添加到字典中

字典元素的增加
1. 字典[新key] = 新值，一次只能添加一个值
2. 字典.update(可迭代对象) ，可以一次性添加多个值，可迭代对象中的元素以【键值对】的形式添加到字典中

```python

dct2 = {'name':'deng', 'age':18, 'sex':'男'}
dct2.update({'addr':'shenzhen','height':180})
print(dct2)
```

字典元素的删除
1. del 字典[key]   删除的key不存在就会报错
2. del 字典  这种就是直接把字典删除了
3. 字典.pop(key) 删除的key不存在也会报错
4. 字典.clear() 清除字典中的元素

字典成员运算符
1. 判断key是否存在字典中: `'key' in 字典` ， 结果是布尔值， 在删除字典元素时，不存在会报错，所以可以利用成员运算符判断元素是否存在，存在再删除
 
# 集合(set)
集合存放的是不可变数据类型的元素，可以存放不同类型的数据，是无序的不可重复的数据结构，所以不可以通过下标获取元素，每次输出的元素的顺序也可能不同，放入重复元素会自动去重<br>
格式：set = {元素1，元素2}，也是用大括号包围，但是不是键值对形式存放的

```python
# 注意！！！！！ 单纯的花括号不是集合，而是字典，被字典占用了 🌟🌟🌟
st = {}

st1 = set()

```
集合元素的操作：
1. 集合.add(元素)： 一次添加单个元素
2. 集合.update(可迭代对象)：一次添加多个元素，可迭代对象中的
3. 集合.remove(元素) 删除元素，元素不存在会报错
4. 集合.discard(元素) ，删除元素，元素不存在不会报错，不执行任何操作
5. `集合.pop()`:由于集合的无序性，该方法`删除元素是随机的`
6. 集合.clear()：清除集合中所有的元素

集合运算符：
1. & 交集：两个集合中相同的元素
2. ! 并集: 两个集合中所有不重复的元素
3. `-` 差集

```python
se1 = {11,55,56,23,78}
se2 = {55,77,96,23,88}
print(se1 & se2)   # {55, 23}
```



# 推导式
作用：从一个迭代对象中，通过简洁的语法生成新的序列结构的数据处理方式 <br>
Python 支持 4 种推导式： 列表推导式（List）、字典推导式(dict)、集合推导式(set)、生成器推导式(generator)

它们都是在 Python 中用于实现 映射（map）、过滤（filter）、重组（transform） 的简洁、高效工具。

推导式通用结构：
```css
结果表达式 for 变量 in 可迭代对象 [可选条件]
```
例如： --> 列表推导式
```python
data = [-9,-7,-5,-3,-1,0,1,3,4,5,6,7] # 列表

# 把列表中大于0的元素乘2然后放到新的列表中
#普通写法
new_data = []
for i in data:
    if i > 0:
        new_data.append(i * 2)
print(new_data) # [1, 3, 4, 5, 6, 7]

```
根据推导式拆解：
1. 结果表达式：`i * 2` -> 放到新列表中
2. 循环部分：`for i in data`
3. 过滤条件（可选）：`if i > 0` -> 过滤数据

```python
# 列表
data = [-9,-7,-5,-3,-1,0,1,3,4,5,6,7] 

# 推导式写法
new_data = [i * 2 for i in data if i > 0]
```
各推导式的语法 + 示例:
① 列表推导式（最常用）
```css
new_list = [表达式 for 变量 in 可迭代对象 if 条件]
```
示例：
```python
nums = []
squares = [x * x for x in range(10)]
evens   = [x for x in nums if x % 2 == 0]
```

② 字典推导式
```css
new_dict = {k,v for k,v in dict.items() if 条件}
```
示例：
```python
scores = {"tom": 88, "jerry": 59}
new_dict = {k:v for k,v in scores.items() if v >= 60}
```
用途： 重建字典、 过滤字典、 翻转 key→value、做映射表（数据清洗常用)

③ 集合推导式
```python

# new_set = {表达式 for x in 可迭代对象 if 条件 }
unique_lengths = {len(s) for s in ["aa", "bbb", "bb"]} # 将字符串长度放到新集合中，并将长度去重

```
用途： 生成集合（自动去重）、 快速构造去重数据

推导式的典型使用场景总结：

|  场景   | 示例  |
|  ----     | ----  |
| 映射（转换） | [x*x for x in nums] |
|过滤	|[x for x in nums if x > 0] |
|数据清洗	|{k: v.strip() for k,v in data} |
|去重	|{x for x in names} |
|文件读取|	[line.strip() for line in f if line.strip()] |
|扁平化	|[x for row in matrix for x in row] |
|大数据节省内存|	(x*x for x in huge_file) |

推导式不适用的情况（非常重要）🌟🌟🌟：
1. 逻辑太复杂（多层判断、多步骤）
2. 多行处理逻辑才清晰
3. 包含 try/except
4. 需要修改外部状态

**一句话总概：推导式是 Python 中表达“从一堆数据生成另一堆数据”的最佳方式。**

# 数据类型的相互转换

1. int(数据): 将数据转换为整数，数据要求是：整数、浮点数、被引号包围的整数
2. float(数据)：将数据转换为浮点数，数据要求是：整数、浮点数、被引号包围的整数、被引号包围的浮点数
3. bool(数据)：非零非空为True，为零为空为False
4. str(数据)：将数据转换为字符串，列表转换为字符串不是把元素组合起来，列表的中括号也会被转换进来
5. eval(str): 把字符串列表的引号去掉，把中间的内容作为python表达式执行
6. list()
7. tuple():
8. dict()：有多种格式，dict({(k1,v1),(k2,v2)})、dict(k1=v1,k2=v2)
9. set() ,转换为集合后，元素顺序是无序的
10. zip(可迭代对象1，可迭代对象2)，将多个可迭代对象中的元素取出放到元组中，再根据需要转换成指定的数据形式
```python
lst_num = [1,2,3]
lst_str = ['a','b','c']
dct = dict(zip(lst_str,lst_num))
print(dct)  # {'a': 1, 'b': 2, 'c': 3}

lst = list(zip(lst_str,lst_num))
print(lst) # [('a', 1), ('b', 2), ('c', 3)]

tup = tuple(zip(lst_str,lst_num))
print(tup) # (('a', 1), ('b', 2), ('c', 3))

st = set(zip(lst_str,lst_num))
print(st) # {('a', 1), ('b', 2), ('c', 3)}

# 注意，zip这个函数只会将这些可迭代对象中的能一一对应上的元素进行组合，对应不上的直接忽略掉
lst_num1 = [1,2,3,4,5]
lst_str1 = ['a','b','c']
dct1 = dict(zip(lst_str,lst_num))
print(dct1)  # {'a': 1, 'b': 2, 'c': 3}  ，多余的忽略掉

lst_num2 = [1,2,3]
lst_str2 = ['a','b','c','d','e','f']
dct2 = dict(zip(lst_str,lst_num))
print(dct2)  # {'a': 1, 'b': 2, 'c': 3}  ，多余的忽略掉
```


# 深拷贝 & 浅拷贝
深拷贝：指创建一个新的对象，并且递归的复制原对象中的所有元素<br>
浅拷贝：指创建一个新的对象，其内容是原始对象中元素的引用的拷贝，只是拷贝了引用并没有拷贝数据

不可变数据类型：数值型（int/float/boll/complex）、字符串（str）、元组（tuple）。修改数据时，数据所在地址一定会发生改变，定义新变量接受修改后的数据<br>
可变数据类型：列表(list)、字典(dict)、集合(set)，修改数据时，数据所在的地址不会变，不需要新变量接收修改后的数据，打印原变量就可以数据修改后的数据，就算用新变量接收这个修改后的列表，打印的是None

Java 与 Python 最大的不同点：`Java 的基本类型不是对象`<br>
Python：<br>
一切皆对象<br>
int，float，bool 都是对象（immutable不可变）<br>

Java：<br>
有基本类型（primitive type）：int, float, double, boolean...<br>
primitive 类型不是对象，不存在“可变 / 不可变”概念，它们是值存储在栈中。<br>
同时 Java 还有包装类（对象）：<br>
Integer、Double、Boolean → 这些是 immutable(不可变) 的<br>

| 类型       | Python             | Java                               |
| -------- |--------------------| ---------------------------------- |
| 数值类型     | 全是对象（immutable不可变） | primitive 不是对象；包装类是对象（且 immutable） |
| 字符串      | immutable          | immutable                          |
| 元组 tuple | immutable          | Java 无对应结构                         |
| 列表 list  | mutable (可变)       | ArrayList 是 mutable                |
| 字典 dict  | mutable            | HashMap 是 mutable                  |
| 集合 set   | mutable            | HashSet 是 mutable                  |

可使用`id(对象名)` 查看数据所在地址

```python

lst = [11,22,33]
lst2 = lst.append(44)

print(f'原始数据：{lst} 数据地址:{id(lst)}')  # 原始数据：[11, 22, 33, 44] 数据地址:2365203668096
print(f'修改后的数据：{lst2} 修改后的数据地址:{id(lst2)}') # 修改后的数据：None 修改后的数据地址:140732517739720
```

深浅拷贝语法：
1. 浅拷贝：copy.copy(数据),适用于简单对象，复制速度更快，占用空间更小
2. 深拷贝：copy.deepcopy(数据)，`注意！！！ 如果深拷贝的对象是不可变对象，那么就算拷贝了，数据内存地址也是一样的`

```python

import copy
lst = [11,22,33]
new_lst = copy.copy(lst)

print(f'原始数据：{lst} 数据地址:{id(lst)}') # 原始数据：[11, 22, 33, 44] 数据地址:2317185324672
print(f'浅拷贝的数据：{new_lst} 浅拷贝的数据地址:{id(new_lst)}') # 浅拷贝的数据：[11, 22, 33] 浅拷贝的数据地址:2318770167360

print(f'原始列表元素数据地址:{id(lst[0])}  {id(lst[-1])}') #原始列表元素数据地址:140732519212136  140732519212840
print(f'浅拷贝的列表元素数据地址：{id(new_lst[0])}  {id(new_lst[-1])}') # 浅拷贝的列表元素数据地址：140732519212136  140732519212840

# 所以可以看到，浅拷贝时，数据拷贝成功，并创建了新对象，打印了新对象的地址，但是原列表和拷贝后的列表的元素的地址都一致🌟🌟🌟

import copy
lst1 = [11,22,33,[44,55]]
new_lst1 = copy.deepcopy(lst1)

print(f'原始数据：{lst1} 数据地址:{id(lst1)}')
print(f'深拷贝的数据：{new_lst1} 深拷贝的数据地址:{id(new_lst1)}')

print(f'原始列表元素数据地址:{id(lst1[0])}  {id(lst1[-1])}')
print(f'深拷贝的列表元素数据地址：{id(new_lst1[0])}  {id(new_lst1[-1])}') 

#原始列表元素数据地址:140732519212136  2822649353024
#深拷贝的列表元素数据地址：140732519212136  2822650780864

# 这里可以看到，深拷贝的列表元素如果是不可变的（lst1[0]），数据地址就不会变；深拷贝的列表元素如果是可变的（lst1[-1]），数据地址就会变；

```


# 函数
1. 函数定义
```text
#函数定义
def 函数名():
    函数体代码
    
#函数调用
函数名()
```
2. pass占位符：使用pass占位符先搭建好框架，再去填充函数中的代码细节

```python
def func():
    pass
```
3. 函数注释：函数体中的第一行编写函数注释
```python
def func():
    """
    函数的注释内容
    :return: 返回值
    """
```
4. 函数的参数：函数名(变量1，变量2) ，这种叫形参
```python
def func(name, age):
    print(f'姓名:{name} 年龄:{age}')

func('张三', 18)
```
1️⃣ 位置参数：传入的实际参数需要根据形式参数的位置和个数进行创参，如果个数不一致报错，如果位置不一致输出的内容容易混淆，原因就是python的参数可以不用在定义的时候指定参数类型 <br>
2️⃣ 关键字参数：再调用函数时，不需要按照形式参数的位置来传参，但是个数还是要一致,实际就是将实际参数和形式参数绑定在一起 <br>
```python

def func(name, age):
    print(f'姓名:{name} 年龄:{age}')

func(age=18,name='张三')

```
3️⃣ 默认参数：在定义方法的时候，可以指定形式参数的默认值，再调用的时候也可以给这个形式参数传值，但是新值会覆盖默认值 <br>
```python

# 默认参数只能放在位置参数的后面，放前面会报错
def func(name, age=18):
    print(f'姓名:{name} 年龄:{age}')
    
# 下面的定义方式就会报错
def func( age=18, name):
    print(f'姓名:{name} 年龄:{age}')

func('dengchao') #直接使用默认值
func('dengchao', 28) # 覆盖默认值

```
4️⃣ 可变参数：定义函数时，传入的参数个数不确定, *args -> arguments -> 传入的数据以元组形式存放
```python
def func(*args):
    '''
    可变参数：数字求和
    :param args
    :return:
    '''
    print(f'数据内容:{args} 数据类型:{type(args)}')

func(11,22) # 数据内容:(11, 22) 数据类型:<class 'tuple'>
func(11,22,33) # 数据内容:(11, 22, 33) 数据类型:<class 'tuple'>
```

5️⃣ 可变关键字参数：使用 **kwargs 关键字，以字典的形式存储数据，使用起来更加灵活
```python
def func(**kwargs):
    print(f'数据内容:{kwargs} 数据类型:{type(kwargs)}')

func(name='dengchao') # 数据内容:{'name': 'dengchao'} 数据类型:<class 'dict'>
func(name='dengchao',age=18) # 数据内容:{'name': 'dengchao', 'age': 18} 数据类型:<class 'dict'>
```
5. 函数的返回值,如果返回为空或者没有返回值，直接打印不会报错，会打印None
```python
def func(num1, num2):
    return num1 + num2

res = func(1,2)
print(func(1,2))

```
1️⃣多个返回值，是以元组的形式存放的, 同时可以直接进行元组解包，就是定义与返回值相同数量的变量来接收返回值
```python
def func(num1, num2):
    return num1,num2,num1 + num2
# res = func(1,2)

# 返回值:(1, 2, 3) 返回值类型:<class 'tuple'>
# print(f'返回值:{res} 返回值类型:{type(res)}') 

# 元组解包，三个返回值，用三个变量去接
x, z, y = func(1, 2)
print(f'返回值:{x} {y} {z}') 

```

6. 函数变量的作用域
1️⃣ 函数内的局部变量只能在函数内使用，因为函数执行完后变量就会被销毁
2️⃣ 可以在函数内使用global关键字将局部变量声明为全局变量
```python

def func():
    global name
    name = '张三'
    
    print(f'函数内使用局部变量:{name}') # 函数内使用局部变量:张三

func()

print(f'函数外使用局部变量:{name}') # 函数外使用全局变量:张三

```
7. 嵌套函数, 下面有几个细节需要注意
```python
def out():
    
    name = '张三'
    print(f'函数内部使用变量：{name}')
    
    # 函数内部可以直接定义函数，并使用
    def inner():
        # 这里的name变量和上层的name变量同名，但是这个方法里面优先使用方法中定义的name变量，如果这个方法中没有定义就会找上层的name变量
        # 如果想要这里的修改对上层的name生效，可以使用nonlocal关键字
        # name = '李四'
        nonlocal name
        name = '李四'
        print(f'嵌套函数内部使用变量：{name}')
        
    inner()
        
    # inner方法中对name进行了重新赋值，但是inner方法中的name变量只属于inner方法，修改了也不会影响上层的同名变量
    print(f'函数内部使用变量：{name}')
    
out()

```

# 异常处理
语法格式：使用`try ... except ... `关键字

```python
try:
    被检测的代码块
except Exception as e: # 将错误提示信息存放到变量e中
    捕获到异常时的处理代码
else:
    未出现异常的处理代码
finally:
    一定会执行的代码
```
1. 常见的异常类型
基类Exception、ValueError（数据转换报错）、AttributeError（使用的方法不存在）等

2. 自定义异常
格式：raise Exception('错误提示信息')
```python
try:
    user = input('输入用户名：')
    if len(user) >= 20:
        raise Exception('用户名超长')
    else:
        print(f'用户名:{user}')
except Exception as e:
    print(f'异常:{e}')
```
3. 异常的传递：如果函数内部出现异常，异常会沿着调用链向上传递，直到被except捕获，如果没有捕获异常，程序会崩溃报错

# 模块
概念：一个简单的代码封装和重用机制。模块通常保存在一个.py文件中，每个文件定义一个模块，文件名就是模块名<br>
分类：
1. 内置模块
```python
import copy
# copy模块
# 深拷贝
copy.deepcopy()
# 浅拷贝
copy.copy()

# math模块
math.pi
# 向上取整 
math.floor()
# 向下取整 
math.ceil()

# random模块
import random
print(random.uniform(1,5)) # 获取1-5的随机数，带随机小数
print(random.randint(1,5)) # 获取1-5的随机整数，[1,5]

# string模块
import string
print(string.digits) # 0-9的十进制数字
print(string.ascii_letters) # 所有大小写字母
print(string.ascii_lowercase) # 所有小写字母
print(string.ascii_uppercase) # 所有大写字母

```

