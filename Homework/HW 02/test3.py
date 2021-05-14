# 3. 编写函数，模拟内置函数sorted()。（你需要先读内置函数 sorted() 的关方文档，搞清楚它的输入参数和输出）
def bubble_sort(arry, reverse=True):
    """
    sorted()的内部实现类似于排序算法，以冒泡排序为例进行重写
    sorted(iterable, cmp=None, key=None, reverse=False)
    ----
    param arry:输入数组
    param reverse:降序排列
    """
    len_arry = len(arry)
    for i in range(len_arry):
        for j in range(1, len_arry - i):
            if arry[j-1] > arry[j]:
                # 交换
                arry[j-1], arry[j] = arry[j], arry[j-1]
            else:
                pass
    
    if reverse:
        return arry
    else:
        # .reverse()方法对原数组操作，不带返回值，所以不能直接return 该语句！
        arry.reverse()
        return arry

arry = [5,2,1,1,3,1,4]
print(bubble_sort(arry))

# 输出：
"""
[1, 1, 1, 2, 3, 4, 5]
"""