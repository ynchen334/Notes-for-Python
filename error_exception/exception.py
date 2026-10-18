#错误Error
#语法错误 SyntaxError
# while True print('Hello world')
# File "/home/yinuo/labs/PythonLab/error_exception/exception.py", line 3  打印出错文件名
#     while True print('Hello world')   语法：没加冒号
#                ^^^^^
# SyntaxError: invalid syntax

#异常Exception
#即使语句或表达式使用了正确的语法，执行时仍可能触发错误。执行时检测到的错误称为 异常
#例如ZeroDivisionError NameError TypeError

#异常的处理
#try-except
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
#先执行try，无异常就跳过except，有异常就跳过子句，和后边的except匹配
#如果不匹配，就把异常传到外层try
try:
    try:
        result = 10 / 0
    except ValueError:
        print("内层处理 ValueError")  #不匹配
except ZeroDivisionError:
    print("外层处理除零异常")          #匹配2
#都不匹配，打印traceback，程序终止
#一个 except 子句 可以指定多个异常，例如
# except RuntimeError, TypeError, NameError:
#      pass
#父类可以匹配子类的异常，反过来不行
class B(Exception):
    pass

class C(B):     #括号内是子类
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()   #raise抛出异常，比如cls=B时抛出B异常
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")   #B，C，D
#如果except的顺序是BCD，则结果是BBB

#except 子句 可能会在异常名称后面指定一个变量
# 这个变量将被绑定到异常实例，该实例通常会有一个存储参数的 args 属性
# 为了方便起见，内置异常类型定义了 __str__() 来打印所有参数而不必显式地访问 .args
#可以获取具体的错误原因
try:
    raise Exception('spam', 'eggs')  #定义一个异常对象并传入两个参数
except Exception as inst:  #将异常对象赋给一个变量，类型为Exception
    print(type(inst))    # 异常的类型
    print(inst.args)     # 参数保存在 .args 中，成为元组
    print(inst)          # __str__ 允许直接打印为字符串
                         # 但可能在异常子类中被覆盖
    x, y = inst.args     # 解包 args
    print('x =', x)
    print('y =', y )

# 创建 Exception 异常对象
#         ↓
# 传入 'spam' 和 'eggs'
#         ↓
# 参数保存在异常对象的 args 元组中
#         ↓
# raise 抛出异常
#         ↓
# except Exception 匹配成功
#         ↓
# 把异常对象绑定给变量 inst
#         ↓
# type(inst) 得到 Exception
#         ↓
# inst.args 得到 ('spam', 'eggs')
#         ↓
# 打印 inst 时调用其字符串表示
#         ↓
# 将 args 解包给 x 和 y


#baseException是所有异常的基类，Exception是他的一个子类
#Exception可以捕获几乎一切，但建议具体


#except字句后边可以加else，用于执行try想要执行的命令
#可以缩小try中异常捕获的范围（前边的exception捕获不到else中的异常）
# try:
#     可能出错的代码
# except 某种异常:
#     处理异常
# else:
#     try 成功后执行的代码
#注意else里的内容只有try不出错时才会执行

#异常处理程序不仅会处理在 try 子句 中立刻发生的异常还会处理在 try 子句 中调用（包括间接调用）的函数


触发异常  raise
raise NameError('HiThere')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#     raise NameError('HiThere')
# NameError: HiThere

#也可以在Exception最后一行加raise，表示把刚才捕获到的异常抛到外层
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
# An exception flew by!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     raise NameError('HiThere')
# NameError: HiThere


#异常链
#处理第一个异常的过程中，又产生了第二个异常。Python 会保留两者，并告诉你第二个异常是在处理第一个异常时发生的
try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")

# Traceback (most recent call last):      第一个异常
#   File "<stdin>", line 2, in <module>
#     open("database.sqlite")
#     ~~~~^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

# During handling of the above exception, another exception occurred:   解释 

# Traceback (most recent call last):      第二个异常
#   File "<stdin>", line 4, in <module>
#     raise RuntimeError("unable to handle error")
# RuntimeError: unable to handle error

#显式异常链
# exc 必须为异常实例或为 None。
# raise RuntimeError from exc
def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     func()
#     ~~~~^^
#   File "<stdin>", line 2, in func
# ConnectionError

# The above exception was the direct cause of the following exception:
#连接语句明确表示因果关系
# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
#     raise RuntimeError('Failed to open database') from exc
# RuntimeError: Failed to open database

# 允许使用 from None 表达禁用自动异常链（一般不藏）
try:
    open('database.sqlite')    #这条的异常不显示
except OSError:
    raise RuntimeError from None

# Traceback (most recent call last):
#   File "<stdin>", line 4, in <module>
#     raise RuntimeError from None
# RuntimeError


#定义清理操作finally
# 如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。如果该异常没有 except 子句处理，在 finally 子句执行后会被重新触发。

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
# Goodbye, world!
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
#     raise KeyboardInterrupt
# KeyboardInterrupt
#如果没有相应的Exception子句接，那就先执行finally再抛异常

# 如果exception或else里有触发异常，先执行finally再抛出异常
# 如果finally里有break，continue，return，异常不重新引发（不推荐）
# 如果try中有以上三个语句之一，先执行finally再退出
# 如果try和finally都包含return，则返回finally的return
# 在实际应用程序中，finally 子句对于释放外部资源（例如文件或者网络连接）非常有用，无论是否成功使用资源。


 引发和处理多个不相关的异常
#ExceptionGroup
# 用于把多个已经发生的异常打包成一个异常，一次性抛出
# raise ExceptionGroup("发生多个问题", [异常1, 异常2])
def f():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup('there were problems', excs)
try:
    f()
except Exception as e:
    print(f'caught {type(e)}: {e}')
# caught <class 'ExceptionGroup'>: there were problems (2 sub-exceptions)
#异常组中必须放异常实例
# 正确
# excs = [OSError("error 1"), SystemError("error 2")]
# 错误
# excs = [OSError, SystemError]

# 将多个异常收集起来的方法：建列表
exceptions = []

for task in tasks:
    try:
        task.run()
    except Exception as e:
        exceptions.append(e)

if exceptions:
    raise ExceptionGroup("多个任务执行失败", exceptions)

