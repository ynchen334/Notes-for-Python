#列表可以修改
l1 = ['a', 'b', 'c']
print(l1)
l1[1] = 'B'
print(l1)
l1.append('d')   #append（）没有返回值，先调用再print
print(l1)
del l1[2]
print(l1)

#list的截取与字符串类似，并且可以用+来拼接
#列表可以嵌套


#列表比较需要引入 operator 模块的 eq 方法
# 导入 operator 模块
import operator

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))  #false
print("operator.eq(c,b): ", operator.eq(c,b))  #true

#常见函数
#len()  max()  list(seq)

#常见方法
#list.count(obj)

#list.extend(seq)  
#seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾

#list.index()

#list.insert(index, obj)  指定对象插入列表的指定位置
list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('列表插入元素后为 : ', list1)

#list.pop([index=-1])  移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#list.remove(obj)      移除列表中某个值的第一个匹配项
#list.reverse()        将列表反过来

#list.sort( key=None, reverse=False)
#对原列表进行排序
#key代表每一个可迭代元素的索引第key个
#reverse = True 降序， reverse = False 升序

#list.clean()
#list.copy()




