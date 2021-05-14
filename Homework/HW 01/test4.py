# 4. 编写程序，实现分段函数计算，如下所示:
def piecewise_func(x):
    """
    分段函数计算
    """
    if x < 0:
        return 0
    elif x >= 5 and x < 10:
        return 3 * x - 5
    elif x >= 10 and x < 20:
        return 0.5 * x - 2
    else:
        return 0
    
print(piecewise_func.__doc__)
piecewise_func(18)

"""
分段函数计算
    
7.0
"""