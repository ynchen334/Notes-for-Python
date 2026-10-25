#使用psutil这个第三方模块在Python中获取系统信息
#psutil = process and system utilities
#第三方库，需要先用 pip install psutil 安装
import psutil

#获取CPU信息
#可以把 物理核心理解为真正负责计算的核心，把逻辑 CPU 理解为操作系统能够调度的计算线程
logic_cpu_count = psutil.cpu_count() # 逻辑CPU数量
print(logic_cpu_count)    #16
physical_cpu_count = psutil.cpu_count(logical=False)  # CPU物理核心
print(physical_cpu_count)   #8

#统计cpu的用户/系统/空闲时间
cpu_times = psutil.cpu_times()
print(cpu_times)
# output:scputimes(
#         user=10963.31,   #执行普通用户程序的时间
#         nice=0.0,        #执行经过 nice 优先级调整的用户进程的时间
#         system=5138.67,  #执行操作系统内核代码的时间
#         idle=356102.45   #CPU 处于空闲状态的时间
#     )

#统计cpu使用率（百分比）
for x in range(10):
    break
    print(psutil.cpu_percent(interval=1, percpu=True))
# interval=1：每次统计约 1 秒的 CPU 活动情况。
# percpu=True：分别返回每个逻辑 CPU 的使用率，而不是只返回整体使用率

# 对比	             cpu_times()	         cpu_percent()
# 作用	            获取各状态的累计时间	获取 CPU 使用率
# 返回内容	        多个时间字段	          百分比
# 是否适合实时监控	 需要自行计算时间差       	更直接
# 项目中的用途	     深入分析 CPU 活动	    展示当前 CPU 负载
#cpu_times() 提供的是累计数据，而 cpu_percent() 计算的是一段时间内 CPU 忙碌程度的比例

#获取内存信息
#使用psutil获取物理内存和交换内存信息
print(psutil.virtual_memory())  #物理内存
# svmem(
#     total=8589934592,      总物理内存
#     available=2866520064,   可用内存
#     percent=66.6,           内存使用率
#     used=7201386496,       已使用内存
#     free=216178688,        完全空闲的内存
#     active=3342192640,
#     inactive=2650341376,
#     wired=1208852480
# )

print(psutil.swap_memory())    #查看交换空间
# Swap:临时存放部分内存数据的备用空间，通常位于磁盘上，访问速度比 RAM 慢得多
# sswap(
#     total=1073741824,      Swap 总量
#     used=150732800,       当前使用量
#     free=923009024,          剩余空间
#     percent=14.0,          Swap 使用率
#     sin=10705981440,        累计换入量
#     sout=40353792          累计换出量
# )

#sutil.virtual_memory() 和 psutil.swap_memory() 的返回结果都是 命名元组（namedtuple）类型，具体来说，是 psutil 定义的类的实例,可以按索引和字段访问
print("=================================")
print(psutil.virtual_memory().total)

#获取磁盘信息