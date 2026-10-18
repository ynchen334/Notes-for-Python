def task1():
    raise ValueError("数据格式错误")


def task2():
    print("任务 2 成功")


def task3():
    raise OSError("无法读取文件")


tasks = [task1, task2, task3]
exceptions = []

for task in tasks:
    try:
        task()
    except Exception as e:
        exceptions.append(e)

if exceptions:
    raise ExceptionGroup("部分任务执行失败", exceptions)