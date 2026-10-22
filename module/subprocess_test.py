#核心概念和安全注意事项
#创建新的子进程，用来和新的子进程交互，获取子进程的输入输出错误和状态检查码
#尽量不要用shell=True

import subprocess
#基础操作
#如何运行外部的命令  subprocess.rum()实现
#subprocess.run(arggs,shell=True/False, check=False/True, capture_output=False/True, text=False/True)
#查看当前目录下，有哪些文件和文件夹
result = subprocess.run(["ls"], shell=True)
print(f"result:>>>\n{result}")    #CompletedProcess(args=['ls'], returncode=0(返回状态码是0就是运行成功，1是运行失败)

# 使用shell特性，通配符处理
result_1 = subprocess.run(["ls *.py"], shell=True)
print(f"result:>>>\n{result_1}")

print('=' * 20)

#获取命令的输出
#最常用
#ls -l的输出
#windows用cmd = ["cmd", "/c", "dir"] cmd表示调用cmd，/c表示执行后面的命令后立即退出cmd
#capture_output=True表示捕获命令执行后的屏幕输出保存到res1，不会输出到终端
#text=True将捕获到的结果解码为字符串
#check=True如果执行的命令报错，python会自动抛出异常
#shell=True有安全风险，不建议用，如果shell=False，"ls -a"无法执行，需要写成["ls", "-a"]

#shell=True配合完整的字符串"ping -c 2 localhost"
#False配合["ping", "-c", "2", "localhost"]

cmd = "ls -a"
res1 = subprocess.run(cmd, capture_output=True, text=True, check=True, shell=True)
print(res1)   #直接输出的格式不方便阅读

print(f"标准输出：{res1.stdout}")   #标准输出
print(f"标准错误：{res1.stderr}")

#获取ping的测试
print("-" * 10)
ping_cmd = ["ping", "-c", "2", "localhost"]
#ping_cmd = "ping -c 2 localhost"
res2 = subprocess.run(ping_cmd, capture_output=True, text=True, check=True, shell=False)
print(res2.stdout)
print(res2.stderr)

#windows执行ls这种指令时，前面要加"cmd","/c"，表示用cmd执行，-c表示执行完退出，执行ping不用加，因为ping是一个独立的程序文件，并且自动出，Windows指令只能写成列表，不能写成连续的字符串

#错误处理和返回码
# check=True, CalledProcessError错误，可以捕捉失败时的returncode，stdout，stderr
print("===错误处理===")
try:
    res = subprocess.run(["ls"], capture_output=True, text=True, check=True)
except FileNotFoundError as e:                    #找不到命令文件抛出
    print(e)
except subprocess.CalledProcessError as cpe:      #找到文件但是运行失败
    print(f"错误输出码：{cpe.returncode}")  
    print(f"错误输出：{cpe.stdout}")
else:
    print("命令运行成功")


#如何给命令提供输入
#通过input参数给命令提供输入（文本模式下是字符串，二进制模式下是bytes）
#假设下载需要给python解释器输入代码
print("===给命令提供输入===")
python_code = """
    print("hello from subprocess!")
    print(1+2+3)
"""

res3 = subprocess.run(["python3"], input=python_code, capture_output=True, text=True)
print(f"输出是：{res3.stdout}")
print(res3)

#高级用法
#popen   边执行边读取输出
#是底层类，比run更灵活
#需要实时获取输出的场景，需要与命令进行持续交互的场景
#popen.poll()检查命令是否完成，返回None就表示未完成，返回returncode就表示已经完成
#popen.wait()等待命令完成，实现阻塞功能
#Poppen.communicate(input=None) 发送输入，获取输出/错误
#Popprn.stdout/stderr 标准的输出或错误的文件对象
print("Poppen 实时获取输出")
ping_cmd = ["ping", "-c", "4", "localhost"]
with subprocess.Popen(ping_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1, universal_newlines=True) as proc:
    for line in proc.stdout:
        print(line, end="")
    print(proc.pid)  #查看进程号

# stdout=subprocess.PIPE 表示管道，输出结果不要显示在终端，而是通过管道传给python
#  bufsize=1  1行缓冲，输出一行立即刷新，保证实时读取
# universal_newlines=True  类似text=true，一般不用加

#常见应用场景
#调用系统工具：git ffmpeg
#检查系统状态：ping检查网络，df检查磁盘空间，ps查看进程状态
#批量处理文件：shell
#自动化任务：corn或者Windows任务计划程序
#调用其他脚本