import sys
#核心概念
#sys是python的内置库，主要负责：
#和python解释器交互，和操作系统交互，管理python运行的环境
#常用函数学习

#常用功能
#sys.argv() 脚本参数的入口，储存命令行传递给脚本的所有参数
als = sys.argv     #list
print(f"命令行所有参数为{als},type:{type(als)}")
print(f"第一个参数：{als[0]}")   #第一个参数是当前文件的文件名
#处理参数
if len(als) > 1:
    print(f"传递的参数为：{als[1]}")
    try:
        index = 1
        for cho in als[1:]:
            print(f"ARGS-{index}:{cho}")
            index += 1
    except Exception as e:
        print(e)
else:
    print("没有传入参数,程序退出")
    #sys.exit(0)   #程序主动退出,里面是状态码
print("===")

#如何解决ModuleNotFoundError报错
#通常情况下，再导入python的一个模块后，python会根据sys.path中所有的路径进行查找，如果没有就报错
sys.path.append("/home/yinuo/labs")   #先添加路径再引入
import main

for i,path in enumerate(sys.path,1):   #遍历时顺便给下标索引，默认从零开始
    print(f"[{i}].{path}")


#处理标准输入，标准输出，标准错误流

# sys.stdin   标准输入
# print("请输入一行文字:", end="")
# line = sys.stdin.readline().strip()
# print(f"你的输入文字为：{line}")

# readline和input的区别：input可以自己打印前置内容，输入内容没有换行符，便于交互readline返回的内容带\n, 适合定向输入或大规模
# write和print的区别：write只能输入字符串，不会自动换行，可以返回写入了多少个字符

# sys.stdout  标准输出
sys.stdout.write("这是通过sys.stdout打印的文字\n")

# sys.stderr  标准错误流
sys.stderr.write("这是一条错误信息\n")

#如何获取系统与解释器信息
print(f"python版本信息：{sys.version}")
print(f"python版本信息-更详细:{sys.version_info}")
print(f"当前程序运行的平台:{sys.platform}")
print(f"python解释器的可执行文件路经:{sys.executable}")
print(f"python解释器的默认编码方式：{sys.getdefaultencoding()}")

#如何查看对象占用的内存空间大小
print(f"int类型占用的内存空间大小为：{sys.getsizeof(1)}")
print(f"char类型占用的内存空间大小为：{sys.getsizeof('c')}")
print(f"list类型占用的内存空间大小为：{sys.getsizeof(['a','b','d'])}")
#只是计算容器本身大小，比如说列表的大小，并不会计算列表内元素的大小

#重置递归深度的大小
#python为了防止栈溢出，默认递归深度大小为1000
print(f"当前递归深度为{sys.getrecursionlimit()}")
sys.setrecursionlimit(2000)
print(f"重置后递归深度为{sys.getrecursionlimit()}")

#system标准库的常见应用场景
# 脚本开发：用sys.argv进行传递参数，sys。exit来进行程序的主动退出
# 模块导入日志：sys.path动态添加模块所在路径
# 日志与输出：输入输出与信息调错
# 跨平台与兼容性：得到平台信息
# 性能调试：sys.getsizeof()查看对象内存大小

#实战案例-命令行系统信息工具
print("--------------------------------------")

class SystemInfoTool:
    def __init__(self):
        if len(sys.argv) < 2:
            self.show_usage()
            sys.exit(0)
        self.arg = sys.argv[1]
        
    def show_usage(self):
        print("===命令行简易信息管理工具===")
        print("参数列表：")
        print("--version")
        print("--path")
        print("--platform")
   
    def print_version(self):
        print("===version===")
        print(sys.version)
        print(f"主版本:{sys.version_info.major}, 次版本：{sys.version_info.minor}, 微版本：{sys.version_info.micro}")
    
    def print_platform(self):
        print("===platform===")
        print("sys.platform")
  
    def print_path(self):
        print("===Path===")
        for i,path in enumerate(sys.path,1):
            print(f"[{i}].{path}")

    def run(self):
        if self.arg == "--version":
            self.print_version()
        elif self.arg == "--platform":
            self.print_platform()
        elif self.arg == "--path":
            self.print_path
        else:
            print("参数错误")
            self.show_usage()
            sys.exit(1)

def test():
    SystemInfoTool()
if __name__ == "__main__":
    test()