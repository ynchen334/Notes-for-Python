# pathlib标准库学习:
# 1、路径的获取
# (1)获取当前用户路径
# (2)获取当前工作目录
# 2、路径的操作
# (1)路径拼接
# (2)获取各个属性部分 文件名-含后缀-文件后缀-父目录
# 3、文件和路径的基础操作
# (1)是否存在/是否是文件/路径
# (2)创建目录
# (3)创建文件
# (4)重命名/移动文件
# (5)删除文件/目录
# 4、目录遍历和文件查找
# (1)遍历当前目录
# (2)匹配当前目录文件
# (3)递归匹配所有子目录
# 5、简化文件读写操作
# (1)快速读文件
# (2)快速写文件

from pathlib import Path

# 路径的获取
p1 = Path("/home/yinuo/labs/PythonLab/module/pi.txt")
print(p1)
print(type(p1))

#返回当前用户主目录
p2 = Path.home()  
print(p2)

#返回上级目录，属性没有括号
#只根据输入的字符串来，如果是单个的文件名就返回".""
print(f"parent:{p1.parent}")     
print(list(p1.parents))    #返回一个列表，包含所有层级目录

#获取当前工作路径pwd
p3 = Path.cwd()
print(p3)

#路径拼接
#路径不存在也可以
p4 = Path("./usr/admin")
print(p4)
p5 = p4/"download" / "xunlei"
print(p5)
p6 = p5/"main.py"
#得到拼接后的各属性部分
file_basename1 = p6.name       #带后缀的文件名
file_basename2 = p6.stem       #不带后缀的文件名
file_suffix = p6.suffix        #文件后缀名
file_father_dir = p6.parent    #目录
print(file_basename1)
print(file_basename2)
print(file_suffix)
print(file_father_dir)

# 路径判断和文件系统操作
p7 = Path("pi.txt")

#判断路径和文件是否存在
if (p7.exists()):
    print(("exists"))
else:
    print("not exist")

#判断是文件还是路径
def judge(obj):
    if obj.is_file():
        print("file")
    else:
        if obj.is_dir():
            print("dir")
        else:
            print("not exist")

judge(p7)
judge(p5)
p8 = Path.cwd()
judge(p8)

#创建目录      dirname.mkdir()
create_dir_1 = Path("data")
create_dir_2 = create_dir_1/"input"
create_dir_2.mkdir(parents = True, exist_ok = True)    #parents能否递归创建，exist_ok存在是否报错

#创建文件    filename.touch()
create_file_1 = create_dir_2/"input.txt"
create_file_1.touch(exist_ok = True)

#重命名文件
file1 = Path("data/input/input.txt")
print(file1)
file1.rename(file1.parent / "new_input.txt")

#剪切，前提是目录存在且目录内没有同名文件
file2 = Path("data/input/new_input.txt")
file2.rename("data/new_input.txt")

#删除文件
obj_new_input = Path("./data/new_input.txt")
print(obj_new_input.resolve())          #将相对路径补全为绝对路径
obj_new_input.unlink()                  #相当于os.remove()

#删除目录
dir_obj = Path("./some")
if dir_obj.exists():
    dir_obj.rmdir()
else:
    print("dir not exist")

#目录遍历和文件查找
#主要替代os.walk()
base_dir = Path("test_project")
(base_dir/"src").mkdir(parents = True, exist_ok=True)
(base_dir/"docs").mkdir(parents=True, exist_ok=True)
(base_dir/"src"/"main.py").touch()
(base_dir/"docs"/"readme.md").touch()

print("-" * 10)

#查找当前路径下内容（非递归）
for item in base_dir.iterdir():
    print(item, type(item))       #每个item是一个Path类对象

print("-" * 10)
#查找当前目录下某格式文件（非递归）
for py in base_dir.glob("*.py"):
    print(py)

print("-" * 10)
#查找当前目录下所有某格式的文件（递归）
for py in base_dir.rglob("*.py"):
    print(py)


#文件的写操作
file_Path = Path("pi1.txt")  
file_Path.write_text("abc\nhello world\n你好")        #覆盖，没有自动创建，存在不报错

#文件的读操作
res = file_Path.read_text(encoding="utf-8")
print(res)


