#字符串
s1 = "aaa"
s2 = 'aaa'
s3 = """aaa"""

#索引和切片(从0开始)
s = "python是世界上最好的编程语言"
print(s[0])
#可以向左
print(s[-3])

#切片的规则 [start：end]
#从start开始，end取不到
print(s[1:4])   #yth
#前或后不写代表到边界
print(s[:7])    
print(s[4:])    
print(s[:])       #字符串重复一遍
# [start:step:end]
print(s[::2])
#step如果是负数，从右向左
#可用于判断回文
print(s[-1:-5:-1])      #言语程编

#f-string
name = "world"
print(f"hello {name}")

#字符串内置方法

#1.lstrip([chars])
print('[' + "  hi  ".lstrip() + ']')   #去左边的空格
#可选去掉边上的字符，并且不受字符顺序的影响
#去右边用rstrip()，两边用strip()

#2.len(str) 返回字符串长度
#3.lower(str) 将字符串所有大写字母转为小写   upper()
#4.max(str) 返回最大的字母

#str.replace(old, new[, max])
#old -- 将被替换的子字符串。
#new -- 新字符串，用于替换old子字符串。
#max -- 可选字符串, 替换不超过 max 
s5 = "www.baidu.com"
print(s5.replace("baidu", "google"))

#str.split(str="", num=string.count(str))  返回列表
#str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
#num -- 分割次数，如果设置了这个参数，则最多分割成 maxsplit+1 个子字符串。默认为 -1, 即分隔所有
str = "this is string example....wow!!!"
print (str.split())        # 默认以空格为分隔符
print (str.split('i',1))   # 以 i 为分隔符
print (str.split('w'))     # 以 w 为分隔符

# str.find(str, beg=0, end=len(string))     index同find，找不到会报错     rfind从右开始找
#str -- 指定检索的字符串
#beg -- 开始索引，默认为0。
#end -- 结束索引，默认为字符串的长度。
str1 = "Runoob example....wow!!!"
str2 = "exam"
print (str1.find(str2))
print (str1.find(str2, 5))
print (str1.find(str2, 10))   #找不到返回-1

#isdigit()
#isupper()
#isalpha()     判断是否全为数字，字母，大写
#capitalize()  首字母大写
#title()       每个单词首字母大写

#str.join(sequence) 将序列中的元素以指定的字符连接生成一个新的字符串
#!/usr/bin/python3
s6 = "-"
s7= ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s6.join( seq ))   #r-u-n-o-o-b
print (s7.join( seq ))   #runoob
