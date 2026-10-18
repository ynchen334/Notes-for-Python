#键必须是唯一的，但值则不必。
#值可以取任何数据类型，但键必须是不可变的，如字符串，数字
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}

#两种创建空字典的方式
#emptyDict = dict()
#emptyDict = {}

#字典可以修改和添加
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
 
tinydict['Age'] = 8               # 更新 Age
tinydict['School'] = "菜鸟教程"    # 添加信息
 
print ("tinydict['Age']: ", tinydict['Age'])
print ("tinydict['School']: ", tinydict['School'])

#不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
#键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

#字典内置函数
#len()
#str()    {'Name': 'Runoob', 'Class': 'First', 'Age': 7}

#方法
#dict.get(key[, value]) 返回指定键的值
#key -- 字典中要查找的键
#value -- 可选，如果指定键的值不存在时，返回该默认值

