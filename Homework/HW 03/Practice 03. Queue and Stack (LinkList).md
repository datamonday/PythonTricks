# Practice Content

编写如下两个程序。程序源文件名为test1.py、test2.py。

1. 编写代码，实现一个栈（Stack）类。栈是只能在一端插入和删除数据的序列，它按照先进后出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶，需要读数据的时候从栈顶开始弹出数据，最后一个数据被第一个读出来

---
学习 pickle 和 unittest 两个模块，并在自己写的程序test1.py、test2.py中使用这两个模块
有兴趣的同学还可以学用 shelve 模块

## 1. Stack class
![image.png](attachment:image.png)

### 1.1 基本概念
1. 栈（Stack）与队列（Queue）是两种基本的数据结构，同为容器类型。两者的区别在于：栈为后进先出，对列为先进先出。

2. 栈与队列没有查询某一位置元素的操作，但它们是按顺序排列的。

3. 在Python中，可以使用list实现栈，因为list是线性数组，在末尾插入和删除一个元素所使用的的时间均为 $O(1)$。

4. 也可以使用链表实现。

---
### 1.2 基本操作

1. 初始化 init
2. 入栈 push
3. 出栈 pop
4. 判断栈是否为空 is_empty
5. 获取栈顶元素 top
6. 获取栈的容量 size
7. 打印栈中元素 elem
8. 清空栈 empty
9. 销毁栈 destroy

---
### 1.3 List 实现 栈


```python
class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if len(self.stack):
            self.stack.pop()
        else:
            raise LookupError("Stack is empty now!")
    
    def is_empty(self):
        if len(self.stack):
            return False
        else:
            return True
        
    def get_top_elem(self):
        return self.stack[0]
    
    def get_size(self):
        return len(self.stack)
    
    def display_elem(self):
        print(self.stack)
        
    def empty(self):
        self.stack = []
        
    def destroy(self):
        del self.stack
```


```python
new_stack = Stack()
```


```python
new_stack.push(1)
```


```python
new_stack.push(2)
```


```python
new_stack.push(3)
```


```python
new_stack.pop()
```


```python
new_stack.is_empty()
```




    False




```python
new_stack.get_top_elem()
```




    1




```python
new_stack.get_size()
```




    2




```python
new_stack.display_elem()
```

    [1, 2]
    


```python
new_stack.empty()
```


```python
new_stack.destroy()
```


```python
new_stack
```




    <__main__.Stack at 0x1a1ae98c370>




```python
# 销毁之后，无法进行栈的操作
new_stack.push(1)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-16ead85fdd3c> in <module>
    ----> 1 new_stack.push(1)
    

    <ipython-input-1-bda02de92406> in push(self, value)
          4 
          5     def push(self, value):
    ----> 6         self.stack.append(value)
          7 
          8     def pop(self):
    

    AttributeError: 'Stack' object has no attribute 'stack'


### `->` marks the return function annotation

These are function annotations covered in PEP 3107(https://www.python.org/dev/peps/pep-3107/).


```python
def kinetic_energy(m:'in KG', v:'in M/S')->'Joules': 
    
    return 1/2*m*v**2

kinetic_energy.__annotations__
```




    {'m': 'in KG', 'v': 'in M/S', 'return': 'Joules'}




```python
def f(x: float) -> int:
    
    return int(x)

f.__annotations__
```




    {'x': float, 'return': int}



### 1.4 单向链表实现 最小栈
- Reference: https://leetcode-cn.com/problems/min-stack/solution/python-lian-biao-shi-xian-zhan-by-fu-hao-tong/
- https://leetcode-cn.com/problems/min-stack/solution/min-stack-fu-zhu-stackfa-by-jin407891080/


```python
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.min_value = None

class MinStack:
    def __init__(self):
        self.value = None
        self.next = None
        
    def push(self, value: int) -> None:
        p = Node(value)
        p.next = self.next
        self.next = p
        # 表长大于1时
        if p.next:
            p.min_value = min(value, p.next.min_value)
        else:
            p.min_value = value
    
    def pop(self) -> None:
        tmp = self.next
        if tmp != None:
            self.next = tmp.next
        return
    
    def get_top_elem(self) -> int:
        if self.next != None:
            return self.next.value
        return None
    
    def get_min_elem(self) -> int:
        p = self.next
        return p.min_value
