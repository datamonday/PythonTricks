原载于：[深入浅出解析 Python yield](https://blog.csdn.net/weixin_39653948/article/details/105110120)

---

之前遇到yield的时候没有深入了解，今天又遇到了`yield`，发现对`yield`的用法已经模糊不清了，于是重新查阅资料，发现很多教程对小白不友好，因此我以小白的视角把自己对`yield`的基本用法的理解梳理总结出来，希望对大家有帮助，如果我的理解与各位小伙伴理解的有出入或文中有错误，欢迎提出，我们一起讨论。我将从以下三个方面介绍。

---

[TOC]

---

# 1. 为什么要用 yield ？
在我遇到yield的时候，首先想的是`“什么是yield？”`，但是当专注去找yield是什么的时候，发现越来越看不懂了，因为要搞清楚这个问题需要一些先修知识，比如可迭代对象、迭代器、生成器，这些概念稍后介绍。当了解这些以后，就一目了然了。

## 1.1 print() 和 return 有什么区别？
<font color=red> 清楚二者用法的直接跳过此部分。</font>

相信小伙伴们都清楚`print()`的用法，也用过`return`，那么 `print()` 和 `return` 有什么区别呢？顾名思义，“print”即“打印”，将在控制台打印`print()`方法中的信息。`return`的作用是使函数退出，并将返回值返回给调用者。看一个简单的例子：

```python
# 定义一个加法运算函数
def print_vs_return(a, b):
	c = a + b
	print("运算结果为:{}".format(c))
	return c
```

```	python
# 调用函数实现两个数的加法运算
print_vs_return(1,2)
```

如果在解释器中（比如在IPython中或者spyder、pycharm等IDE中）运行，则输出为：
```shell
运算结果为:3
```

如果将其作为脚本（比如.py文件）运行或者在notebook中运行，则输出为：
```shell
运算结果为:3
3
```

---
使用赋值的方法调用

```python
callback_c = print_vs_return(1,2)
print("callback_c调用函数后的值为:{}".format(callback_c))
```
在IDE中运行输出为：

```shell
运算结果为:3
callback_c调用函数后的值为:3
```

---
如果我们把上例中的`return c` 语句去掉，重新运行赋值方法调用，结果为`None`：

```python
def print_vs_return(a, b):
	c = a + b
	print("运算结果为:{}".format(c))
	#return c

callback_c = print_vs_return(1,2)
print("callback_c调用函数后的值为:{}".format(callback_c))
```

输出：
```shell
运算结果为:3
callback_c调用函数后的值为:None
```

<font color=blue>由以上分析可以看出，调用函数时，`print()`会在控制台打印信息，然后继续执行下一条语句，并不会退出函数执行，同时“print”出的信息不能被其他变量调用；而`return`执行完之后则终止函数运行，并将“return”的“值”返回给调用它的函数（如上例），当函数中有返回值`return`时，可以采用赋值调用的方法给变量赋值，如果函数中没有返回值，采用赋值调用给变量赋值时，变量赋值的结果为`None`，表示无意义或空值。</font>

---
## 1.2 什么时候用`yield`而不是`return`？
`yield`语句会【**<font color=orange>暂停</font>**】函数的执行并将语句此时的运算结果返回给调用方，但会保留当前状态，以使函数可以再中断的地方继续执行。当恢复时，该函数将在最后一次`yield`运行后立即继续执行。这样，就可以**随着时间的推移产生一系列值**，一个接一个地返回给调用方，而不是像列表那样将运算结果一次性返回给调用方（比如用`return`实现）。

注意：yield是【暂停】，return是【终止】！

<font color=red>return将指定的值发送回其调用方，而Yield可以产生一系列值。当我们要遍历一个序列，但又不想将整个序列存储在内存中时，应该使用yield。</font>

---
# 2 迭代器与生成器 
## 2.1 可迭代对象（iterables）与 迭代器（Iterators）
1. **可迭代对象的定义**

- 一次迭代能够返回集合中的一个元素。比如，在for循环中迭代字符串、列表（list）、元组（tupple）等有顺序集合或者字典（dict）、集合（set）等非顺序集合中的元素。


2. **迭代器（Iterator）**

- 迭代器是一个对象，其中包含可计数的值。
- 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
- 迭代器有两个基本的方法：`iter()` 和 `next()`。
- 字符串、列表（list）、元组（tupple）、字典（dict）、集合（set）等对象都可用于创建迭代器。

看一个例子：

```python

list_example = [1,2,3] # 使用列表（list）构建可迭代对象
list_example_iterator = iter(list_example) # iter()方法构造迭代器

# 迭代器的next()方法进行迭代
print("第一次迭代结果：{}".format(next(list_example_iterator)))
print("第二次迭代结果：{}".format(next(list_example_iterator)))
print("第三次迭代结果：{}".format(next(list_example_iterator)))
```
输出为：

```shell
第一次迭代结果：1
第二次迭代结果：2
第三次迭代结果：3
```
如果我们继续迭代会出现什么问题呢？

```python
print("第四次迭代结果：{}".format(next(list_example_iterator)))
```
报错：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200326112357294.png)
另一种实现方式：

