"""
Spark是Apache基金会旗下的顶级开源项目，用于对海量数据进行大规模分布式计算
PySpark是Spark的Python实现，是Spark为Python开发者提供的编程入口，用于
以Python代码完成Spark任务的开发
PySpark不仅可以作为Python第三方库使用，也可以将程序提交的Spark集群环境
中，调度大规模集群进行执行
Spark（Pyspark）是大数据开发中核心技术


演示获取PySpark的执行环境入库对象： SparkContext
并通过SparkContext对象获取当前的PySpark的版本

SparkContext类对象，是PySpark编程中一切功能的入口
PySpark的功能都是从SparkContext对象作为开始
PySpark的编程，主要分为如下三个步骤
数据输入：
通过SparkContext类对象的成员方法完成数据的读取操作
读取后得到RDD类对象
（RDD:弹性分布式数据集）
数据处理计算：
通过RDD对象的成员方法，完成各种数据计算的需求

数据输出：将处理完成后的RDD对象调用各种成员方法完成，写出文件，转换为list等操作


# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = Conf().serMaster("local[*]").setAppName("test_Spark_app")
#conf = SparkConf()
#conf.setMaster("local[*]")
#conf.setAppName("test_name")

# 基于 SparkConf类对象创建SparkContext对象
sc = SparkContext(conf = conf)

# 打印PySpark的运行版本
print(sc.version)
# 停止对SparkContext对象的运行(停止PySpark程序)
sc.stop()

RDD对象
PySpark支持多种数据的输入，在输入完成后，都会得到一个：RDD类的对象
（RDD:弹性分布式数据集）
PySpark针对数据的处理，都是以RDD对象作为载体，即：
· 数据存储在RDD内
· 各类数据的计算方法，也都是RDD的成员方法
· RDD的数据计算方法，返回值依旧是RDD对象

PySpark支持通过SparkContext对象的parallelize成员方法
注意：字符串会被拆出1个个的字符，存入RDD对象
     字典仅有key会被RDD对象
通过parallelize方法将Python对象加载到Spark内，成为RDD对象
用textFile方法，读取文件数据加载Spark内，成为RDD对象


from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 通过parallelize方法将Python对象加载到Spark内，成为RDD对象
rdd1 = sc.parallelize([1, 2, 3, 4])
rdd2 = sc.parallelize((1, 2, 3, 4))
rdd3 = sc.parallelize("abcdefg")
rdd4 = sc.parallelize({1, 2, 3, 4})
rdd5 = sc.parallelize({"key1": "value1", "key2": "value2"})

# 如果要查看RDD里面有什么内容，需要用collect()方法
print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())


# 用textFile方法，读取文件数据加载Spark内，成为RDD对象
rdd = sc.textFile("D:/word.txt")
print(rdd.collect())
sc.stop()

数据计算：
map方法：
成员方法(算子)
map算子是将RDD的数据一条条处理，(处理的逻辑，基于map算子中接收的处理函数)，返回新的RDD

D:/dev/python/python3.11.1/python.exe
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python3.11.1/python.exe"

conf = SparkConf().setMaster(["local[*]"]).setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1, 2, 3, 4])

# 通过map方法将全部数据都乘10
def func(data):
    return data * 10

rdd2 = rdd.map(func)
# rdd2 = rdd.map(lambda x: x * 10).map(lambda x: x + 5)
print(rdd2.collect())


flatmap算子
计算逻辑和map一样
可以比map多出，接触一层嵌套的功能
功能：对rdd执行map操作，然后进行解除嵌套操作
接触嵌套：
# 嵌套的list
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#如果接触嵌套
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 构建执行环境，和入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python3.11.1/python.exe"
conf = SparkConf().setMaster(["local[*]"]).setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["happy hello map", "hoop year near", "ok jack cook"])

# 需求，将RDD数据里的一个个单词提取出来
rdd2 = rdd.map(lambda x: x.split(" "))
# 结果：  [['happy', 'hello', 'map'], ['hoop', 'year', 'near'], ['ok', 'jack', 'cook']]
# 如果用flatMap
rdd2 = rdd.flatMap(lambda x: x.split(" "))
# 结果： ['happy', 'hello', 'map', 'hoop'......]
print(rdd2.collect())

reduceByKey算子
功能：针对KV型RDD，自动按照key分组，然后根据你提供的聚合逻辑，完成组内数据(value)的聚合操作
语法：
rdd.reduceByKey(func)
# func: (v, v) -> v
# 接受2个传入参数（类型要一致），返回一个返回值，类型要和传入要求一致
注意： reduceByKey中接受的函数，只负责聚合，不理会分组
分组是自动by key来分组的

# 构建执行环境，和入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python3.11.1/python.exe"
conf = SparkConf().setMaster(["local[*]"]).setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(['男', 99], ['女', 99], ['男', 88], ['女', 66])
# 求男生和女生两个组的成绩之和
rdd2 = rdd.reduceByKey(lambda a, b: a + b)
print(rdd2.collect())

案例： 完成使用PySpark进行单词技术的案例
· 读取文件
· 统计文件内，单词出现的数量
# 构建执行环境，和入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python3.11.1/python.exe"
conf = SparkConf().setMaster(["local[*]"]).setAppName("test_spark")
sc = SparkContext(conf=conf)
# 读取数据文件
rdd = sc.textFile("D:/word.txt")
# 取出全部单词
word_rdd = rdd.flatMap(lamb x: x.split(" "))
# 将所有单词都转换为二元元组，单词为Key，value为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
print(result_rdd)


Filter
功能：过滤想要的数据进行保留
rdd.filter(func)
# func: (T) -> bool
传入1个参数进来随意类型，返回值必须是True or False
rdd = sc.parallelize([1, 2, 3, 4, 5])
# 过滤掉偶数
rdd2 = rdd.filter(lambda x: x % 2 == 0)
print(rdd2.collect())


distinct算子
功能: 对RDD数据进行去重，放回新RDD
rdd = sc.parallelize([1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9, 10 ])
rdd2 = rdd.distinct()
print(rdd2.collect())


sortBy算子
功能： 对RDD数据进行排序，基于你指定的排序依据
语法：
rdd.sortBy(func, ascending=false, numPartitions=1)
# func: (T) -> U: 告知按照rdd中的哪个数据进行排序，比如 lambda x: x[1]
  表示按照rdd中的第二列元素进行排序
# ascending  True升序  False 降序
# numPartition : 用多少分区排序

# 读取数据文件
rdd = sc.textFile("D:/word.txt")
# 取出全部单词
word_rdd = rdd.flatMap(lamb x: x.split(" "))
# 将所有单词都转换为二元元组，单词为Key，value为1
word_with_one_rdd = word_rdd.map(lambda word: (word, 1))
# 分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b: a + b)
# 对结果进行排序
sorted_result_rdd = result.sortBy(lambda x: x[1], ascending=True, numPartition=1)
print(result_rdd)
print(sorted_result_rdd)


案例2：
使用Spark读取文件进行计算
· 各个城市销售额排名，从大到小
· 全部城市，有哪些商品类别在售卖
· 北京市有哪些商品类别在售卖

# 构建执行环境，和入口对象
import json
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python3.11.1/python.exe"
conf = SparkConf().setMaster(["local[*]"]).setAppName("test_spark")
sc = SparkContext(conf=conf)

# 需求1: 城市销售额排名
# 1.1 读取文件得到RDD
file_rdd = rdd.textFile("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/第15章资料/资料/order.txt")
# 1.2 取出一个个JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))
# 1.3 将一个个JSON字符串转换为字典
dict_rdd = json_str_add.map(lambda x: json.loads(x))
# 1.4 取出城市和销售额数据
city_with_money_rdd = dict_rdd.map(lambda x: (x['areaName'], int(x['money'])))
# 1.5 按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda a, b: a + b )
# 1.6 按销售额聚合结果进行排序
result1_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False, numPartition=1)
# 需求2: 全部城市有哪些商品类别在售卖
# 2.1 取出全部的商品类别
category_rdd = dict_rdd.map(lambda x: x['category']).distinct()
print("需求2的结果是：", category_rdd.collect())
# 2.2 对全部商品类别进行去重
# 需求3：北京市有哪些商品类别在卖
# 3.1 过滤北京市的数据
beijing_data_rdd = dict_rdd.filter(lambda x: x['areaName'] == '北京')
# 3.2 取出全部商品类别
result3_rdd = beijing_data_rdd.map(lambda x: x['category']).distinct()
print("需求3的结果是：", result3_rdd.collect())


数据输出：
Python文件或文件  ->  RDD  ->  Python对象或文件
计算： rdd的那些返回值还是rdd的方法
输出： rdd的那些返回值不是rdd的方法

collect算子
功能： 将rdd各个分区内的数据，统一收集到Driver中，形成一个list对象
用法：rdd.collect
返回值是一个list

reduce算子
功能： 对RDD数据集按照你传入的逻辑进行聚合
rdd.reduce(func)
# func: (T, T) -> T
# 2参数传入 1个返回值和参数要求类型一致
rdd = sc.parallelize(range(1, 10))
print(rdd.reduce(lambda a, b: a + b))

take算子
功能：取RDD的前N个元素，组合成list返回给你
sc.parallelize([3, 1, 3, 4, 5, 6]).take(5)

count算子
功能： 计算rdd有多少条数据，返回值是一个数字
sc.parallelize([3, 1, 3, 4, 5, 6]).count()


输出到文件中：
掌握将RDD的内容输出到文件中
了解如何更改RDD的分区数为1


saveAsTextFile算子
功能；将RDD的数据写入文本文件中
支持本地写出，hdfs等文件系统
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python3.11.1/python.exe"
os.environ['HADOOP_HOME']='D:/Python学习资料/Python快速入门（8天零基础入门到精通）/第15章资料/资料/hadoop-3.0.0'
conf = SparkConf().setMaster(["local[*]"]).setAppName("test_spark")
sc = SparkContext(conf=conf)
rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize([("hello", 3), ("Spark", 5), ("Hi", 7)])
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]])
rdd1.saveAsTextFile("D:/output1")
rdd2.saveAsTextFile("D:/output2")
rdd3.saveAsTextFile("D:/output3")

修改rdd分区为1个
方式1：SparkConf对象设置属性全局并行度为1：
conf = SparkConf().setMaster(local[*].setAppName("test_spark"))
conf,set('spark.default.parallelism', "1")
sc = SparkContext(conf=conf)

方式2： 创建RDD的时候设置(parallelize方法传入numSlices参数为1)
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)
rdd1 = sc.parallelize([1, 2, 3, 4, 5], 1)

综合案例： 搜索引擎日志分析
读取文件转换成RDD，并完成：
· 打印输出： 热门搜索时间段(小时精度)Top3
· 打印输出： 热门搜索词Top3
· 打印输出： 统计黑马程序员关键字在哪个时段被搜索最多
· 将数据转换为JSON格式，写出为文件
D:/Python学习资料/Python快速入门（8天零基础入门到精通）/第15章资料/资料

from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "D:/dev/python/python3.11.1/python.exe"
os.environ['HADOOP_HOME']='D:/Python学习资料/Python快速入门（8天零基础入门到精通）/第15章资料/资料/hadoop-3.0.0'
conf = SparkConf().setMaster(["local[*]"]).setAppName("test_spark")
conf,set('spark.default.parallelism', "1")
sc = SparkContext(conf=conf)

# 读取文件转换成RDD
file_rdd = sc.textFile("D:/Python学习资料/Python快速入门（8天零基础入门到精通）/第15章资料/资料/search_log.txt")
# 需求1：热门搜索时间段(小时精度)Top3
# 1.1 取出全部的时间并转换为小时
# 1.2 转换为(小时, 1)的二元元组
# 1.3 Key分组聚合Value
# 1.4 排序(降序)
# 1.5 取前三
result1 = file_rdd.map(lambda x: x.split("\t")).\
    map(lambda x: x[0][:2]).\
    map(lambda x: (x, 1)).\
    #
    file_rdd.map(lambda x: (x.split("\t")[0][:2], 1))
    #
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartition=1).\
    take(3)
print(result1)
# 需求2： 热门搜索词Top3
# 2.1 取出全部的搜索词
# 2.2 (词, 1)二元元组
# 2.3 分组聚合
# 2.4 排序
# 2.5 Top3
result2 = file_rdd.map(lambda x: (x.split("\t")[2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartition=1)
    take(3)
print(result2)

# 需求三：统计黑马程序员关键字在什么时段被搜索的最多
# 3.1 过滤内容，只保留黑马程序员关键词
# 3.2 转换为(小时, 1)的二元元组
# 3.3 Key分组聚合Value
# 3.4 排序(降序)
# 3.5 取前1
result3 = file_rdd.map(lambda x: x.split("\t")).\
    filter(lambda x: x[2]=="黑马程序员").\
    map(lambda x: (x[0][:2], 1)).\
    reduceByKey(lambda a, b: a + b).\
    sortBy(lambda x: x[1], ascending=False, numPartition=1)
    take(1)
print(result3)

# 需求4： 将数据转换为JSON格式，写出到文件中
# 4.1 转换为JSON格式的RDD
# 4.2 写出到文件
file_rdd.map(lambda x: x.split("\t")).\
    map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank1": x[3], "rank2": x[4], "url": x[5]}).\
    saveAsTextFile("D:/output_json")




"""

