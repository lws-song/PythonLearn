"""
数据库是用来存储数据的，会涉及到
·数据的 增、删、改、查
而SQL语言，就是一种对数据库，数据进行操作、管理、查询的工具
使用数据库软件取获得库->表->数据，这种数据组织、存储的能力
并借助SQL语言，完成对数据的增删改查
在MySQL的命令行环境下，可以通过：
· show databases; 查看有哪些数据库
· use 数据库名;   使用某个数据库
· show tables;  查看数据库内有那些表
· exit推出MySQLde命令行环境

SQL：结构化查询语言，用于访问和处理数据库的标准的计算机语言
由于数据库管理系统（数据库软件）功能非常多，不仅仅是存储数据，还要包含：
数据的管理，表的管理，库的管理，账户管理，权限的管理
所以：操作数据库的SQL语言，也基于功能，可以划分为4类：
· 数据定义： DDL (Data Definition Language)
     · 库的创建删除、表的创建删除等
· 数据操纵： DML (Data Manipulation Language)
     · 新增数据、删除数据、修改数据等
· 数据控制： DCL (Data Control Language)
     · 新增用户、删除用户，密码修改，权限管理等
· 数据查询： DQL (Data Query Language)
     · 基于需求查询和计算数据

在学习DDL、DQL等之前
· SQL语言，大小写不敏感
· SQL语言可以单行或多行书写，最后以;号结束
· 多行支持注释：
    · 单行注释： --注释内容（--后面一定要有空格）
    · 单行注释： # 注释内容（#后面可以不加空格，推荐加上）
    · 多行注释： /* 注释内容 */
-----------------------
执行那条语言，就选择那条语言
-----------------------

DDL

DDL-库管理
查看数据库：
show databases;
使用数据库：
use 数据库名称;
创建数据库：
create databases 数据库名称 [CHARSET UTF-8]
删除数据库：
drop databases 数据库名称;
查看当前使用的数据库：
select databases();

show
-- 大小写不敏感，show databases 也可以
# 我是注释
/*
 我
 是
 注释
 */
databases;

use world;
select database();
create database test charset utf8;
show databases;
drop database test;

# DDL-表管理
# 查看有哪些表：
show tables   # 注意先选择数据库
# 删除数据库：
# drop tables 表名称;
创建表：
create tables 表名称(
    列名称 列类型
    列名称 列类型
    ............
)
类类型有：
int
float
varchart(长度)  --文本，长度为数字，做最大长度限制
date           --日期类型
timestamp      --时间戳类型


use world;
show tables;
create table student(
(缩进)id int,
(缩进)name varchar(10),
(缩进)age int
);
drop table student;


DML

数据插入insert
基础语法：
insert into 表[列1， 列2， ........,列N] values(值1， 值2，..........
值N)[, (值1，值2，.....值N),......,(值1, 值2,.......值N)]
create table student(
id int,
name varchar(10),
age int
);

# insert into student(id) values(1);
# insert into student(id) values(2);
# insert into student(id) values(3);
insert into student(id) values(1), (2), (3);

# insert into student values(4, '周杰伦', 31), (5, '周杰', 32);
insert into student(id, name, age) values(4, '周杰伦', 31), (5, '周杰', 32);

数据删除 Delete
基础语法：
delete from 表名称 [where 条件判断]
条件判断： 列 操作符 值
操作符： = < > <= >= !=  等等
# delete from student where id = 1;
# delete from student where id < 4;
# delete from student where age = 31;
# 删除表中的全部元素
delete from student;

数据更新：
基础语法
update 表名 set 列=值 [where 条件判断]
insert into student(id, name, age) values(4, '周杰伦', 31), (5, '周杰', 32);
# update student set name = '王力宏'
# 将表中所有name改为王力宏
update student set name = '张学友' where id = 4;

DQL
select 字段列表|* from 表
insert into student(id, name, age) values
(1, '周杰伦', 31),
(2, '周杰', 32),
(3, '周', 33),
(4, '张学友', 34),
(5, '王力宏', 35),
(6, '林俊杰', 36),
(7, '库里', 37),
(8, '杰斯', 38);
# select * from student;
# * 为通配符 即选择所有展示
# select id, name, age from student;
# select * from student where age > 33;
select * from student where name = '张学友';
select id, name from student where age > 33;

# DQL : group by 进行分组聚合查询
如：统计班级中，男生和女生的人数
基础语法：
select 字段|聚合函数 from 表 [where 条件] group by 列
聚合函数：
-- sum(列)  求和
-- avg(列)  求平均值
-- min(列)  求最小值
-- max(列)  求最大值
-- count(列|*)  求数量
create table student(
id int,
name varchar(10),
age int,
gender varchar(1)
);
insert into student(id, name, age, gender) values
(1, '周杰伦', 31, '男'),
(2, '周杰', 32, '女'),
(3, '周', 33, '男'),
(4, '张学友', 34, '女'),
(5, '王力宏', 35, '男'),
(6, '林俊杰', 36, '女'),
(7, '库里', 37, '男'),
(8, '杰斯', 38, '男');
# 对性别分组，计算年龄的平均值
# select avg(age) from student group by gender;
# 但看不到性别，加上gender
# select gender, avg(age) from student group by gender;
# 也可以叠加多个聚合函数
select gender, avg(age) , sum(age), min(age), max(age),count(*) from student group by gender;
注意：
group by中出现了哪一列，哪个列才能出现在select的非聚合中

# 结果排序
使用order by关键字，指定某个列进行排序，语法：
select 列|聚合函数|* from 表
where ...
group by ...
order by ...[ASC | DESC]   ASC从小到大  DESC从大到小
结果分页限制
可以使用limit关键字，对查询结果进行数量限制或分页显示，语法：
limit n[, m]
# select * from student where age > 20 order by age desc;
# 限制只要显示前五条
# select * from student limit 5;
# 限制只要从第3条开始，显示前五条,但不包括地3条
select * from student limit 3, 5;
# 顺序不要搞错
select age, count(*) from student where age > 20 group by age
order by age limit 3;

执行顺序：
from     where    group by和聚合函数   select   order by  limit

# python & MYSQL
pymysql
在python中，使用第三方库：pymysql来完成对mysql数据库的操作
创建到mysql的数据库连接：
from pymysql import Connection
# 获取到MySQL数据库的连接对象
conn = Connection(
    host="localhost",  # 表示自己的电脑
    port=3306,
    user="root",
    password="111"
)
# 打印MySQL数据库软件信息
# print(conn.get_server_info())
# 执行非查询性质SQL
cursor = conn.cursor()  # 获取游标对象
# 选择数据库
# conn.select_db("test")
conn.select_db("world")
# 执行sql
# 游标对象.execute()执行SQL语句
# cursor.execute("create table test_pymysql(id int);")  # 其中的;可以不加
cursor.execute("select * from student")
# 仪表对象.fetchall()得到全部的查询结果封装入元组中
results = cursor.fetchall()

for r in results:
    print(r)
# 关闭到数据库的链接
conn.close()

# 数据的插入
commit提交
pymysql在执行数据或其他产生数据更改的SQL语句是，默认是需要提交更改的，即
需要通过代码“确认”这种更改行为
通过   连接对象.commit()即可完成此行为
from pymysql import Connection
# 获取到MySQL数据库的连接对象
conn = Connection(
    host="localhost",  # 表示自己的电脑
    port=3306,
    user="root",
    password="111"
    autocommit=True # 设置自动提交
)
cursor = conn.cursor()
conn.select_db("world")
cursor.execute("insert into student values(9, '刘大帅', 22, '男' )")
conn.commit()
conn.close()
# 如果不想手动commit确认，可以构建链接对象的时候，设置自动commit的属性
autocommit=True



"""

