
"""
编写代码，实现一个栈（Stack）类。

栈是只能在一端插入和删除数据的序列，它按照先进后出的原则存储数据，先进入的数据被压入栈底，最后的数据在栈顶，
需要读数据的时候从栈顶开始弹出数据，最后一个数据被第一个读出来。


---
1. 栈（Stack）与队列（Queue）是两种基本的数据结构，同为容器类型。两者的区别在于：栈为后进先出，对列为先进先出。
2. 栈与队列没有查询某一位置元素的操作，但它们是按顺序排列的。
3. 在Python中，可以使用list实现栈，因为list是线性数组，在末尾插入和删除一个元素所使用的的时间均为 O(1)。
4. 也可以使用链表实现。

"""

############################## 1. Python List 实现栈 ##############################

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
        
        
############################## 2. 链表实现(最小)栈 ##############################
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
        
############################## 3. Python List 实现队列 ##############################
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
        
        
############################## 4. 链表实现队列 ##############################
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
