import os
#路径操作
#获取当前路径   os.getcwd()
curr_cwd = os.getcwd()
print (curr_cwd)
#路径拼接    os.path.join()
res_cwd = os.path.join(curr_cwd, "os_test.py" )
print(res_cwd)
#拆分路径     os.path.dirname/basename()
a = os.path.dirname(res_cwd)    #路径
b = os.path.basename(res_cwd)   #文件名
print(a)
print(b)
#判断路径是否存在     os.path.exists()
test_path = "/usr/opt"
if os.path.exists(test_path):      #返回布尔值
    print("exist")
else:
    print("not exist")

#判断是路径还是文件名    os.path.isfile/isdir()
print(os.path.isfile(a))
print(os.path.isdir(a))
#获取文件大小
#单位是字节     os.path.getsize()
size_b = os.path.getsize(b)
print(size_b)


#目录操作
#增加一个目录
#非递归增加     os.mkdir()
os.mkdir("test_dir")    #存在会报错
#使用递归增加目录       os.makedirs()
os.makedirs("test_dir2", exist_ok = True)    #存在也不报错
os.makedirs("test_dir2/abc", exist_ok = True) 
#删除目录
os.rmdir("test_dir")    #只能以非递归形式删除
#os.rmdir("test_dir2")   #若目录非空则报错
#递归删除
os.removedirs("test_dir2/abc")   #从内到外删除，不能直接删除外层文件夹

#查找
#非递归查找
ls1 = os.listdir(".")    #当前文件夹的文件（非递归） 列表形式
print(ls1)
#递归查找       
ls2 = os.walk(".")
#print(list(ls2))               #返回迭代器
for a,b,c in ls2:
    print(f"{a}: folder{b}, files{c}")


#环境变量和系统操作（重要）
#获取环境变量
envs = os.environ.get("PATH")
#print(envs)
print(type(envs))
#列表化环境变量
path_envs = envs.split(":")
for cho in path_envs:
    print(cho)

#设置临时环境变量
os.environ["MY_SET_ENV"] = "MY_SET_ENV"
print(os.environ.get("MY_SET_ENV"))

#获取系统信息
#posix = MACOS/LINUX，NT = windows
info_pc = os.name
print(info_pc)

#执行系统命令
sys_obj = os.system("tree")  #sys_obj储存退出状态码，0代表执行成功
print(sys_obj)
