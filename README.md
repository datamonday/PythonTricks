# Pythonic Code

<center>Python相关知识总结与学习笔记。</center>

---

> Contributer: datamonday
>
> Github Repo: [https://github.com/datamonday/PythonTricks](https://github.com/datamonday/PythonTricks)

---

## 自学编程十大误区

1. 只学习，不动手练习。
2. 放弃学习，自我怀疑。（避免低水平勤奋）
3. 看到错误心就发慌。
4. 不注重编程语法基础。
5. **收藏学习资料和视频，而不去学习**。
6. 不做实战案例和练习。
7. 只输入，不输出。（费曼学习法）
   1. 盲目模仿，没有主见。
   2. 只会输入，不会思考。
   3. 没有计划，散心二意。
   4. 表面学习，流于形式。
8. 太注重语言本身，不断更换语言。
9. 不注重设计模式，死记硬背代码。
10. 学而不用，学习效率低下。



Reference：[避开这10个坑 自学编程很轻松](https://www.bilibili.com/video/BV1NX4y1N71i/?spm_id_from=333.788.recommend_more_video.4)

---

## 1. Python基础知识

> Reference:
>
> 1. [10个Python编程技巧（video）](https://www.bilibili.com/video/BV1kT4y1u72i?t=364)

---

## 2. Python 函数



> Reference:
>
> 1. [Python函数的参数详解（video）](https://www.bilibili.com/video/BV1k7411W78H/?spm_id_from=333.788.recommend_more_video.4)



---

## 3. Python 迭代器、生成器、yield



> Reference:
>
> 1. [深入浅出解析 Python yield（blog）](https://blog.csdn.net/weixin_39653948/article/details/105110120)
>
> 2. [15分钟彻底搞懂迭代器、可迭代对象、生成器（video）](https://www.bilibili.com/video/BV1BT4y1P7nn?from=search&seid=16190845741488495859)
>
> 3. [迭代器（blog）](https://pythonav.com/wiki/detail/1/11/)、[生成器（blog）](https://pythonav.com/wiki/detail/1/12/)

---

## 4. Python 闭包与装饰器

> Reference:
>
> 1. [Python小技巧：装饰器(Decorator) （video）](https://www.bilibili.com/video/BV11s411V7Dt?from=search&seid=6784234166068928110)
> 2. [5句口诀理解记忆Python闭包和装饰器 （video）](https://www.bilibili.com/video/BV1ZJ411y7Te?from=search&seid=6784234166068928110)
> 3. [彻底学会Python装饰器（video）](https://www.bilibili.com/video/BV1Vv411x7hj?p=4)

---

## 5. Python 并发编程

> Reference:
> 1.  [2小时玩转python多线程编程（video）](https://www.bilibili.com/video/BV1fz4y1D7tU?p=16)
> 2.  [Python 并发编程实战，用多线程、多进程、多协程（video）](https://www.bilibili.com/video/BV1bK411A7tV?p=10&t=318)
> 3. Github Repo: [ant-learn-python-concurrent](https://github.com/peiss/ant-learn-python-concurrent)



---

## 6. asyncio 异步编程





---

## 7. Python 内存管理与垃圾回收机制

> Reference:
>
> 1. [2小时吃透python内存管理和垃圾回收机制（video）](https://www.bilibili.com/video/BV1Ei4y1b7mo?p=5&t=283)
> 2. [C语言源码解析Python内存管理和垃圾回收机制（blog）](https://pythonav.com/wiki/detail/6/88/)

---

## 8. Python面向对象






---

## 9. Python模块





---

## 10. Python文件操作





---

## 11. Python编程规范





---

## 12. 制作 pip install 包

>  Reference：
>
> 1. [制作 pip install 包（video）](https://www.bilibili.com/video/BV17541187de)、[pip install 包（blog）](https://pythonav.com/wiki/detail/6/95/)

---

# Homework

Python课程上机实验题目

### Exp 01

- 编写程序，生成包含1000个0到100之间的随机整数，并统计每个元素的出现次数。
- 编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果。
- 编写程序，运行后用户输入4位整数作为年份，判断其是否为闰年。如果年份能被400整除，则为闰年；如果年份能被4整除但不能被100整除也为闰年。
- 编写程序，实现分段函数计算。
- 编写程序，用户在命令提示行输入文件名和该文件的编码格式，读入文件，将其转存成UTF-8格式。如果用户没有指定输入文件的编码格式，则使用chardet模块“猜”出其编码格式，用于解码。使用argparse模块解析用户命令提示行输入。

---

### Exp 02

- 编写函数，接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，并以元组的形式返回结果。
- 编写函数，可以接收任意多个整数并输出其中的最大值和所有整数之和。
- 编写函数，模拟内置函数sorted()。（你需要先读内置函数 sorted() 的关方文档，搞清楚它的输入参数和输出）。
- 以字典为基础建立一个通讯录，向字典中添加和删除通讯人（名字、电话、email、工作单位等），查询某个人的信息，然后输出通讯录中所有人的信息。
- 用生成器的方式计算任意起止范围内质数的和。质数又称素数，是大于1的自然数，除了1和它本身外，不能被其他自然数整除。