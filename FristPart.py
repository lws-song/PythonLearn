# 单行注释（#之后要有空格 这是规范）

"""
python.org
www.jetbrains.com

shift + Ctrl + Alt + 鼠标左键拖动
Alt + 鼠标左键拖动

多行注释
print(666)
print(13.14)
print("黑马程序员")

# 定义一个变量，用来记录钱包的余额
money = 50
print("钱包还有：", money)

# 买了一个冰淇淋 花了10快
money = money - 10
print("现在还剩余：", money, "元")

# 假设，每隔一小时，输出一下钱包余额  ctrl + d  复制
print("现在是下午1点，钱包余额剩余：", money)
print("现在是下午2点，钱包余额剩余：", money)
print("现在是下午3点，钱包余额剩余：", money)


type() 查看数据类型 type(变量)
# 方式1，使用print直接输出类型信息
print(type("黑马程序员"))
print(type(666))
print(type(11.345))

# 方式2， 使用变量存储type()语句的结果
string_type = type("哈哈哈哈")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)

方法3，使用type()语句，查看变量中存储的数据类型信息
name = "哈哈哈"
name_type = type(name)
print(name_type)


数据类型的转换
int(x)
float(x)
str(x)
# 将数据类型转换为字符串
num_str = str(11)
print(type(num_str), num_str)


标识符：
    给所使用的一系列变量，类，方法等命名
    英文
    中文
    数字 (不用在开头)
    下划线(_)
    大小写是可以区分的，关键字不可用于作为标识符
    变量命名规范：见面起意、下划线把不同单词分开、英文字母全部小写

算数(数学)运算符：
    // 取整除
    %  取余
    ** 指数

字符串在python中有多种定义方式
1.单引号定义法 name = '哈哈哈'
2.双引号定义法 name = "哈哈哈"
3.三引号定义法 name =
三引号定义法，和多行注释的写法一样，同样支持换行操作
使用变量接受他，它就是字符串
不用变量接受它，就是作为多行注释使用

字符串的嵌套：
  1.使用反斜杠来转义
  2.单引号内可以使用双引号或者双引号内可以写单引号号
  Name = '"哈哈"'
  name = "'哈哈'"
  print(Name)  "哈哈"
  print(name)  '哈哈'
  转义字符的使用
  name = "\"黑马\""
  print(name)
  输出"黑马"

使用+号连接字符串变量或字符串字面量即可
无法和非字符串类型进行拼接
name = "我家"
address = "在中国"
print("我是:" + name, "我家在:" + address)

字符串格式化：
name = "哈哈哈"
message = "我喜欢%s" % name
其中的 %s
% 表示：我要占位
s 表示：将变量变成字符串放入占位的地方
d 表示：将变量变成整数放入占位的地方
f 表示：将变量变成浮点数放入占位的地方

class_num = 57
avg_salary = 11243
message = "班级人数为%s，毕业的平均工资为%s" % (class_mun,avg_salary)
print(message)

字符串格式化 - 数字精度控制
· m 控制宽度，要求是数字（很少使用），设置的宽度
    小于数字本身，不生效
· .n 控制小数点精度，要求是数字，会进行小数的四舍五入
小数点算一位
%5d:表示将整数的宽度控制在5位，如数字11，变成【空格】【空格】【空格】11
%5.2: 表示将宽度控制为5，将小数点精度控制为2
      11.345 在 %7.2 后 变为 【空格】【空格】11.35
%.f: 表示不限制宽度，只设置小数点精度为2，11.345 变为 11.35

快速格式化
# 通过语法： f"内容{变量}"的格式来快速格式化
         f"{占位}"
name = "刘伟松"
set_up_year = 2000
stock_price = 1919
print(f"我是{name}, 我成立于{}，我今天的工资是{stock_price}.")

print("1 * 1的结果是：%d" % (1*1))
print(f"1 * 1结果是{1 * 1}")
print("字符串在python中的类型是：%s" % type('字符串'))

----------计算股票小程序-----------
name = "刘氏集团"
stock_price = 19.19
stock_code = "16168"
stock_price_daily_growth_factor = 1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days
print(f"公司：{name},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数 %.2f,经过%d天的增长，股价到达了：%.2f" % (stock_price_daily_growth_factor,growth_days,finally_stock_price))
--------------------------------

获取键盘输入
input() 默认接受的是字符串
name = input("告诉我你还是谁？\n请输入：")
print("我知道了！你是:%s" % name)

bank_code = int(input("告诉我你的银行卡的密码？\n请输入："))
print("我知道了！\n你的密码是:%d" % bank_code)

python 判断语句
布尔类型不仅可以通过定义得到，也可以通过比较运算符进行内容比较得到
result1 = 10 > 5
result2 = "123" == "456"
print(f"10 > 5 的结果是：{result1}，类型是：{type(result1}")
print(f"字符串123是否与字符串456相等，结果是：{result2}，类型是：{type(result2}")


if 要判断的条件:         严格符合缩进原则
    条件成立时，要做的事情
age = int(input("输入你的年龄：\n"))
if age > 18:
    print("你已经成年了！")
elif (age >= 0 || age <= 18):
    print("你还没有成年噢！")
else:
    print("输入格式错误！")

import random
num = random.randint(1,10)
num1 = 0
while 1:
    num1 += 1
    if int(input("输入你猜的数字：")) == num:
        print("你猜对了！")
        break
    elif num1 == 5:
        print("你已经猜了5次了，out!")
        break
    else :
        print("你猜错了！再来一次吧！")

print("Hello", end='')  输出不换行
print("World", end='')
/t 制表符 相当与Tab键

输出九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j} * {i} = {j * i}\t", end='')
        j += 1
    i += 1
    print()

for 临时变量 in 待处理数据集:
    循环满足条件时执行的代码
for循环是将字符串的内容：依次取出
所以for循环也被称为：遍历循环
* 理论上讲，python的for循环无法实现无线循环（被处理的数据不可能无限大）
遍历字符串：
name = "abcd"
for x in name:
    print(x)
输出：
a
b
c
d

sum = 0
name = "abc is a brand of cast"
for x in name:
    if x == "a":
        sum += 1
print(f"name中一共有{sum}个a")

range语句：
1.range(num)
    获取一个从0开始，到num结束的数字序列（不含num本身）
    如，range(5)取得的数据是;[0,1,2,3,4]
2.range(num1,num2)
    获得一个从num1开始，到num2结束的数字序列（不含num2本身）
    如，range(5,10),取得的数据是：[5,6,7,8,9]
3.range(num1,num2,step)  step是步长
    获得一个从num1开始，到num2结束的数字序列（不含num2本身）
    数字之间的步长，以step为准(step默认为1)
    如,range(5,10,2)取得的数据是：[5,7,9]

函数：
    是组织好的，可重复使用，是用来实现特定功能的代码段
    函数必须先定义，后使用

def 函数名(传入参数):
    函数体
    return 返回值

def add(x,y):
    print(f"{x} + {y}相加的结果是：{x + y}")
函数定义中的参数，称之为形式参数
函数调用中的参数，称之为实际参数
函数的参数数量不限，使用逗号分开

def add(a, b):
    result = a + b
    return float(result)

num = add(1, 2)
print(f"返回的东西是{num},返回的数据类型是{type(num)}")

None 类型
def  my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度是{count}")
str1 = "abcdefg"
result = my_len(str1)  # 结果是None
print(type(result))    # 结果<class NoneType>

在if判断中，None等同于False
一般用于在函数中主动放回None，配合if判断做相关处理
def check_age(age):
    if age > 18:
        return "SUCCESS"
result = check_age(16)
if not result:
    print("未成年！")

#None用于声明无初始值内容的变量

局部变量
全局变量
global关键字:
    可以在函数内部声明变量为全局变量

def main():
    return input("输入你想要办理的业务代码：")
code = main()
print(code)

数据容器：
一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素
每一个元素，可以是任意类型的数据，如字符串，数字，布尔等

数据容器的不同，特点也不同：
* 是否可以重复元素
* 是否可以修改
* 是否有序
分为5类：
列表（list），元组（tuple），字符串（str），集合（set），字典（dict）

列表：
· 可以容纳多个元素（2**63 - 1）
· 可以容纳不同类型的元素（混装）
· 数据是有序存储的
· 允许重复数据存在
· 可以修改

# 字面量
[元素1,元素2,元素3,.......]

# 定义变量
变量名称 = [元素1,元素2,元素3........]

# 定义空列表
变量名称 = []
变量名称 = list()

name_list = ['Tom', 'Lily', 'Rose']
print(name_list[-1])  # 结果为：Rose

my_list = [[1,2,3], [4,5,6]]
print(my_list[0][0])  #1

列表的方法：
回忆：函数是一个封装的代码单元，可以提供特定的功能
    在Python中，如果将函数定义为class（类）的成员，那么函数会
    称之为：方法
1.查找某元素的下标：       列表.index(元素)   如果找不到，报错ValueError
2.修改特定位置（元素）的值： 列表[下标] = 值
3.插入元素：              列表.insert(下标,元素)
4.追加单个元素到列表的结尾：  列表.append(元素)
5.追加一批元素：           列表.extend(其他数据容器)
6.删除元素：              del 列表[下标]
                        列表.pop(下标)
  删除某元素在列表中的第一个匹配项：
                        列表.remove(元素)
  清空列表内容:            列表.clear()
7.统计列表内某元素的数量      列表.count(元素)
8。统计列表中的所以元素的数量： len(列表)

元组（tuple）：
元组里面元素不可修改！但有个特例，如果元组里面嵌套了列表，可以修改内部list的元素
使用小括号，数据可以是不同的数据类型
t1 = (1, 'Hello', True)
t2 = ('Hello',)         只有一个元素的时候后面要有一个单独的逗号
t3 = tuple()
t4 = ((1,2,3),(4,5,6))
num = t4[1][2]     # 6
index()
count()
len()
print(f"t1中一个有{len(t1)}个元素")

字符串：
· 只可以存储字符串
· 长度任意
· 支持下标索引
· 允许重复字符串的存在
· 不可以修改(增加或删除元素等)
· 支持for循环

修改指定下标的字符  字符串[0] = 'a'
移除特定下标的字符  del 字符串[0]  字符串.remove()  字符串.pop()
追加字符等         字符串.append()
字符串的替换：      字符串.replace(字符串1, 字符串2)
                将字符串中的所有字符串1替换为字符串2
                注意：不是修改字符串本身，而是得到一个新的字符串哦
字符串的分割：     字符串.split(分割符字符串)
                按照什么来切分
字符串的规整操作（去前后的空格） 字符串.strip()
s1 = "  hhh hhh hhh  "
print(s1.strip())      #结果"hhh hhh hhh"
字符串的规整操作（去前后指定字符串） 字符串.strip(字符串)
s2 = "12hhh hhh hhh21"
print(s2.strip("12"))  #结果"hhh hhh hhh"
注意：传入的是“12”，其实就是：“1”和"2"都会移除，是按照单个字符
    满足两个中的任意一个，就会被移除
统计字符串中某字符串的出现次数，count
    s1.count("hhh")
统计子符串的长度：  len(字符串)

序列
序列的常用操作 - 切片
序列支持切片，即：列表，元组，字符串，均支持进行切片操作
切片：从一个序列中，取出一个子序列

序列[启示下标:结束下标:步长]
    起始下标可以留空，留空视作从头开始
    结束下标可以留空，留空视作到尾结束
    步长：依次取元素的间隔
    步长N，每次跳过N-1个元素取
    步长为负表示，反向取（起始下标和结束下标也要反向标记）

my_str = "哈哈哈哈,计算机技术哎,python"
print(my_str[9:4:-1])   # 计算机技术
print(my_str.split(",")[1].replace("哎", "")[::-1])
split之后是列表

set(集合): {}
集合无序，所以集合不支持：下标索引访问
和其他三个容器相比，最大的特点是 不支持重复，自带自动去重功能
但集合和列表一样，是允许修改的
{元素1,元素2,元素3,.......}
变量名称 = {元素1,元素2,元素3........}
变量名称 = set()

1. 添加： 集合.add(元素)
2. 移除： 集合.remove(元素)
3. 从集合中随机取出元素:   集合.pop()
4. 清空集合     集合.clear()
5. 取出2个集合的差集： 得到一个新集合，集合1和集合2不变
                集合1.difference(集合2)
6. 消除2个集合的差集:  在集合1内，删除和集合2相同的内容
                集合1.difference_update(集合2)
7. 2个集合合并     得到新集合，集合1和集合2不变
                集合1.union(集合2)
8. 统计集合数量len()
9. 集合的遍历：      集合不支持下标索引，不能用while循环
                可以用for
set = {1,2,3,4,5}
for element in set1:
    print(f"集合的元素有：{element}")


字典  key:Value
可以通过 Key，取到对于的 Value
{key: value, key: value, key: value,.......}
变量名称 = {key: value, key: value, key: value........}
变量名称 = {}
变量名称 = dict()
{"王思聪": 99, "王健林": 100}
但是：{"王思聪": 99, "王思聪": 89, "王健林": 100}
后者会覆盖前者，key不可以重复

1，从字典中基于key获取value
my_dict1 = {"王思聪": 99, "王健林": 100}
score1 = my_dict1["王思聪"]
score2 = my_dict1["王健林"]
print(f"王思聪的考试分数是：{score1}")
print(f"王健林的考试分数是：{score2}")

2.字典的嵌套：
stu_score_dict = {
    "王力宏": {
        "语文": 134
        "数学": 134
        "英语": 99
    }
    "周杰伦": {
        "语文": 123
        "数学": 145
        "英语": 99
    }
    "林俊杰": {
        "语文": 133
        "数学": 145
        "英语": 111
    }
}

3.从嵌套的字典获取数据
score = stu_score_dict["周杰伦"]["语文"]

新增元素和更新元素一样：
    字典[Key] = Value
元素的删除：字典.pop(Key)
清空字典    字典.clear()
获取全部的key：
my_dict = {"王思聪": 99, "王健林": 100, "刘德华": 100}
keys = my_dict.keys()
for key in keys:
    print(f"字典的key是：{key}", end="\t", )
    print(f"字典的value是：{my_dict[key]}")
统计字典内的函数数量：len()
支持for 不支持while

列表： 可修改，可重复的一批数据纪录场景
元组： 不可修改，可重复的一批数据记录场景
字符串：一串字符的记录场景
集合： 不可重复的数据场景
字典：  以key检索Value的数据记录场景

max()最大元素
min()最小元素
sorted()排序 之后标为列表对象
{sorted(my_list), reverse=True} (反向排序)
容器的通用容器转换：
list(容器)
str(容器)、
tuple(容器)
set(容器)

字符串的大小比较
用码值比较  a是97  A是65
字符串是按位比较，也就是一位位进行比对，只要有一位大，那么整体就大
'abc' > 'abb'  'a' < 'ab'


Python 函数进阶
多个返回值：
def test_return():
    return 1, "hello", True
x, x = test_return()
print(x)
print(y)

缺省参数（默认参数）：注意：设置默认值，必须统一的在最后
def user_info(name, age, gender='男')、
    print(f"你的名字是{name}，你的年龄是{age}，你的性别是{gender}")
user_info('小王', 11)   不传gender的话，默认gender=为“男”
user_info('小美', 12, '女')

不定长 - 位置不定长 ，*号
def user_info(*args):   # 传进的所有参数（无限的）都会被args变量收集，他会根据
    print(args)           传进参数的位置合并为一个元组(tuple)，args
                          是元组类型，这就是位置传递
      -  关键字传递不定长 ，**号
def user_info(**kwargs): 参数是“键=值”的形式，所有的“键=值”都会被kwargs接受
    print(kwargs)        同时会根据“键=值”组成字典，类型是字典
user_info(name='Tom', age=18, id= 110)

匿名函数：
1，函数作为参数传递
def test_func(compute):
    result = compute(1, 2)
    print(result)
def compute(x, y)
    return x + y
test_func(compute)
这是一种计算逻辑的传递（代码的执行逻辑），而非数据的传递

在函数定义中：
    def关键字，可以定义带有名称的函数
    lambda关键字，可以定义匿名函数（无名称）
有名字的函数，可以基于名称重复使用
无名称的匿名函数，只可以临时使用一次

匿名函数定义语法：
    lambda 传入参数: 函数体（一行代码）
lambda是关键字，表示定义匿名函数
函数体，就是函数的执行逻辑，要注意：只能写一行代码，无法写多行代码
def test_func(compute):
    result = compute(1, 2)
    print(result)
test_func(lambda x, y: x + y)


闭包
在函数嵌套的前提下，内部函数使用了外部函数的变量，并且外部函数返回了内部函数
这个使用外部函数变量的内部函数称为为闭包

def outer(logo):

    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn1 = outer("黑马程序员")
fn1("大家好呀")
fn2("快快快")

fn2 = outer("教育")
fn2("IT")
fn2("快快快")3

# 使用nonlocal关键字修改外部函数的值

def outer(num1):

    def inner(num2):
        nonlocal num1
        num1 += num2
        print(num1)

    return inner

fn = outer(10)
fn(10)  # 20
fn(10)  # 30
fn(10)  # 40
fn(10)  # 50
# 就可以实现内部函数依赖外部变量，而外部变量又是外层函数的内部临时变量
# 通过嵌套的方式实现了不断的记录值，同时又确保了外部变量不是全局的，不会被篡改
# 无需定义全局变量即可实现通过函数，持续的时间、修改某个值
# 但是是：由于内部函数持续应用外部函数的值，所以会导致这一部分的内存空间
# 不被释放，一直占用内存、


装饰器
装饰器其实就是一种闭包，其功能就是在不破坏目标函数原有的代码和功能的前提
下，为目标函数增加新功能
装饰器的一般写法(闭包写法)：
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")
    return inner

def sleep():
    import random
    import time
    print("睡眠中........")
    time.sleep(random.randint(1, 5))
fn = outer(sleep)
fn()

# ----装饰器的快捷写法(语法糖)
def outer(func):
    def inner():
        print("我要睡觉了")
        func()
        print("我起床了")

    return inner

@outer
def sleep():
    import random
    import time
    print("睡眠中........")
    time.sleep(random.randint(1, 5))

sleep()

设计模式：
设计模式是一种编程套路，可以极大的方便开发，我们称之为设计模式：
最常见、最经典的设计模式就是面向对象
除了面向对象外，编程中也有很多的套路可以方便开发，称之为设计模式
· 单例、工厂模式
· 建造者、责任链、状态、备忘录、访问者、观察者、中介、模板、代理模式
· 等等模式

单例模式是一种常用的软件设计模式，该模式的主要目的是确保某一个类只用一个
实例存在
在这系统中，某个类只有一个实例时，单例对象就能派上用场
· 定义： 保证一个类只有一个实例，并提供一个访问它的全局访问点
· 使用场景： 当一个类只能又一个实例，而客户可以从一个众所周知的访问点访问它时
# 在一个格外的文件中
class strTools:
    pass

str_tool = StrTools()
# 在文件中导入包
from test import str_tool
s1 = str_tool
s2 = str_tool
print(s1)
print(s2)
此时s1和s2的内存地址一样

# 工厂模式
class Person:
    pass
class Worker(Person):
    pass
class Teacher(Person):
    pass
class Student(Person):
    pass

class Factory:
    def get_person(self, p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 't':
            return Teacher()
        else p_type == 's':
            return Student()

factory = Factory()
worker = factory.get_person('w')
tch = factory.get_person('t')
stu = factory.get_person('s')
# 创建大批量对象的时候又统一的入口，易于代码维护
# 当发生修改的时候，仅修改工厂类的创建方法即可


# 多线程并行执行概念
操作系统中可以运行多个进程，即多任务运行
一个进程内可以运行多个线程，即多线程运行
# 多线程编程
threading模块： Python的多线程可以通过threading模块来实现
import threading

thread——obj = threading.Thread([group [, target [, name [, args [, kwargs]]]]])
- group : 暂时不用，未来功能的预留参数
- target : 执行的目标任务名
- args : 以元组的方式给执行任务传参
- kwargs : 以字典方式给执行任务传参
- name : 线程名， 一般不要设置

# 启动线程，让线程开始工作
thread_obj.start()

import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)

def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing, args=("我要唱歌，啦啦啦！", ))
    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dance, kwargs={"msg": "我要跳舞，呱呱呱！"})

    # 进程干活
    sing_thread.start()
    dance_thread.start()


# Socket服务端开发
2个进程之间通过Socket进行相互通讯，就必须有服务端和客户端
Socket服务端: 等待其他进程的连接、可接受发来的消息、可以回复消息
Socket客户端： 主动连接服务端、可以发送消息、可以接受回复
1. 创建socket对象
import socket
socket_server = socket.socket()

2. 绑定socket_server到指定IP和地址
socket_server.bind((host, port))

3. 服务端开始监听端口
socket_server.listen(backlog)
# backlog为int整数，表示允许的连接数量，超出的会等待，可以不填，
不填会自动设置一个合理值

4. 接收客户端连接，获得连接对象
conn, address = socket_server.accept()
print(f"接收到客户端连接，连接来自：{address}")
# accept方法是阻塞方法，如果没有连接，会卡在当前这一行不向下执行代码
# accept返回的是一个二元元组，可以使用上述形式，用两个变量接收二元元组的2个元素

5. 客户端连接后，通过recv方法，接收客户端发送的消息
while True:
    data = conn.recv(1024).decode("UTF-8")
    # recv方法的返回值是字节数组(Bytes)，可以通过decode使用UTF-8
    解码为字符串
    # recv方法的传参是buff size，缓冲区大小，一般为1024即可
    if data == 'exit'
        break
    print("接收到发送来的数据", data)
# 可以通过while True无限循环来持续和客户端进行数据交互
# 可以通过判定客户端发来的特殊标记，如exit 来退出无限循环

6. 通过conn(客户端当次连接对象)，调用send方法可以回复消息
conn.send("你好，哈哈哈哈".encode("UTF-8))

7. conn(客户端当次连接对象)和socket_server对象调用close方法，关闭连接
import socket
socket_server = socket.socket()
socket_server.bind(("localhost", 8888))
socket_server.listen()
# result: tuple = socket_server.accept()
# conn = result[0]
# address = result[1]
conn, address = socket_server.accept()
print(f"接收到了客户端的连接，客户端的信息是: {address}")
while True:
    data: str = conn.recv(1024).decode("UTF-8")
    print(f"客户端发来的消息是： {data}")
    msg = input("请输入你要和客户端回复的信息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))
conn.close()
socket_server.close()


# socket客户端编程
import socket
socket_client = socket.socket()
socket_client.connect(("localhost", 8888))
while True:
    send_msg = input("请输入要发送的消息：")
    if send_msg == 'exit':
        break
    socket_client.send(send_msg.encode("UTF-8"))
    recv_data = socket_client.recv(1024)
    # recv方法是阻塞式的，即不接收到返回，就卡在这里等待
    print("服务端回复的消息为：", recv_data.decode("UTF-8"))
socket_client.close()

正则表达式
又称之为：规则表达,是使用单个字符串来描述、匹配某个句法规则的字符串
常被用来检索，替换那些符合某个模式(规则)的文本，验证字符串是否匹配
比如：
# (^[\w-]+(\.w-)+)*@[\w-]+(\.[\w-]+)+$)
即可匹配一个标准邮箱格式

Python正则表达式，使用re模块，并基于re模块中三个基础方法来做正则匹配
分别是: match、 search、 findall三个基础方法

· re.match(匹配规则, 被匹配字符串)
只匹配头部字符串
import re
s = 'python is the best language'
result = re.match('python', s)
print(result)  # <re.Match object; span=(0, 6), match='python'>
print(result.span())   # (0. 6)
print(result.group())  # python

s = 'ipython is the best language python'
result = re.match('python', s)
print(result)       # None

· re.search(匹配规则, 被匹配字符串)
搜索整个字符串,找出匹配的.从前到后,找到第一个后,就停止,不会继续向后
s = 'ipython6666777jokerJoker'
result = re.search('python', s)
print(result)   # <re.Match object; span=(1, 7), match='python'>
print(result.span())  # (1, 7)
print(result.group)   # python

s = 'joker666'
result = re.search('python', s)
print(result)   #None

· re.search(匹配规则, 被匹配字符串)
匹配整个字符串，找出全部匹配项
s = '1python666joker666python'
result = re,findall('python', s)
print(result)   # ['python', 'python']

找不到返回空的list:[]
s = '1666joker777year777'
result = re.findall('python', s)
print(result)         # []

元字符匹配
单字符匹配
.:   匹配任意1个字符(除了\n),  \. 匹配点本身
[]:  匹配[]中列举的字符
\d:  匹配数字, 即 0~9
\D:  匹配非数字
\s:  匹配空白,即空格,tab键
\S:  匹配非空白
\w:  匹配单词字符， 即a~z， A~Z，0~9， _
\W:  匹配非单词字符

示例:
字符串  s = ”joker @@python2 !!666##joker3“
· 找出全部数字: re.findall(r'\d', s)
字符串的r标记，表示当前字符串是原始字符串，即内部的转义字符无效而是普通字符
· 找出特殊字符
re.findall(r'\W', s)
· 找出全部英文字母
re.findall(r'a-zA-Z', s)
[]内可以写：[a-zA-Z0-9]这三种范围组合或
指定单个字符如[aceDFG135] # 找出所有的a，c，e，D，F，G，1，3，5

数量匹配:
* ： 匹配前一个规则的字符出现0至无数次
+ ： 匹配前一个规则的字符出现1至无数次
？：  匹配前一个规则的字符出现0次或1次
{m}： 匹配前一个规则的字符出现m次
{m.}：  匹配前一个规则的字符出现最少m次
{m,n}：  匹配前一个规则的字符出现m到n次

边界匹配：
^ : 匹配字符串开头
$ : 匹配字符串结尾
\b: 匹配一个单词的的边界
\B: 匹配非单词边界

分组匹配：
|: 匹配左右任意一个表达式
(): 将括号中字符作为一个分组

# 匹配一个账号,只能由字母和数字组成，长度限制6到10位
r = '^[0-9a-zA-Z]{6,10}$'
# 若要判断字串，则^和$不用写，若要匹配全部，则就要写
s = "1234556678888"  # []
s = "1234567"    # [1234567]
print(re.findall(r, s))

# 匹配QQ号，要求纯数字, 长度5-11，第一位不为0
r = "^[1-9][0-9]{4,10}$"
s = "123456"   # [12345]
s = "0123444"  # []

# 邮箱
# abc.efg.hij@qq.com.cn.eu
# abc@qq.com
import re
r = '^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]*)+$'
s = "a.b.c.b@qq.com.eu"
print(re.findall(r, s))

import re
r = '(^[\w-]+(\.[\w-]+)*@(qq|163|gmail)(\.[\w-]*)+$)'
# findall的话，如果字符串又分组，就会把每个分组的内容输出，若要输出所有，就要在整体加上()
s = "a.b.c.b@qq.com.eu"
print(re.findall(r, s))



递归
import os

def test_os():
    # 演示os模块的3个基础方法
    print(os.listdir("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest"))
    显示DGtest中的目录
    print(os.path.isdir("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest/a"))
    判断a是否是一个文件夹
    print(os.path.exits("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest"))
    判断是否有DGtest的路径

def get_files_recursion_from_dir(path):
    从指定的文件夹中使用递归的方法，获取全部的文件列表
    :param path: 被判断的文件夹
    :return: list. 包含全部的文件夹，如果目录不存在或者无文件就返回一个空list
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}，不存在")
        return []

    return file_list


if __name__ == '__main__':
    print(get_files_recursion_from_dir("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest"))
"""
import os


def test_os():
    # 演示os模块的3个基础方法
    print(os.listdir("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest"))
    # 显示DGtest中的目录
    print(os.path.isdir("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest/a"))
    # 判断a是否是一个文件夹
    print(os.path.exists("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest"))
    # 判断是否有DGtest的路径


def get_files_recursion_from_dir(path):
    # 从指定的文件夹中使用递归的方法，获取全部的文件列表
    """
    :param path: 被判断的文件夹
    :return: list. 包含全部的文件夹，如果目录不存在或者无文件就返回一个空list
    """
    file_list = []
    if os.path.exists(path):
        for f in os.listdir(path):
            new_path = path + "/" + f
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)
    else:
        print(f"指定的目录{path}，不存在")
        return []

    return file_list


if __name__ == '__main__':
    test_os()
    print(get_files_recursion_from_dir("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/DGtest"))
