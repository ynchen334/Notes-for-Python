# 文件读取
# f = open('workfile', 'w')
# 第一个参数是文件名，第二个是读取方式,默认r
# r = 只读   w = 只能写入，现有同名文件会被覆盖（不存在则创建，存在则清空）
# a = 追加内容   r+ = 读写，但不自动创建文件    b = 二进制
# 注意：r+写完后，指针会往后移，想从头读需要f.seek(0)
#默认etf-8，可以用encoding=指定

# 读取完后，要用f.close()关闭，或者用with：
with open('file.txt') as f:
    s1 = f.read(5)
    f.readline()  #读完hello后，指针移到行末尾隐藏的\n,需要再readline一次，切到下一行
    s2 = f.readline()


print(s1)
print(s2)

    

#  f.read(size)  size是可选参数，为负时读取整个文件
# readlines()将内容转为列表，每行为一个元素
# 只返回字符串

#seek(offset, whence) 改变文件对象的位置
# 通过向参考点添加 offset 计算位置；参考点由 whence 参数指定
# whence = 0从开头计算，  =1从当前位置计算   =2从末尾计算
# f.seek(5)      定位到文件中的第 6 个字节
# f.seek(-3, 2)  定位到倒数第 3 个字节

#文件写入
#f.write(s)  换行需要手动添加
#f.writelines(lines)   讲一个元素为字符串的列表整体写入文件