```


```python
new_stack = MinStack()
```


```python
new_stack.push(1)
```


```python
new_stack.push(2)
```


```python
new_stack.push(3)
```


```python
new_stack.pop()
```


```python
new_stack.get_top_elem()
```




    2




```python
new_stack.get_min_elem()
```




    1



### 1.5 List 实现队列


```python
class Queue(object):
    def __init__(self):
        self.queue = []
        
    def enqueue(self, value):
        self.queue.append(value)
        
    def dequeue(self):
        self.queue.pop(0)
        
    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False
    
    def get_size(self):
        return len(self.queue)
    
    def display_elem(self):
        print(self.queue)
        
    def empty(self):
        self.queue = []
        
    def destroy(self):
        del self.queue
```


```python
new_queue = Queue()
```


```python
new_queue.enqueue(1)
```


```python
new_queue.enqueue(2)
```


```python
new_queue.enqueue(3)
```


```python
new_queue.dequeue()
```


```python
new_queue.is_empty()
```




    False




```python
new_queue.get_size()
```




    2




```python
new_queue.display_elem()
```

    [2, 3]
    


```python
new_queue.empty()
```


```python
new_queue.destroy()
```


```python
new_queue.enqueue(1)
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-42-b593db2f36c6> in <module>
    ----> 1 new_queue.enqueue(1)
    

    <ipython-input-30-1f2346df7582> in enqueue(self, value)
          4 
          5     def enqueue(self, value):
    ----> 6         self.queue.append(value)
          7 
          8     def dequeue(self):
    

    AttributeError: 'Queue' object has no attribute 'queue'


### 1.6 链表实现队列

思路：定义一个单链表，其头结点的指针域指向首元结点，头结点的数据域指向链表的尾结点，时间复杂度为 $O(1)$。如图所示：

![image.png](attachment:image.png)


```python
a1 = [5, 4, 3, 2, 1, 2, 3, 4, 5]
a1.sort()
a1
```




    [1, 2, 2, 3, 3, 4, 4, 5, 5]




```python
# 无返回值
b1 = a1.sort()
b1
```


```python
a2 = [5, 4, 3, 2, 1, 2, 3, 4, 5]
sorted(a2)
```




    [1, 2, 2, 3, 3, 4, 4, 5, 5]




```python
# 有返回值
b2 = sorted(a2)
b2
```




    [1, 2, 2, 3, 3, 4, 4, 5, 5]




```python
class Head(object):
    def __init__(self):
        self.left = None
        self.right = None

class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue(object):
    def __init__(self):
        # 初始化头结点
        self.head = Head()

    def enqueue(self, value):
        # 新建插入元素结点
        new_node = Node(value)
        # 定义头指针
        p = self.head
        # 如果头结点之后不为None，说明链表中有元素
        if p.right:
            temp = p.right
            p.right = new_node
            temp.next = new_node
        # 如果为None，说明表为空，只有头结点
        else:
            p.right = new_node
            p.left = new_node

    def dequeue(self):
        p = self.head
        
        # 只有一个元素
        if p.left and (p.left == p.right):
            temp = p.left
            p.left = p.right = None
            return temp.value
        # 不止一个元素
        elif p.left and (p.left != p.right):
            # 最先入队的元素
            temp = p.left
            p.left = temp.next
            return temp.value

        else:
            raise LookupError('Queue is empty now!')

    def is_empty(self):
        if self.head.left:
            return False
        else:
            return True

    def top(self):
        if self.head.left:
            return self.head.left.value
        else:
            raise LookupError('Queue is empty now!')
```


```python
new_queue = Queue()
```


```python
new_queue.enqueue(1)
new_queue.enqueue(2)
new_queue.enqueue(3)
```


```python
new_queue.dequeue()
```




    1




```python
new_queue.is_empty()
```




    False