```python
import sys
list_ = [1,2,3]
list_iter = iter(list_)
while True:
    try:
        print("迭代结果：{}".format(next(list_iter)))
    except StopIteration:
        sys.exit()
```
输出：

```python
迭代结果：1
迭代结果：2
迭代结果：3
```

<font color=red>由上例分析可知，`iter()`方法构造迭代器，`next()`方法进行迭代，每次迭代返回可迭代对象（序列，上例中用列表演示，也可以使用字符串、字典等其他可迭代对象）中的一个元素，最大迭代次数是构造的可迭代对象的长度，再进行迭代会报错并提示迭代终止。</font>

---
## 2.2 生成器函数（generator function）与生成器（generator）
在 Python 中，使用了 yield 的函数被称为生成器函数（generator），生成器函数实例化后是生成器。

跟普通函数不同的是，**生成器是一个返回迭代器的函数**，只能用于迭代操作，更简单的理解：**生成器就是一个迭代器**。

看一个斐波那契数列（从第3项开始，每一项都等于前两项之和。）的例子：

```python
import sys
 
def fibonacci(n): # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a # 使用yeild 具体用法请看下文第二部分
        a, b = b, a + b
        counter += 1
        
f = fibonacci(10) # f是一个迭代器，由生成器返回生成
 
while True:
    try:
        print (next(f), end=" ") # 打印每次迭代的返回值，注意next()方法
    except StopIteration:
        sys.exit()
```
执行以上程序，输出结果如下：

```shell
0 1 1 2 3 5 8 13 21 34 55
```
此处只需明白生成器的概念（使用包含`yield`的函数是生成器函数，生成器函数实例化后是生成器，生成器是可迭代的）即可，关于`yield`的使用请看下文第二部分。

---

# 3. 如何使用yield？
`yield` 在 Python 生成器中使用。生成器函数的定义类似于普通函数，但是每当需要生成值时，它都使用 `yield` 关键字而不是return来生成。如果定义的函数中包含 `yield`，则该函数将自动成为生成器函数。

## 3.1 如何判断自定义函数是否为生成器？
我们使用 2.2 节提到的斐波那契数列的例子来看一下：

```python
def fibonacci(n): # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
        
f = fibonacci(10) # f是一个迭代器，由生成器返回生成
 
# 查看是否是生成器函数       
from inspect import isgeneratorfunction 
print(isgeneratorfunction(fibonacci))  
```
运行上例，返回 `True`，说明定义的函数是生成器。

---
## 3.2 如何区分生成器函数与生成器

注意区分 `fibonacci` 和 `fibonacci(10)`。
`fibonacci` 是一个 生成器函数（generator function），而 `fibonacci(10)` 是调用 `fibonacci` 返回的一个生成器，两者就好比**类的定义**和**类的实例**的区别：

```python
def fibonacci(n): # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
        
f = fibonacci(10) # f是一个迭代器，由生成器返回生成

# 查看是否是生成器
import types
print(isinstance(fibonacci, types.GeneratorType))        
print(isinstance(fibonacci(10), types.GeneratorType)) 
# 查看是否可迭代
from collections import Iterable
print(isinstance(fibonacci, Iterable))        
print(isinstance(fibonacci(10), Iterable)) 

```
运行上例，输出：

