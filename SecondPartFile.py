"""
Python 文件操作
文件编码:翻译为计算机认识的0/1
文件的操作文件：打开，读写，关闭
在python中，使用open函数，可以打开一个已经存在的文件，或者创建一个新文件
open(name,mode,encoding)
name: 是要打开的目标文件名的字符串（可以包含文件所在的具体路径）
mode: 设置打开文件的模式（访问模式）：只读，写入，追加等
encoding: 编码格式（推荐使用UTF-8）
例子：
f = open('python.txt','r',encoding="UTF-8")
# encoding 的顺序不是第三位，所以不能用位置参数，用关键字参数直接指定
r: 以只读方式打开文件，文件的指针将会放在文件的开头，这是默认方式
w: 打开一个文件只用于写入，如果该文件已存在则打开文件，清空原有文件内容并从开头开始编辑，
    原有内容会被删除，如果该文件不存在，创建新文件
a： 打开一个文件用于追加。如果该文件已存在，新的内容将会被写道已有的内容中
    如果该文件不存在，创建新文件进行写人

read()方法:   如果连续使用read,第二次read从第一次read后面开始读
    文件对象.read(num)
    num表示要从文件中读取的数据得分长度(单位是字节)，如果没有传入num
    那么就表示读取文件中所有的数据
# read lines()方法  （之间无空格）  和read一个道理，也会接read后面的指针
read lines可以按照行的方式，把整个文件中的内容进行一次性读取，并且返回
    的是一个列表，其中每一行的数据为一个元素
# readline()方法，与read lines相比只调用一行

for循环读取文件行
for line in open("D:/test.txt", "r")
    print(line)             # 每一个临时变量，记录了文件的一行数据

# 文件的关闭：  f.close()     [不关的话，文件会一直处于打开的状态，如同 time.sleep(50000)]

with open语法
with open("D:/test.txt", "r") as f:
    f.read lines()
# 通过在with open的语句快中对文件进行操作
# 可以在操作完成后自动关闭close文件，避免遗忘掉close方法

# 通过文件读取操作，读取此文件，统计"hhh"出现的次数
content = f.read()
count = content.count("hhh)
或者按行读入,先删去前后的空格以及换行符，在以空格分割，按行统计字符个数


# 写操作
1.打开文件： f = open("D:/word.txt", "w")
2.文件写入： f.write("hello world")
3.内容更新： f.flush
直接调用write，内容并未真正写入文件，而是会积攒在程序的内存中，称之为缓冲区
当调用flush的时候，内容会真正写入文件
这样做是避免频繁的操作硬盘，导致效率下降（攒一堆，一次性写硬盘）

# 文件的追加
1.打开文件： f = open("D:/word.txt", "a")
2.文件写入： f.write("hello world")
3.内容更新： f.flush
可以使用”/n“来写换行符
a模式：文件不存在会创建文件
a模式：文件存在会在最后追加写入文件 与write的区别

# 打开文件
f = open("D:/test.txt", "r", encoding="UTF-8")
print(type(f))
print(f"读取10个字符的结果：{f.read(10)}")
print(f"用read方法读取全部内容的结果：{f.read()}")
print("------------------------------------")
lines = f.read lines()
print(f"lines对象的类型是:{type(lines)}")
print(f"lines的对象的内容是: {lines}")
print("------------------------------------")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")
print("------------------------------------")
for line in f:
    print(f"每一行的数据是：{line}")
print("------------------------------------")
with open("D:/test.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据是：{line})
print("------------------------------------")
f = open("D:/word.txt", "r", encoding="UTF-8")
content = f.read()
print(content.count("hhh"))
# 方式二：
count = 0
for line in f:
    line = line.strip()  #去除开头和结尾的空格以及换行符
    words = line.split(" ")
    for word in words:
        if word == "hhh"
            count += 1
print(f"文件中有{count}个hhh")
print("------------------------------------")
f = open("D:/test.txt", "w", encoding="UTF-8")
f.write("Hello World")  # 内容写入到内存中，暂时在文件夹的文件中看不到写入的字符
f.flush()               # 将内存中积攒的内容，写入到硬盘的文件中
f,close()               # close方法，内置了flush的功能


Python异常、模块和包
异常的捕获：可以对BUG进行提醒，整个程序继续运行，提前假设某处会出现
          异常，做好提前准备，当真的出现异常的时候，可以有后续手段
try:
    可能出现错误的代码
except:
    如果出现异常执行的代码
如:
需求：尝试以”r“模式打开文件，如果文件不存在，则以"w"方式打开
try:
    f = open("linux.txt", "r")
except:
    f = open("linux.txt", "w")

# 捕获指定的异常：
try:
    print(name)
    1 / 0                  # 捕获的类型不一样
except NameError as e:
    print("出现了变量未定义的异常)
    print(e)               # name 'name' is not defined

# 捕获多个异常：
try:
    print(1/0)
except (NameError,ZeroDivisionError):
# except (NameError,ZerpDivisionError) as e:
    print('ZeroDivision错误....')

# 捕获所有异常
try:
    1 / 0
except Exception as e:
    print("出现异常了！")

# 异常else
else表示的是如果没有异常要执行的代码
try:
    print(1)
except Exception as e:
    print(e)
else:
    print("我是else，是没有异常的时候执行的代码")

# finally表示的是无论是否异常都要执行的代码，例如关闭文件
try:
    f = open("linux.txt", "r")
except:
    f = open("linux.txt", "w")
else:
    print("没有异常！")
finally:
    f.close()

异常的传递：
def func01():    # 异常子啊func01中没有被捕获
    print("这是func01开始")
    num = 1 / 0
    print("这是func01结束)

def func02():
    print("这是func02开始")
    func01()
    print("这是func02结束)

def main():    # 异常在main中被捕获
    try:
        func02()
    except Exception as e:
        print(e)


模块(Module):
是个Python文件，以 py.结尾
模块能定义函数，类和变量，模块里也能包含可执行的代码
模块可以快速实现一些功能
模块在使用前需要先导入，导入的语法如下：
[from 模块名] import [模块 | 类 | 变量 | 函数 | *] [as 别名]
常用的组合形式：
import 模块名
from 模块名 import 类、变量、方法
from 模块名 import *           # 导入模块的全部功能
import 模块名 as 别名
from 模块名 import 功能名 as 别名

import time  # 导入Python内置的time模块（time.py这个代码文件）
time.sleep(5)  #沉睡5秒

from time import sleep
sleep(5)

import time as t    # 有的模块名过长，可以进行改名
from time import sleep as sl

自定义模块
新建一个python文件，可以命名为my_module.py,并定义test函数
每个Python文件都可以作为一个模块，每一个模块名必须要符合标识符命名规则
注意： 但导入多个模块的时候，且模块内有向名功能，当调用同名功能的时候，调用的时候
      是后面导入的模块的功能

import my_module
# from my_module import test
my_module.test(1, 2)
# test(1, 2)

__main__ 变量:
if __name__== "__main--"表示：
只有当程序是直接执行的才会进入if内部，如果是被导入的，则if无法进入

__all__变量:
如果一个模块文件中“__all__”变量，当使用 from xxx import *导入时
只能导入这个列表中的元素

Python包
Python模块太多，就会混乱
从物理上看，包就是一个文件夹，在该文件下包含了一个_init_.py文件
该文件可用于包含多个模块文件
从逻辑上看，包的本质依然是模块
导入包：
import 包名.模块名
包名.模块名.目标

注意：必须在‘_init_.py’文件中添加'_all_=[]',控制允许导入的模块列表
from 包名 import*
模块名.目标

import my_package.my_module1
import my_package.my_module2
my_package.my_module1.info_print1()
my_package.my_module2.info_print2()

from my_package import my_module1
from my_package import my_module2
my_module1.info_print1()
my_module2.info_print2()

from my_package.my_module1 import info_print1
from my_package.my_module2 import info_print2
info_print1()
info_print2()

安装第三方包
在Python程序的生态中，有许多的第三方包（非Python官方），可以极大的帮助我们提高
开发效率
如：
· 计算科学： numpy包
· 数据分析： pandas包
· 大数据计算： pyspark、apache-flink包
· 图像可视化： matplotlib、pyecharts
· 人工智能： tensorflow
但是由于是第三方，所以Python没有内置，所以我们需要安装它们才可以导入使用
pip install 包名称
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

Python异常、模块、包: 综合案例：
创建一个自定义包，名称为：my_utils(我的工具)
在包内提供2个模块
· str_util.py (字符串相关工具，内含：)
    · 函数：str_reverse(s),接受传入字符串，将字符串反转返回
    · 函数：sub str(s, x, y), 按照下标x和y，对字符串进行切片
· file_util.py (文件处理相关工具，内含：)
    · 函数：print_file_info(file_name),接受传入文件的路径，打印
    文件的全部的路径，打印文件的全部内容，如文件不存在则捕获异常，输出
    提示信息，同过finally关闭文件对象
    · 函数: append_to_file(file_name, data),接收文件路径以及
    传入数据，将数据追加到文件中

import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("广东工业大学"))
print(my_utils.str_util.substr("dictionary", 0, 4))
file_util.append_to_file("D:/test.txt", "okokok")
file_util.print_file_info("D:/test.txt")

数据可视化
-折线图可视化
json格式：
json无非就是一个单独的字典或一个内部元素都是字典的列表
1. JSON是一种轻量级的数据交互格式，可以按照JSON的格式取组织和封装数据
2. JSON本质是一个带有特定格式的字符串
主要功能：JSON就是一种在各个编程语言中流通的数据格式，负责不同编程语言中
的数据传递和交互，类似于：
    · 国际通用语言 - 英语
    · 中国56个民族不同的通用语言 - 普通话
json格式数据转化：
· json格式的数据要求很严格：
# json数据的格式可以是：
    {"name":"admin, "age":18}
# 也可以是：
    [{"name":"admin", "age":18},{"name":"root","age":16}]

Python数据和Json数据的相互转化
# 导入json模块
import json
# 准备符合json格式要求的python数据
data = [{"name":"admin", "age":18}, {"name":"root","age":16}]

# 通过json.dumps(data)方法把python数据转化为了json数据
data = json.dumps(data, ensure_ascii=False)
如果有中文，带上 ensure_ascii=False确保中文正常转换

# 通过json.loads(data)方法把json数据转化为了python数据
data = json.loads(data)

将JSON字符串转换为Python数据类型[{k: v, k: v}, {k: v, k: v}]
s = '[{"name":"admin", "age":18}, {"name":"root","age":16}]'
l = json.loads(s)
print(type(l))\
print(l)

pyecharts模块          pyecharts.org
做出数据可视化效果图
Echart是个由百度开源的数据可视化

pyecharts模块中有很多的配置选项
· 全局配置选项 : 针对整个图像来去设置，图像的标题，图例，工具箱等
· 系列配置选项 : 针对轴数据来个性化设置

from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
line = Line()
line.add_xaxis(["中国", "美国", "英国"])
line.add_yaxis("GDP", [30, 20, 10])
# 设置全局配置项set_global_opts
line.set_global_opts{
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap——opts=VisualMapOpts(is_show=True),
}

line.render()

数据处理：    # ab173.com 懒人工具网站
折线图开发：
import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

f_us = open("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/资料/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()  # 美国的全部内容

f_jp = open("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/资料/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()  # 日本的全部内容

f_in = open("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/资料/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()  # 印度的全部内容

# 去除不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")

# 去除不合JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]

# JSON转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend Key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于x轴，取2020年(到314下标结束)
us_x_data = us_trend_data['updateDate'][:314]
jp_x_data = jp_trend_data['updateDate'][:314]
in_x_data = in_trend_data['updateDate'][:314]

# 获取日期数据，用于y轴，取2020年(到314下标结束)
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
line = Line()  # 构建折线图对象
# 添加x轴数据
line.add_xaxis(us_x_data)  # x轴是公用的
# 添加y轴数据
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))

# 设置全局变量
line.set_global_opts(
    # 标题设置
    title_opts=TitleOpts(title="2020年美日印三国确诊人数对比折线图", pos_left="center", pos_bottom="1%")
)
line.render()

f_us.close()
f_jp.close()
f_in.close()


数据可视化 - 地图可视化
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts
map = Map()
data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("广东省", 499),
]
# 添加数据
map.add("测试地图", data, "china")

# 设置全局选项
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min": 10, "max": 99, "label": "10-99", "color": "#FF6666"},
            {"min": 100, "max": 500, "label": "100-500", "color": "#990033"}
        ]

    )
)

map.render()

#  演示全国疫情可视化地图开发
#  演示全国疫情可视化地图开发
#  演示全国疫情可视化地图开发
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f = open("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 取到各省数据
# 将字符串json转换为python的字典
data_dict = json.loads(data)
# 从字典中取出省份的数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并各个省的数据都封装如列表内
data_list = []
for province_data in province_data_list:
    if province_data["name"] == '北京' or province_data["name"] == '上海' or province_data["name"] == '重庆':
        province_name = (province_data["name"] + "市")
    elif province_data["name"] == '天津':
        province_name = (province_data["name"] + "市")
    elif province_data["name"] == '西藏':
        province_name = (province_data["name"] + "自治区")
    elif province_data["name"] == '内蒙古':
        province_name = (province_data["name"] + "自治区")
    elif province_data["name"] == '新疆':
        province_name = (province_data["name"] + "维吾尔自治区")
    elif province_data["name"] == '宁夏':
        province_name = (province_data["name"] + "回族自治区")
    elif province_data["name"] == '广西':
        province_name = (province_data["name"] + "壮族自治区")
    elif province_data["name"] == '香港' or province_data["name"] == '澳门':
        province_name = (province_data["name"] + "特别行政区")
    else:
        province_name = (province_data["name"] + "省")
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()
map.add("各省份确诊人数", data_list, "china")
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分段
        pieces=[
            {"min": 1, "max": 99, "label": "1-99", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "label": "100-999", "color": "#FFFF99"},
            {"min": 1000, "max": 4999, "label": "1000-4999", "color": "#FF9966"},
            {"min": 5000, "max": 9999, "label": "5000-9999", "color": "#FF6666"},
            {"min": 10000, "max": 99999, "label": "10000-99999", "color": "#CC3333"},
            {"min": 100000,  "label": "100000+", "color": "#990033"}
        ]
    )
)
map.render("全国疫情地图.html")
-------------------------------------------------------
import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

# 读取文件
f = open("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/资料/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
f.close()
# 取到各省数据
# 将字符串json格式转化为python的字典
data_dict = json.loads(data)
province_data_list = data_dict ["areaTree"][0]["children"]


# 组装省份和各省确诊人数为元组，并封装到列表中
data_list = []
for province_data in province_data_list:
    province_name = province_data["name"]
    province_confirm = province_data["total"]["confirm"]
    if province_name=="北京"or province_name=="天津"or province_name=="上海"or province_name=="重庆":
        data_list.append((province_name+"市", province_confirm))
    elif province_name=="西藏"or province_name=="内蒙古":
        data_list.append((province_name + "自治区", province_confirm))
    else:
        data_list.append((province_name+"省",province_confirm))
print(data_list)

# 创建地图
map = Map()
# 添加数据
map.add("各省确诊人数",data_list,)
# 设置全局配置，定制分段颜色
map.set_global_opts(
    title_opts = TitleOpts(title="各省疫情统计图"),
   visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 9, "label": "1-9", "color": "#CCFFFF"},
            {"min":10,"max":99,"label":"10-99","color":"#FFFF00"},
            {"min":100,"max":999,"label":"100-999","color":"#FFF000"},
            {"min":1000,"max":4999,"label":"1000-4999","color":"#FF9966"},
            {"min":5000,"max":9999,"label":"5000-9999","color":"#FF6666"},
            {"min":10000,"max":99999,"label":"10000-99999","color":"#cc3333"},
            {"min":100000,"label":"100000+","color":"#990033"},
        ]
    )
)
# 绘图
map.render("全国疫情地图.html")
-----------------------------------------------------------

# 动态柱状图:
基础柱状图：
from pyecharts.charts import Bar
bar = Bar()
bar.add_xaxis(["中国", "美国", "英国"])
bar.add_yaxis("GDP", [30, 20, 10])
# 把y轴放在右边
# bar.add_yaxis("GDP", [30, 20, 10]，label_opts(position="right"))
# 反转xy轴
bar.reversal_axis()
bar.render("基础柱状图.html")

时间线： Timeline：
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "英国"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "英国"])
bar2.add_yaxis("GDP", [50, 30, 15], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "英国"])
bar3.add_yaxis("GDP", [60, 55, 50], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

# 创造时间线对象
timeline = Timeline({"theme": ThemeType.DARK})
# timeline对象添加bar柱状图
timeline.add(bar1, "2021年三国GDP")
timeline.add(bar2, "2022年三国GDP")
timeline.add(bar3, "2023年三国GDP")
# 自动播放设置
timeline.add_schema(
    play_interval=1000,  # 自动播放的时间间隔，单位毫秒
    is_timeline_show=True,   # 是否在自动播放的时候，显示时间线
    is_auto_play=True,    # 是否自动播放
    is_loop_play=True     # 是否循环自动播放
)
# ThemeType.WHITE   红蓝  默认颜色等同于 bar=Bar()
# ThemeType.LIGHT   蓝黄粉  高亮颜色
# ThemeType.DARK    红蓝   黑色背景
# ThemeType.CHALK   红蓝绿  黑色背景
# 通过时间线绘图
timeline.render("基础柱状图-时间线.html")

# 如下嵌套列表，要求对外层列表进行排序，排序的依据市内层列表的第二个元素数字
# 以前学习的sorted函数就无法适用了，可以使用列表的sort方法
my_list = [["a", 33], ["b", 55], ["c", 11]]
def choose_sort_key(element):
    return element[1]
my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)

my_list = [["a", 33], ["b", 55], ["c", 11]]
my_list.sort(key=lambda element:element[1], reverse=True) # 匿名函数
print(my_list)

"""
# GDP动态柱状图开发
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType

# 读取数据
f = open("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r",
         encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典储存，格式为：
# {1960：[[美国， 123]， [中国，321],......], 1961}
# 先定义一个字典对象
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    # 如何判断字典里面有没有指定的key：
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])

# 创建时间线对象
timeline = Timeline({"theme": ThemeType.LIGHT})
# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    # 取出本年份前8名
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1])

    # 构建柱状图
    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    # 反转x轴和y轴
    bar.reversal_axis()
    # 设置每一年的图表的标题
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球GDP前8名数据")
    )
    timeline.add(bar, str(year))

# 设置时间线自动播放
timeline.add_schema(
    play_interval=800,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
timeline.render("1960~2019年全球GDP前8名国家.html")
