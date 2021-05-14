# 2. 编写函数，可以接收任意多个整数并输出其中的最大值和所有整数之和。

def max_sum_of_int_list(input_list):
    sum_elem = 0
    
    # 从键盘输入的值
    input_list = input_list.split(",")
    max_elem = int(input_list[0])
    for elem in input_list:
            sum_elem += int(elem)
            if int(elem) > max_elem:
                max_elem = int(elem)
                
    return sum_elem, max_elem
 
input_list = input("Please input number list(split by ,):\n")
sum_elem, max_elem = max_sum_of_int_list(input_list)
print("Sum of input:", sum_elem)
print("Max of input:", max_elem)
 
# 输出：
"""
Please input number list(split by ,):
1,2,3,4,5,6,7,8,9,10
Sum of input: 55
Max of input: 10
"""