# JSON 标准库学习
# 1、数据类型的映射关系
# 2、序列化操作
# 3、反序列化操作
# 4、处理自定义对象
# 5、常见场景应用实战

import json

#json的核心概念和数据类型的映射
# object -> dict
# array -> list/tuple
# string -> str
# number -> int/float
# null -> none

#序列化
#主要是实现将python数据类型转换为json数据类型
#准备一个python 字典,实现到object的转换
data = {
    "name":"admin",
    "age":25,
    "is_student":False,
    "address":{"city":"北京", "district":"朝阳区"}
}
#将python对象转换为json的字符串
json_obj = json.dumps(data)
print(json_obj)
print(type(json_obj))

json_obj_format = json.dumps(
    data,
    indent=2,
    ensure_ascii=False,
    sort_keys=True
)
print(json_obj_format)