# tempfile 标准库学习:临时文件和临时目录的创建和使用
# 1、临时文件创建(核心功能)
# (1)临时文件
# (2)文件
# 2、临时目录创建(批量临时文件)

import tempfile as tf
import pathlib

#临时文件的创建
#自动删除的临时文件的创建
with tf.TemporaryFile(mode="w+", encoding="utf-8") as f1:
    f1.write("111\n")
    f1.write("222\n")
    f1.write("333\n")
    f1.seek(0)
    content = f1.read()
    print(content)
    fname1 = str(f1.name)  #临时文件名可能是纯数字，先强转一下，防止创建Path对象时报错
#检测是否自动删除
print(fname1)
fname1 = pathlib.Path(fname1)
if fname1.exists():
    print("exists")
else:
    print("not exist")


#非自动删除的临时文件的创建
with tf.NamedTemporaryFile(mode="w+", encoding="utf-8", delete=False) as f2:
    fname2 = f2.name
    f2.write("aaabbbccc")
    f2.seek(0)
    content = f2.read()
    print(content)

fname2 = pathlib.Path(fname2)
if fname2.exists():
    print("exist")
else:
    print("not")

#temporaryfile，创建匿名文件，调用name时，返回的是文件描述符（整数）（适合用完就删）
#namedtemporaryfile，创造具名文件


#临时目录的创建
with tf.TemporaryDirectory() as dir:
    print(dir)     #/tmp/tmpn4_o6mc2
    dir_obj = pathlib.Path(dir)
    dir_obj = dir_obj/"some"
    dir_obj.mkdir()
    lists = dir_obj.iterdir()
    print(list(lists))
if dir_obj.exists():
    print("yes")
else:
    print("no")