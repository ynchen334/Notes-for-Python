import argparse as ap
from pathlib import Path
#核心概念和基础使用
#argparse是将命令行输入的字符串，解析成结构化的python对象，自动完成一系列重复动作
#创建解析器：ArgumentParser()对象
    # ap_obj = ap.ArgumentParser(description="这是解析器")
# # 添加参数：add_argument()
    # ap_obj.add_argument("user", help="登录的用户")
    # ap_obj.add_argument("password", help="登陆的密码")
# # 解析参数：parse_args()
    # args = ap_obj.parse_args()
# # 使用参数：args.xxx 来进行参数的使用
    # print(f"[args]:{args}, type:{type(args)}")
# #自动将参数按照顺序进行解析，然后按照顺序赋值给argument

#必选参数
#位置参数   按照顺序传递的必选参数，不需要添加--前缀，用户必须按照我们自定义的顺序传入，否则报错，少传就报错
#“filename","encoding"是位置参数，也就是终端文件名后的参数
# ap_obj2 = ap.ArgumentParser(description="必选参数调试")
# ap_obj2.add_argument("filename", help="文件名", type=str)
# ap_obj2.add_argument("encoding", help="编码方式", type=str)
# args = ap_obj2.parse_args()
# print(f"[args]:{args}")

#可选参数
#带--前缀的参数，也叫做长选项，是最常用的参数类型
# p1 = ap.ArgumentParser(description="可选参数")
# p1.add_argument("-n", "--name", help="用户姓名", required=True, type=str)
# p1.add_argument("-a", "--age", help="用户年龄", default=18, type=int)

# #开关参数
# p1.add_argument("-d", "--debug", help="调试", action="store_true")
# args = p1.parse_args()
# print(f"[args]:{args}")

#参数类型和合法性检验
#sys.args拿到的参数都是字符串，需要手动转换类型
#检验端口号，必须在1~65535之间
# def check_port(port_str):
#     try:
#         port = int(port_str)
#     except ValueError:
#         raise ap.ArgumentTypeError("端口号必须是整数")
#     if not 1 <= port <= 65535:
#         raise ap.ArgumentTypeError("端口号范围不合法")
#     return port

# p2 = ap.ArgumentParser(description="端口解析检验器")
# #原生检验类型
# p2.add_argument("--num", help="一个数字", type=float, required=True)
# #自定义的检验类型
# p2.add_argument("--port", help="端口号", type=check_port, default=8000)
# args = p2.parse_args()
# print(f"num:{args.num}")
# print(f"port:{args.port}")

#子命令系统
# add_subparsers() 创建子命令系统，add_parser() 添加具体子命令，子解析器的 add_argument() 添加该子命令专属参数

import argparse

#第一步：创建主解析器parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(
    description="服务器管理工具"
)

#第二步：创建子命令管理器
subparsers = parser.add_subparsers(
    dest="command",
    required=True
)

#第三步：创建具体子命令并添加参数
# start子命令
start_parser = subparsers.add_parser(
    "start",
    help="启动服务器"
)

start_parser.add_argument(
    "--port",
    type=int,
    default=8080,
    help="服务器端口"
)

start_parser.add_argument(
    "--debug",
    action="store_true",
    help="开启调试模式"
)

# stop子命令
stop_parser = subparsers.add_parser(
    "stop",
    help="停止服务器"
)

stop_parser.add_argument(
    "--force",
    action="store_true",
    help="强制停止"
)

# status子命令
subparsers.add_parser(
    "status",
    help="查看服务器状态"
)

#第四步：解析并处理
args = parser.parse_args()

if args.command == "start":
    print(f"启动服务器，端口：{args.port}")

    if args.debug:
        print("调试模式已开启")

elif args.command == "stop":
    if args.force:
        print("正在强制停止服务器")
    else:
        print("正在正常停止服务器")

elif args.command == "status":
    print("服务器正在运行")


#如何优化帮助文档（--help）
# parser = ap.ArgumentParser(
#     description="优化帮助文档"
#     #结尾的补充
#     epilog="sdsdsdsdsd"
#     #自定义命令的用法提示  
#     usage="python app.py [选项]"       usage: python app.py [选项]
      #设置帮助信息中显示的程序名称
      #prog="server"         usage: server [-h] 如果不设置，通常会自动使用当前脚本名称

#) 


#add_argument()参数解释

# -p --port  输入参数是要写-p=xxx  或--port=xxx 或空格

# type：转换数据类型  默认字符串，type=int可以转为int，也可以传入自定义转换函数

# default：默认值  用户没有提供参数时使用的值

# required：是否必须提供，位置参数默认就是必填的

# choices：限制可选值  choices=["dev", "test", "prod"]只允许这三个参数

# help：帮助说明   help="服务器监听端口"   python app.py --help  
    # 就会在帮助信息中看到这个说明。argparse 会自动生成 usage 和帮助内容

# dest：指定保存到哪个属性   dest="username"
    # 之后使用：args.username

# metavar：控制帮助信息中的占位符
    # 例如：
    # parser.add_argument(
    #     "--port",
    #     type=int,
    #     metavar="PORT"
    # )
    # 帮助信息类似：
    # --port PORT
    # 只影响帮助信息中的显示，不会影响保存变量名

# action：参数出现时执行什么动作
    # 默认action="store" 保存用户输入的值
    # action="store_true"  参数出现时为 True，不出现时为 False
    # arser.add_argument(
    #     "-v",
    #     "--verbose",
    #     action="store_true"
    # )

    # 运行：
    # python app.py --verbose
    # 结果：args.verbose == True

    # action="store_false"相反
    # action="append"  允许同一个参数出现多次，结果保存成列表
    # parser.add_argument(
    #     "--tag",
    #     action="append"
    # )
    # 运行：
    # python app.py --tag python --tag linux --tag docker
    # 结果：
    # args.tag == ["python", "linux", "docker"]
    
    # action="count"  统计参数出现次数
    # parser.add_argument(
    #     "-v",
    #     "--verbose",
    #     action="count",
    #     default=0
    # )
    # 运行：
    # python app.py -vvv
    # 结果：
    # args.verbose # 3

    # action="store_const"   参数出现时，保存 const 指定的固定值
    # parser.add_argument(
    #     "--debug",
    #     action="store_const",
    #     const="DEBUG",
    #     default="INFO"
    # )
    # 传入：
    # python app.py --debug
    # 结果：
    # args.debug # "DEBUG"
    # 不传：
    # args.debug # "INFO"


# nargs：一个参数接收几个值
    # parser.add_argument(
    #     "--point",
    #     nargs=2,
    #     type=int
    # )
    # 运行：
    # python app.py --point 10 20
    # 结果：
    # args.point # [10, 20]

    # 注意：只要设置了 nargs，通常结果就是列表，即使一个参数也是
    # nargs="?“ 接收零个或一个值
    # nargs="*”接收零个或多个值

# const：参数出现但没有普通输入值时使用的常量
    # parser.add_argument(
    #     "--*olor",
    #     nargs="?",
    #     const="a*to",
    #     default="never"
    # )
    # 三种情况：
    # python app.py --color always
    # 结果：
    # "always"

    # 只写参数名：
    # python app.py --color
    # 结果：
    # "auto"

    # 完全不写：
    # python app.py
    # 结果：
    # "never"

    # const 通常不会单独使用，主要配合：
    # action="store_const"
    # action="append_const"
    # nargs="?"