```python
False 
True
False 
True
```
<font color=red>说明“未实例化”生成器函数`fibonacci()`不是生成器，自然也就是不可迭代的，“实例化”后的生成器`fibonacci(5)`是生成器，所以是可以迭代的。</font>

如果我们注释掉 `yield`，替换为`print()`，会发生什么？

```python
def fibonacci(n): # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        #yield a
        print(a)
        a, b = b, a + b
        counter += 1
 
# 查看是否是生成器函数       
from inspect import isgeneratorfunction 
print(isgeneratorfunction(fibonacci))        

# 查看是否是生成器（是否可迭代）
from collections import Iterable
print(isinstance(fibonacci, Iterable))        
print(isinstance(fibonacci(5), Iterable))   

```
运行上例输出：

```python
False
False
0
1
1
2
3
5
False
```

可以看出，不使用`yield`关键字的函数已经不是生成器函数，实例化后也不是生成器，并且不可迭代。

---
## 3.3 生成器特性
每次调用 `fibonacci()`(生成器函数)都会生成一个新的生成器实例（`比如fibonacci(10)`），各实例之间互不影响：
```python
import sys
 
def fibonacci(n): # 生成器函数
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a # 使用yeild 具体用法请看下文第二部分
        a, b = b, a + b
        counter += 1
        
f1 = fibonacci(5) # 实例化生成器函数，构造生成器，生成器是可迭代的，则 f 是迭代器
f2 = fibonacci(6) 
while True:
    try:
        print ("f1:{}\n".format(next(f1)), end=" ") 
        print ("f2:{}\n".format(next(f2)), end=" ")
    except StopIteration:
        sys.exit()
```
执行以上程序，输出结果如下：

```shell
f1:0
 f2:0
 f1:1
 f2:1
 f1:1
 f2:1
 f1:2
 f2:2
 f1:3
 f2:3
 f1:5
 f2:5
```
可以看出生成器之间互不影响。
`return` 的作用：在一个生成器函数中，如果没有 `return`，则默认执行至函数完毕，如果在执行过程中 `return`，则直接抛出 `StopIteration` 终止迭代。

---
## 3.4 yield 使用实例：文件读取

```python
def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return
```

关于yield的使用有更复杂的用法，本文仅仅对yield关键字的基本用法做了解释。

---
# 总结
本文代码在python3.6环境中调试通过。

本文介绍了`return`和`print()`的区别，什么时候用`yield`而不是`return`，可迭代对象和迭代器，生成器函数和生成器。

1. 那么我们总结一下，`print()`不会终止程序执行，`return`则会终止。
2. 当我们有需要一个一个的序列化输出时，使用yield关键字。
3. 可迭代对象有字符串、列表、字典、元组、集合等。如果不是函数，使用`iter(可迭代对象)`方法创建迭代器，使用`next()`方法进行迭代。
4. 如果是定义的函数，我们使用yield关键字让这个函数变为生成器函数，然后将这个函数实例化之后，就变为生成器，用这个生成器给变量赋值，则这个变量就是迭代器（简单粗暴理解：【迭代器就是生成器】），迭代器执行调用生成器函数中的功能进行运算。

再看一下斐波那契数列的例子：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20200326131636787.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl8zOTY1Mzk0OA==,size_1,color_FFFFFF,t_70)

---
> 参考：
> 1. [Python Return Statement](https://guide.freecodecamp.org/python/return-statement/)
> 2. [What is the purpose of the return statement?](https://stackoverflow.com/questions/7129285/what-is-the-purpose-of-the-return-statement)
> 3. [python解释器](<https://www.liaoxuefeng.com/wiki/1016959663602400/1016966024263840>)
> 4. [When to use yield instead of return in Python?](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/)
> 5. [python3 迭代器与生成器](https://www.runoob.com/python3/python3-iterator-generator.html)
> 6. [python iterables](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html)
> 7. [python's Iterators](https://www.w3schools.com/python/python_iterators.asp)
> 8. [python yield 使用浅析](https://www.runoob.com/w3cnote/python-yield-used-analysis.html)

