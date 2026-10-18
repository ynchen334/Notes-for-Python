#filter() 是 Python 的一个内置高阶函数，用于从可迭代对象中筛选出符合条件的元素。
#它接收两个参数：一个判断函数和一个可迭代对象。filter() 会将可迭代对象中的每个元素依次传递给判断函数，保留返回值为 True 的元素，并生成一个迭代器
#filter(function, iterable)

#实例
#过滤奇数
def is_odd(n):
    return n % 2 == 1

ls1 = list(filter(is_odd, range(1, 15)))    #返回迭代器，注意转换
print(ls1)

#过滤空字符串
def not_empty(s):
    return s and s.strip()

strings = ['A', '', 'B', None, 'C', ' ']
result = filter(not_empty, strings)
print(list(result))                         # 输出: ['A', 'B', 'C']