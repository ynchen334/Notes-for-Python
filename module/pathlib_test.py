#用于读取文件
from pathlib import Path    #引入Path类
path = Path('pi.txt')          #实例化
contents = path.read_text()    #读到字符串
print(contents)
print(type(contents))
print(contents[:10])

path1 = Path('./my_utils/pwd.txt')
s1 = path1.read_text()
print(s1)