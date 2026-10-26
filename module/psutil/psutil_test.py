#使用psutil这个第三方模块在Python中获取系统信息
#psutil = process and system utilities
#第三方库，需要先用 pip install psutil 安装
#https://liaoxuefeng.com/books/python/third-party-modules/psutil/index.html#0
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
#取磁盘分区、磁盘使用率和磁盘IO信息
print("=================================")
print(psutil.disk_partitions())  #磁盘分区信息
# 可能的输出：
# [
#     sdiskpart(
#         device='/dev/disk1',   设备名称或设备路径
#         mountpoint='/',   挂载点
#         fstype='hfs',     文件系统类型
#         opts='rw,local,rootfs,dovolfs,journaled,multilabel'挂载选项
#     )
# ]

print(psutil.disk_usage('/'))    #磁盘使用情况
print(psutil.disk_io_counters()) #磁盘IO情况
# 字段	                含义	                你的数值
# read_count	    累计读操作次数	               33,292
# write_count	    累计写操作次数	               2,683
# read_bytes	    累计读取字节数	            1,718,815,744
# write_bytes	    累计写入字节数	            180,334,592
# read_time	        累计读操作耗时，通常为毫秒	    15,128
# write_time	    累计写操作耗时，通常为毫秒	    6,429
# read_merged_count	累计合并的读请求数	            4,376
# write_merged_count	累计合并的写请求数	        5,623
# busy_time	    磁盘处于忙碌状态的累计时间，通常为毫秒	4,676


# 获取网络信息
# psutil可以获取网络接口和网络连接信息
print("=================================")
print(psutil.net_io_counters())  # 获取网络读写字节／包的个数
# 字段	              含义	        你的数据
# bytes_sent	累计发送的字节数	约 3.62 GiB
# bytes_recv	累计接收的字节数	约 9.65 GiB
# packets_sent	累计发送的数据包数	10,613,069
# packets_recv	累计接收的数据包数	10,423,357
# errin	        接收方向累计错误数	0
# errout	    发送方向累计错误数	0
# dropin	    接收方向累计丢弃数	0
# dropout	    发送方向累计丢弃数  0
#一般都是累计统计值，不是当前瞬时流量
#默认返回一个 snetio 对象,类似namedtuple，可以通过属性名访问
print("=================================")

from pprint import pprint
addrs = psutil.net_if_addrs()   # 获取网络接口信息,输出字典
pprint(addrs)    #pprint 是 Python 标准库，能自动调整字典的输出格式
# 看地址：接口配置了哪些 IPv4、IPv6 和链路层地址
# 字段	        含义
# family	地址类型，例如 IPv4、IPv6 或链路层地址
# address	IP 地址或其他类型的接口地址
# netmask	子网掩码
# broadcast	广播地址（如果平台提供）
# ptp	    点对点地址（如果平台提供）
#返回字典的值是列表，列表包含namedtuple形式的snicaddr
print("=================================")

pprint(psutil.net_if_stats())   # 获取网络接口状态
#关注的是接口的状态与配置，而不是累计流量
# 字段	        含义	
# isup	    接口是否处于启用状态	
# duplex	双工模式	
# speed	    接口报告的速度，通常以 Mbps 表示	
# mtu	    最大传输单元	
#isup=True 不等于互联网一定可以访问。 它通常只说明接口处于启用状态，不保证 IP 配置、网关、DNS 或远端服务器都正常
# 双工模式描述链路的收发方式：
# - 全双工（Full duplex）：可以同时发送和接收数据。
# - 半双工（Half duplex）：发送和接收不能同时进行。
# - 未知（Unknown）：系统无法报告具体模式，或平台不支持获取该信息。

print("=================================")
pprint(psutil.net_connections())  #获取当前网络连接信息
#可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动
print(type(psutil.net_connections()))  #list
#列表每个元素是sconn对象，类似namedtuple
#每个 sconn 对象代表一条网络连接记录
# 字段	        含义
# fd	    socket 文件描述符
# family	地址类型，例如 IPv4、IPv6
# type	    socket 类型，例如 TCP 常用的 SOCK_STREAM
# laddr	    本地 IP 地址和端口
# raddr	    远端 IP 地址和端口
# status	TCP 连接状态
# pid	    创建该 socket 的进程 PID，可能为 None

print("=================================")
#获取进程信息
print(psutil.pids())  #所有进程ID
p = psutil.Process(1) # 获取指定进程ID=1,systemd
print(p.name()) # 进程名称


# >>> p = psutil.Process(3776) # 获取指定进程ID=3776，其实就是当前Python交互环境
# >>> p.name() # 进程名称
    # 'python3.6'
# >>> p.exe() # 进程exe路径
    # '/Users/michael/anaconda3/bin/python3.6'
# >>> p.cwd() # 进程工作目录
    # '/Users/michael'
# >>> p.cmdline() # 进程启动的命令行
    # ['python3']
# >>> p.ppid() # 父进程ID
    # 3765
# >>> p.parent() # 父进程
    # <psutil.Process(pid=3765, name='bash') at 4503144040>
# >>> p.children() # 子进程列表
    # []
# >>> p.status() # 进程状态
    # 'running'
# >>> p.username() # 进程用户名
    # 'michael'
# >>> p.create_time() # 进程创建时间
    # 1511052731.120333
# >>> p.terminal() # 进程终端
    # '/dev/ttys002'
# >>> p.cpu_times() # 进程使用的CPU时间
    # pcputimes(user=0.081150144, system=0.053269812, children_user=0.0, children_system=0.0)
# >>> p.memory_info() # 进程使用的内存
    # pmem(rss=8310784, vms=2481725440, pfaults=3207, pageins=18)
# >>> p.open_files() # 进程打开的文件
    # []
# >>> p.connections() # 进程相关网络连接
    # []
# >>> p.num_threads() # 进程的线程数量
    # 1
# >>> p.threads() # 所有线程信息
    # [pthread(id=1, user_time=0.090318, system_time=0.062736)]
# >>> p.environ() # 进程环境变量
    # {'SHELL': '/bin/bash', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:...', 'PWD': '/Users/michael', 'LANG': 'zh_CN.UTF-8', ...}
# >>> p.terminate() # 结束进程
    # Terminated: 15 <-- 自己把自己结束了

#和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限
print("=================================")

# 遍历系统中所有进程  psutil.process_iter()
# 获取每个进程的 PID、名称、用户名、内存使用情况等信息
# psutil.process_iter()：返回一个可迭代对象，逐个提供系统中的进程。
# proc：每次循环拿到的都是一个 psutil.Process 对象，代表一个进程
for proc in psutil.process_iter():
    print(proc)
#有pid，name，status三个字段