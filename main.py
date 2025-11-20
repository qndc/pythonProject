# 这是一个示例 Python 脚本。


# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    # print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按装订区域中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助


#输出函数，可以一次输出多个值，可以使用sep指定分隔符
# print("一","二","三",sep= '|')

#end的用法是在输出了hello 后拼接 1，然后再输出第二个hello，再拼接 2
# print("hello", end= "1")
# print("hello", end= "2")
# print("hello", end= "3")

# python定义变量时不需要指定明确的变量类型，同一个变量可以多次赋值，并且可以是不同类型的值，不会重新开辟空间，而是直接修改值
# a = 1
# print(a)
#
# a = 66.6
# print(a)
#
# a= "hello"
# print(a)

# 数值类型：int-整数, float-浮点类型, bool-布尔类型
# bool(1) # 将数字转换为bool值,1-True/0-False，注意bool值的True和False都是首字母大写的
# print(True+1)  #bool值也是可以直接参与计算的
# print(False+1)

# complex-复数,就是复杂的数字类型
# #格式：a +bj
# com = 5+6j
# print(com) # 打印结果(5+6j)

# 字符串类型 -- str，就是被引号包围的数据
# name = 'zhangsna'

# 注意：数值型不需要加引号，加了引号就变成字符串了



#==================================占位符 ===================================
# %d 给整数占位
# %f 给浮点数占位，如果小数点后没有6位，会自动用0补全6为小数
# %s 给字符串占位，除此之外也是通用占位符，既可以给字符串占位，还可以给整数浮点数占位，但是给浮点数占位，小数点后不会补齐
# age = 18
# print("姓名：%s 年龄：%d" % (name, age)) #这里需要用%进行连接，并且多个参数用小括号包起来，这里和java里面不一样，java是逗号分隔
# print("姓名: %s" % name) #如果只有一个参数，不需要用小括号包起来，但是%是必须的

#=================================f表达式 格式化输出 =========================
# 前提：python 3.6及以上的版本
# 格式：print(f"{变量名}")，并且也可以直接在大括号里面对变量直接运算
# print(f"{name}")
#
# num = 14.987221
# print("% .2f" % num)
#
# print(f"{num:.2f}")

# score = input('请输入分数：')
# print(score)
# print(type(score))

# # 这里打印的不是True，而是2，因为and是全为真才是真，所以会比较到2这个位置，此时比较完了，是真，所以打印2
# print(10 and 2)
# # 这里同理，10是真，还是会比较到0这个位置，发现是假，就返回0
# print(10 and 0)
#
# # 这里的or就是或，一真即真，比较到10为真，就直接打印了10
# print(10 or 0)
# # 这里比较0为假，但是后面还有数，所以会比较10，为真，所以打印10
# print(0 or 10)
#
# #这个就更形象了，由于是and，所以这里比较了15 比较10 ，然后比较到了0，此时为假就结束了，打印了0
# print(15 and 10 and 0 and None)

# if num > 15:
#     if num > 20:
#         print("大于20")
#     else:
#         print("15到20之间")
# elif num == 15:
#     print("等于15")
# else:
#     print("小于15")

# for i in range(1,10):
#     print(f"{i}")

# str = 'hello'
# print(f'{str[0]}')
# print(f'{str[-5], str[-1]}')
#
# print(f'{str[0:2]}')
#
# print(f'{str[len(str)-1]}')
#
# print(f'{str[::-1]}')
#
#
# str = 'hello world study python'
#
# print(str.split(' ',1))
#
# print(str.replace(' ','|',1))

# num = '12'
# print(num.isdigit())

# print(len(str))

lst = [100,101.1,'test', True]
# print(len(lst))
#
# print( 666 in lst)
# print(666 not in lst)
#
# for i in lst:
#     if isinstance(i, str):
#         print(i)

# lst.extend('python')
# print(lst)
#
# lst2 = [100,101.1,'test', 100,True,100]
# print(lst2)
# cnt = lst2.count(100)
# for i in range(cnt):
#     lst2.remove(100)
# print(lst2)
#
#
#
# dct2 = {'name':'deng', 'age':18, 'sex':'男'}
# dct2.update({'addr':'shenzhen','height':180})
# print(dct2)
#



data = [-9,-7,-5,-3,-1,0,1,3,4,5,6,7] # 列表

# 把列表中大于0的元素乘2然后放到新的列表中
#普通写法
# new_data = []
# for i in data:
#     if i > 0:
#         new_data.append(i * 2)
# print(new_data)
#
#
# new_data1 = [i * 2 for i in data if i > 0]
# print(new_data1)


se1 = {11,55,56,23,78}
se2 = {55,77,96,23,88}
print(se1 & se2)