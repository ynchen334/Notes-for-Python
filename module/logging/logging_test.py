import logging

# https://blog.csdn.net/B11050729/article/details/132340769

    # 灵活性：logging 模块允许你根据需要设置日志的级别、格式和输出位置。
    # 可扩展性：你可以轻松地将日志输出到文件、控制台、网络等不同的目标。
    # 结构化日志：logging 模块支持结构化日志记录，便于后续的分析和处理。
    # 性能优化：与 print 相比，logging 模块在性能上进行了优化，适合在生产环境中使用。

    # logger：提供日志接口，供应用代码使用。logger最长用的操作有两类：配置和发送日志消息。可以通过logging.getLogger(name)获取logger对象，如果不指定name则返回root对象，多次使用相同的name调用getLogger方法返回同一个logger对象。

    # handler：将日志记录（log record）发送到合适的目的地（destination），比如文件，socket等。一个logger对象可以通过addHandler方法添加0到多个handler，每个handler又可以定义不同日志级别，以实现日志分级过滤显示。

    #  filter：提供一种优雅的方式决定一个日志记录是否发送到handler。

    #  formatter：指定日志记录输出的具体格式。formatter的构造方法需要两个参数：消息的格式字符串和日期字符串，这两个参数都是可选的


#logging标准库的简单解读

# logging.basicConfig(**kwargs)该函数可以对根日志记录器进行配置
# 支持的参数：
#     filename    使用指定的文件名创建FileHandler，该参数缺省则使用StreamHandler
#     format	    指定处理器使用的格式字符串，根日志器的默认：%(levelname)s:%(name) s:%(message)s
#     level	      设置根日志器的级别，根记录器默认的日志级别为：logging.WARNING
#     datefmt     使用指定的日期/时间格式来替换%(asctime)s的默认格式'%Y-%m-%d %H:%M:%S,uuu'，其中 uuu 部分是毫秒值

#日志输出格式
    # %(asctime)s: 获取日志输出的时间
    # %(levelname)s: 获取日志输出的级别
    # %（message）s：获取日志输出的内容
    # %（module)s:获取日志输出的模块名  
    # %(lineno)d:获取日志输出的行号
    # %(function)s:获取日志输出的函数名
    # %(name)s: logger的名字
    # %(filename)s；产生日志的py文件名


