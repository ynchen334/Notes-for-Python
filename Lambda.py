 #传入参数x，返回平方
fun1 = lambda x : x ** 2
print(fun1(3))
#可传多个参数

#声明一个函数，传入一个列表，要求创建一个新列表，对列表每一个值进行加十的操作

def test_map(ls, func):
    res = []
    for i in ls:
        res.append(func(i))
    return res

ls = [1, 2, 3]
v = test_map(ls, lambda x : x + 10)
print(v)

# map函数   map(function, iterable, ...)
#map() 会根据提供的函数对指定序列做映射。
#第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表
def square(x) :            # 计算平方数
     return x ** 2
 
map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
#[1, 4, 9, 16, 25]
map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
#[1, 4, 9, 16, 25]
#提供了两个列表，对相同位置的列表数据进行相加
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
#[3, 7, 11, 15, 19]    
#注意在python3中会返回迭代器，需要用list（）等函数转换