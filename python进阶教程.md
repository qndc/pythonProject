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