#Python 的元组与列表类似，不同之处在于元组的元素不能修改
#元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用
tup1 = (50,)
type(tup1)     # 加上逗号，类型为元组
# >><class 'tuple'>

#元组可以拼接
tup2 = (1, 2, 3, 4, 5, 6, 7 )
tup3 = tup1 + tup2
print (tup3)

#整个元组可以用del删除
tup = ('Google', 'Runoob', 1997, 2000)
print (tup)
del tup
print ("删除后的元组 tup : ")
print (tup)

#元组的内置函数有len。man，tuple（）等