def func1():
    logging.basicConfig(
        level = logging.DEBUG,   #设置日志级别
        format = "%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.debug("调试信息：变量x的数值是10")
    logging.info("输出信息：变量x的数值是20")

    # debug:10, 调试
    # info：20，输出
    # warning：30，警告
    # error：40，报错
    # critical：50，严重报错
#日志级别：精准控制日志的输出(低于设置级别的日志不输出)
def func2():
    logging.basicConfig(level=logging.WARNING)
    logging.debug("[debug]:不输出")
    logging.info("[info]:不输出")
    logging.warning("[warning]:输出")
    logging.error("[error]:输出")
    logging.critical("[critical]:输出")

# func2()

# 将日志发送到不同的位置

#日志库采用模块化 方法，并提供几类组件：记录器、处理程序、过滤器和格式化程序

# 记录器	logging.getLogger()	暴露了应用程序代码直接使用的接口
# 处理程序	logging.FileHandler()
# logging.StreamHandler()
# logging.NullHandler()	将日志记录（由记录器创建）发送到适当的目标
# 过滤器	logging.Filter()	提供了更精细的附加功能，用于确定要输出的日志记录
# 格式化程序	logging.Formatter()	指定最终输出中日志记录的样式

# 目的地：文件，控制台，命令行
# streamhandler:输出到控制台
# filehandler：输出到文件
# 没有设置：输出到命令行

# logger = logging.getLogger(__name__) 使用当前模块自己的命名日志记录器
# 当 main.py 作为主程序运行时，__name__ 的值是 "__main__"。
# 当 database.py 被其他模块导入时，__name__ 的值通常是 "database"
# 便于分辨是哪个模块的日志

def func3():
    #创建logging对象（日志器）
    logger = logging.getLogger("test")   
    #设置日志级别
    logger.setLevel(logging.INFO)   #日志需要先通过logger的等级检查   
    # 创建文件处理程序  默认追加模式
    fh = logging.FileHandler(filename="./test.log",encoding="utf8")
    # 创建流处理程序
    sh = logging.StreamHandler()
    # 为文件处理程序设置日志等级
    fh.setLevel(logging.ERROR)
    # 为流处理程序设置日志等级
    sh.setLevel(logging.DEBUG)
    # 创建格式化程序
    ffmt = logging.Formatter(
        fmt = "%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s",    
        datefmt = "%Y/%m/%d %H:%M:%S"
    )
    # 创建格式化程序
    sfmt = logging.Formatter(
        fmt = "%(asctime)s - %(levelname)s - %(name)s - %(filename)s:%(lineno)d - %(message)s",
    )

    # 将 ffmt 格式化程序应用到 fh 文件处理程序
    fh.setFormatter(ffmt)
    # 将 sfmt 格式化程序应用到 sh 流处理程序
    sh.setFormatter(sfmt)

    # 将文件处理程序应用到logger日志器
    logger.addHandler(fh)
    # 将流处理程序应用到logger日志器
    logger.addHandler(sh)

    # 记录日志信息
    logger.debug("This is a DEBUG log.")
    logger.info("This is an INFO log.")
    logger.warning("This is a WARNING log.")
    logger.error("This is an ERROR log.")
    logger.critical("This is a CRITICAL log.")

# Logger 决定接收和分发哪些日志。
# Handler 决定日志输出到哪里，以及哪些等级可以通过。
# Formatter 决定日志最终如何排版。

# logger.setLevel()：控制日志能不能进入处理器。
# handler.setLevel()：控制日志能不能通过这个处理器。
# handler.setFormatter()：控制输出的日志长什么样。

# func3()

#子记录器

# getLogger() 返回的记录器具有以.分隔的层次结构，在分层列表中较低的记录器是列表中较高的记录器的子项。例如，给定一个名为 foo 的记录器，名称为 foo.bar 、 foo.bar.baz 和 foo.bam 的记录器都是 foo 子项

def func4():
    # 创建日志器 test
    logger = logging.getLogger("test")
    logger.setLevel(logging.INFO)

    # 创建日志器 test.env1 ，表明 env1 上级日志器是 test,有效等级继承test
    logger_env1 = logging.getLogger("test.env1")
    # logger_env1.propagate = False 日志是否能向父日志传播，默认true，如果设为false，子日志没有加handler的情况下，无法用父日志的handler

    # 创建流处理程序
    sh = logging.StreamHandler()

    # 创建格式处理程序
    # %(levelname)8s 最小宽度8字符，默认右对齐
    sfmt = logging.Formatter(
        fmt = "%(asctime)s - %(levelname)8s - %(name)s - %(filename)s:%(lineno)d - %(message)s",
    )

    # 将格式处理程序应用到流处理程序
    sh.setFormatter(sfmt)

    # 将流处理程序应用到test日志器
    logger.addHandler(sh)
    # 将流处理程序应用到env1日志器
    # logger_env1.addHandler(sh)

    # 日志记录
    logger_env1.debug("This is a DEBUG log.")
    logger_env1.info("This is an INFO log.")
    logger_env1.warning("This is a WARNING log.")
    logger_env1.error("This is an ERROR log.")
    logger_env1.critical("This is a CRITICAL log.")

func4()

#Filter（过滤器）

def func5():

    # 创建日志器 test
    logger = logging.getLogger("test")
    logger.setLevel(logging.DEBUG)

    # 创建日志器 test.env1 ，表明 env1 上级日志器是 test
    logger_env1 = logging.getLogger("test.env1")

    # 创建流处理程序
    sh = logging.StreamHandler()

    # 创建格式处理程序
    sfmt = logging.Formatter(
        fmt = "%(asctime)s - %(levelname)8s - %(name)s - %(filename)s:%(lineno)d - %(message)s",
    )

    # 将格式处理程序应用到流处理程序
    sh.setFormatter(sfmt)

    # 创建Filter对象
    class MyFilter(logging.Filter):
        def filter(self, record):
            if record.name == 'test':
                #如果日志来自 test，只允许 INFO 和 WARNING 通过
                return record.levelno in (logging.WARNING,logging.INFO)
            if record.name == 'test.env1':
                return record.levelno == logging.ERROR
            return True    #如果前面的条件都不匹配，就允许日志通过

    # 将过滤器应用到流处理程序（接收的是过滤器对象）
    sh.addFilter(MyFilter())

    # 将流处理程序应用到test日志器
    logger.addHandler(sh)

    logger.debug("This is a DEBUG log.")
    logger.info("This is an INFO log.")
    logger.warning("This is a WARNING log.")
    logger.error("This is an ERROR log.")
    logger.critical("This is a CRITICAL log.")

    logger_env1.debug("This is a DEBUG log.")
    logger_env1.info("This is an INFO log.")
    logger_env1.warning("This is a WARNING log.")
    logger_env1.error("This is an ERROR log.")
    logger_env1.critical("This is a CRITICAL log.")

#代码中使用sh.addFilter(MyFilter())，将自定义的MyFilter()过滤器应用到处理程序，该过滤器将对使用该处理程序的日志器生效；
# test 日志器仅生成了 INFO、WARNING 级别的日志，其余日志被过滤器过滤掉了；
# env1 日志器仅生成了 ERROR 级别的日志，其余日志被过滤器过滤掉了


#record 是一条日志记录对象，里面保存了这条日志的各种信息
    # record.name	        日志器名称	        test
    # record.levelno	    日志等级数值    	40
    # record.levelname	    日志等级名称	    ERROR
    # record.msg	        原始日志消息	    数据库连接失败
    # record.filename	    调用日志的文件名  	main.py

# 一条日志的输出需要经过以下几次过滤：

# 日志器日志等级的过滤；
# 日志器的过滤器过滤；
# 处理器设置的日志等级的过滤；
# 处理器设置的过滤器的过滤；


# RotatingFileHandler 是 Python logging 模块提供的一种可以自动切分日志文件的处理器
# 它解决了一个很实际的问题：如果你的程序一直运行，并且不断向 app.log 写入日志，这个文件就可能越来越大，最后占用大量磁盘空间。

# RotatingFileHandler 可以在日志文件达到指定大小后，自动把旧日志备份，并继续写入新的日志文件。
from logging.handlers import RotatingFileHandler
def func7():
    # 创建日志器
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.DEBUG)

    # 创建支持自动轮转的文件处理器
    handler = RotatingFileHandler(
        filename="app.log",
        maxBytes=1024 * 1024,  # 单个文件最大约 1 MB
        backupCount=3,         # 最多保留 3 个备份
        encoding="utf-8"
    )

    # 设置日志格式
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(handler)

    # 写入日志
    for i in range(10000):
        logger.info("这是第 %d 条日志", i)
