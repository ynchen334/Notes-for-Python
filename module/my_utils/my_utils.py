def calculate_average(data):
    if not data:
        raise ValueError("datalist cannot be empty")
    return sum(data) / len(data)

if __name__ == "__main__":
    ls1 = [10, 20, 40, 111]
    result1 = calculate_average(ls1)
    print(result1)

# __name__ == "__main__"的作用
#自己执行时，脚本的__name__会自动赋值为__main__
#别的文件import这个脚本时，__name__会被赋值为别的名字
#if判断保证了测试代码只会在自己执行时有用，别的文件用不了