# 1. 编写函数，接收一个字符串，分别统计大写字母、小写字母、数字、其他字符的个数，并以元组的形式返回结果。

def char_type_statistic(string):
    stac_dict = {}
    stac_dict["upper_letter"] = 0
    stac_dict["lower_letter"] = 0
    stac_dict["digit"] = 0
    stac_dict["others"] = 0
    
    for elem in string:
        if elem.isupper():
            stac_dict["upper_letter"] += 1
        
        elif elem.islower():
            stac_dict["lower_letter"] += 1
            
        elif elem.isdigit():
            stac_dict["digit"] += 1
            
        else:
            stac_dict["others"] += 1
    
    return stac_dict
    
input_str = input("Please input string: \n")
stac_dict = char_type_statistic(input_str)
print(stac_dict)

# 输出：
"""
Please input string: 
Hello, World!
{'upper_letter': 2, 'lower_letter': 8, 'digit': 0, 'others': 3}
"""


