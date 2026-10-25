import collections

#Counter:元素计数器
#对可迭代对象之中的子元素进行计数处理
names = ["jom", "kom", "lom","jom", "kom", "lom", "jom", "kom", "lom", "lom","lom","lom","lom","lom"]
#普通情况下
res = dict()
for name in names:
    if name in res:
        res[name] += 1
    else:
        res[name] = 1
print(res)

#可以借助counter计数器
res1 = collections.Counter(names)
print(res1)    #Counter({'lom': 8, 'jom': 3, 'kom': 3})
print(type(res1))

#带自定义默认值的字典

#不判断的情况下直接加会发生KeyError报错（不存在key，不能确定初始值）
# res = dict()
# for name in names:
#     res[name] += 1

#自定义一个默认值
#如果key存在，那么就使用已经存在的数值
#key不存在，那么就使用不存在的数值
# collections.defaultdict(<class type>)
# class type: int  0(默认值)
#             list  []
#             tuple ()
#             Boolean  False
res2 = collections.defaultdict(int)   #设置默认值int
for name in names:
    res2[name] += 1
print(res2)

res2 = collections.defaultdict(list)   #设置默认值list
for name in names:
    res2[name].append(name)
print(res2)


#namedtuple  命名元组
#普通元组,可读性差，只能通过过下标访问
# (name, age, address)
data = [("jom", 11, "a"), ("kom", 22, "b"), ("tom", 33, "c")]
for cho in data:
    print(cho[2], end="")
print()

#namedtuple  可以通过key-value的形式访问，可读性高
#1.创建namedtuple子类
#类型名 = namedtuple("类型名", "字段1 字段2 字段3")
Point = collections.namedtuple("Point", ["x", "y"])
#2.创建实例对象
p1 = Point(10, 20)
print(f"下标进行访问:x={p1[0]}, y={p1[1]}")
print(f"通过键值对访问:x={p1.x}, y={p1.y}")
print(type(p1))
#可以解包
x, y = p1
print(x)
print(y)
#创建后不能修改字段

# deque 双端队列
deq = collections.deque([])
print(deq, type(deq))
deq.append(1)
deq.append(2)
deq.append(3)
print(deq)
#头部插入0
deq.appendleft(0)
print(deq)
#从2开始打印，弹出0和1
res_0 = deq.popleft()
res_1 = deq.popleft()
print(f"弹出的第一个元素为{res_0}, 弹出的第二个元素为{res_1}")
print(f"弹出的结果为{deq}")