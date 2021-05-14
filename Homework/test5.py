import chardet
import argparse

parser=argparse.ArgumentParser(description = 'change encoding')
parser.add_argument('name', default = 'file1.txt', help = 'file name')
parser.add_argument('encode', default = 'utf-8', help = 'encoding method')
args=parser.parse_args()


with open(args.name, 'rb') as f:
    file_read = f.read()
    if not args.encode:
        args.encode = chardet.detect(file_read)['encoding']
    # 打印原编码格式
    print("初始编码格式为：")
    print(args.encode)
    
print("args.name：", args.name)
# 以原编码格式打开
f = open(args.name, "r", encoding=args.encode)      
text=f.read()
f.close()

# 以utf-8编码格式打开
f = open(args.name, 'w', encoding='utf-8')         
f.write(text)
f.close()

# 输出新的编码格式以检查是否转换成功
with open(args.name, 'rb') as f: 
    print("新的编码格式为：")
    print(chardet.detect(f.read())['encoding'])
    
# 命令行运行
# python test5.py "file1.txt" "utf-8"

# 输出：

"""
初始编码格式为：
utf-8
args.name： file1.txt
新的编码格式为：
ascii
"""
