# 2. 编写程序，生成包含20个随机数的列表，然后将前10个元素升序排列，后10个元素降序排列，并输出结果。
rand_list = [random.randint(0, 100) for i in range(20)]

sorted_list = []
sorted_list.extend(sorted(rand_list[:10]))
sorted_list.extend(sorted(rand_list[10:], reverse=True))
sorted_list

"""
[9, 12, 34, 38, 43, 57, 85, 98, 98, 100, 92, 89, 65, 60, 52, 51, 31, 20, 5, 3]

"""