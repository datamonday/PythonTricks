# 3.编写程序，运行后用户输入4位整数作为年份，判断其是否为闰年。
#   如果年份能被400整除，则为闰年；如果年份能被4整除但不能被100整除也为闰年。
def is_leap_year(year):
    year = int(year)
    if year < 0:
        print("请输入正确的年份！")
    elif year % 400 == 0:
        print(f"{year} 是闰年！")
    elif year % 4 == 0 and year % 100 != 0:
        print(f"{year} 是闰年！")
    else:
        print(f"{year} 不是闰年！")
    
    
year = input("请输入要判断的年份(四位整数)：\n")
is_leap_year(year)

"""
请输入要判断的年份(四位整数)：
2021
2021 不是闰年！
"""