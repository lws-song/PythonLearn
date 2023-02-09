"""
ctrl + p
Alt + Enter
# 面向对象
类只是一种程序内的”设计图纸“(模板)，需要基于图纸生产实体（对象），才能正常工作，这种
套路称之为：面向对象编程
# 使用对象组织数据
1. 在程序中设计表格，我们称之为：设计类(class)
class Student:
    name = None
    age = None
2. 在程序中打印生产表格，我们称之为：创建对象
# 基于类创建对象
stu_1 = Student()
stu_2 = Student()
3.在程序中填写表格，我们称之为：对象属性赋值
stu_1.name = "周杰伦"
stu_2.name = "林俊杰"

# 类的定义与使用
class 类名称:   # class是关键字,表示要定义类了
    类的属性    # 类的属性，即定义在类中的变量 （成员变量）
    类的行为    # 类的行为，即定义在类中的函数（成员方法）
创建类对象的语法：
对象 = 类名称()
class Student:
    name = None
    age = None
    def say_hi(self):
        print(f"Hi大家好，我是{self.name}")
stu = Student()
stu.name = "周杰伦"
stu.say_hi()

在类中定义成员方法和定义函数基本一直，但仍有细微区别：
def 方法名(self, 形参1, 形参2.... )
    方法体
在方法定义的参数列表中，有一个：self关键字
self关键字是成员方法定义的时候，必须填写的。
· 它用来表示类对象自身的意思
· 当我们使用类对象调用方法的时候，self会自动被python传入
· 在方法内部，想要访问的成员变量，必须使用self

构造方法：
python类可以使用: __init__()方法，称之为：构造方法
可以实现：
· 在创建类对象（构造类）的时候，会自动执行
· 在创建类对象（构造类）的时候，将传入参数自动传递给__init__方法使用
class Student:
    name = None     # 可以省略（在__init__中又声明又赋值）
    age = None      # 可以省略（在__init__中又声明又赋值）
    tel = None      # 可以省略（在__init__中又声明又赋值）

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个对象")
stu = Student("周杰伦", 31, "18500000066")

魔术方法：
__init__是Python类内置的方法之一
这些内置的类方法，各自有各自的功能，这些内置方法我们称之为：魔术方法
__init__: 构造方法
__str__: 字符串方法
__lt__: 小于，大于符号比较
__le__: 小于等于，大于等于符号比较
__eq__: ==符号比较

class Student:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    # __str__魔术方法
    def __lt__(self, other):
        return f"Student类对象，name:{self.name},age:{self.age}"

    # __lt__魔术方法
    def __lt__(self, other):
        return self.age < other.age

    # __le__魔术方法
    def __le__(self, other)
            return self.age <= other.

    # __eq__魔术方法
    def __eq__(self, other)
            return self.age == other.age

若只用__init__的话，所有返回的都是内存地址，内存地址没有多大作用
stu1 = Student("周杰伦", 31)
stu2 = Student("周杰伦", 32)
print(stu1)
print(str(stu1))
print(stu1 < stu2)   # True
print(stu1 > stu2)   # False
print(stu1 <= stu2)   # True
print(stu1 >= stu2)   # False
print(stu1 == stu2)   # False

面向对象编程包含三大主要特性
封装
继承
多态

封装：
表示将现实世界的：属性和行为
封装到类中描述为：成员变量，成员方法
从而完成程序对现实世界的描述

私有成员：
既然现实事物有不公开的属性和行为，那么作为现实事物在程序中映射的类，也应该支持
类中提供了私有成员的形式来支持：
· 私有成员变量
· 私有成员方法
定义私有成员的方法非常简单：
· 私有成员变量：变量名以__开头
· 私有成员方法：方法名以__开头
即可完成私有成员的设置
在类中提供仅供内部使用的属性和方法，而不对外开放
class Phone:

    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g谈话已开启")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g通话，并已使用单核运行进行省电")

phone = Phone()
# phone.__keep_single_core()   # 报错
# print(phone.__current_voltage)  # 报错
phone.call_by_5g()


class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone()
phone.call_by_5g()


继承： 将从父类那里继承（复制）来成员变量和成员方法（不含私有）
基层分为:单继承 和 多继承
class Phone:
    IMEI = None
    producer = "刘氏"

    def call_by_4g(self):
        print("4g通话)

class phone2022(Phone):
    face_id = True

    def call_by_5g(self):
        print("2022最新5g通话")

多继承：
class 类名(父类1, 父类2, 父类3,.....):
    类内容体
多继承注意事项：
多个父类中，如果有同名的成员，那么默认以继承顺序（从左到右）为优先级
即：先继承的保留，后继承的被覆盖
class Phone:
    IMEI = None  # 序列号
    producer = "刘氏"

    def call_by_5g(self):
        print("5g通话")


class NFCReader:
    nfc_type = "第五代"
    producer = "huawei"

    def read_card(self):
        print("读取NFC卡")

    def write_card(self):
        print("写入NFC卡")


class RemoteControl:
    re_type = "红外控制"

    def control(self):
        print("红外线开启了！")


class MyPhone(Phone, NFCReader, RemoteControl):
    pass


my_phone = MyPhone()
print(my_phone.producer)
my_phone.read_card()
my_phone.write_card()
print(my_phone.re_type)
my_phone.control()

复写：
子类继承父类的成员属性和成员方法后，如果对其”不满意“，那么可以进行复写
即：在子类中重新定义同名的属性或方法即可：

调用父类同名成员
一旦复写父类成员，那么类对象调用成员的时候，就会调用复写后的新成员
如果需要使用被复写的父类的成员，需要特殊的调用方式
· 调用父类成员
    使用成员变量： 父类名.成员变量
    使用成员方法： 父类名.成员方法
· 使用super()调用父类成员
    使用成员变量： super().成员变量
    使用成员方法： super().成员方法

类型注解
基础语法：   变量:类型
var_1: int = 10
var_2: float = 3.1415926
var_3: bool = True
var_4: str = "happy"
class Student:
    pass
stu: Student = Student
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"happy": 666}
my_str: str = "happy"

# 元组类型设置类型详细注解，需要将每一个元素都标记出来
# 字典类型设置详细注解，需要2个类型，第一个是key第二个是value
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[str, int, bool] = ("happy", 666, True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"happy": 666}

# 两者都可以
var_1 = random.random(1, 10)  # type: int
var_1: int = random.random(1, 10)
一般，无法直接看出变量类型之时会添加变量的类型注解

函数和方法的形参类型注解语法：
def 函数方法名(形参名: 类型, 形参名: 类型, .....)
    pass
def add(x: int, y: int):
    return x + y
def func(data: list):
    pass
# 对返回值进行类型注解
def func(data: list) -> list:
    return data

Union类型
若数组，字典中又有字符串，又有数字 可以使用Union类型
from typing import Union

my_list: list[Union[str, int]] = [1, 2, "happy", "phone"]
my_dict: dict[str, Union[str, int]] = {"name": "周杰伦", "age": 31}
可以定义联合类型注解
def func(data: Union[int, str]) -> Union[int, str]:
    pass

多态
多态，指的是：多种状态，即完成某个行为时，使用不同的对象会得到不同的状态
多态常作用在继承关系上：
比如
· 函数(方法)形参声明接受父类对象
· 实际传入父类的子类对象进行工作
即：
· 以父类做定义声明
· 以子类做实际工作
· 用以获得同一行为，不同状态

# 演示面向对象的多态特性以及抽象类（接口）的使用
# 抽象类就好比定义一个标准
包含了一些抽象的方法，要求子类必须实现


# 抽象类：含有抽象方法的类称之为抽象类
# 抽象方法： 方法体是空实现的（pass）称之为抽象方法
class Animal:     # 抽象类
    def speak(self):  # 这种设计的含义是：
        pass  # 父类用来确定有哪些方法
        # 具体的方法实现，有子类自行决定


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    # 制造点噪音，需要传入Animal对象
    animal.speak()


# 演示多态，使用2个子类对象来调用函数
dog = Dog()
cat = Cat()
make_noise(cat)
make_noise(dog)

class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass
class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调的制热)
    def swing_l_r(self):
        print("美的空调左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调的制热)
    def swing_l_r(self):
        print("格力空调左右摆风")

def make_cool(ac: AC):
    ac.cool_wind()
midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(midea_ac)
make_cool(gree_ac)

---------------------------------------------------
数据分析案例（面向对象）
---------------------------------------------------
# 案例1：
某公司，有两份文件，需要对其进行分析处理，计算每日的销售额并以柱状图表的形式进行展示
读取数据 -> 封装数据对象 -> 计算数据对象 -> pyecharts绘图



"""
