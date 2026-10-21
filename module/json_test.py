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
print(type(json_obj))    #本质是字符串

json_obj_format = json.dumps(   #美化格式
    data,
    indent=2,               #缩进=2
    ensure_ascii=False,     #输出真实的Unicode字符（中文），不用ASCII显示
    sort_keys=True          #按ASCII顺序由小到大排
)
print(json_obj_format)

#将json数据直接写到文件中
with open("data.json", "w", encoding="utf-8")  as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
    print("successfully written to the file")


#反序列化
#将json转化为python数据类型
#json.loads(s) 将json字符串转换为python对象
json_str = """
    {"name":"Jack", "age":15, "is_student":true}   
"""   #true小写
res = json.loads(json_str)
print(res, type(res))    #字典

#json.load() 从文件读取
with open("data.json", "r", encoding="utf-8") as f:
    res = json.load(f)
    print(res, type(res))


#处理自定义对象
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Person(name = {self.name}, age = {self.age})"

#定义一个专门转换person的类，继承json.JSONEncoder
#__type__用来说明这是Person类，之后转回时不会转成字典而是Person类
class PersonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Person):
            return {"__type__":"Person", "name":obj.name,"age":obj.age}   
        return super().default(obj)    #让父类执行自己的default方法，抛出错误

def person_to_dict(obj):
    if isinstance(obj, Person):
        return {"__type__":"Person", "name":obj.name, "age":obj.age}
    raise TypeError(f"Object of type {type(obj) is not json}")

person = Person("admin", "22")
#序列化
#使用自定义的PersonEncoder
json_str1 = json.dumps(person, cls=PersonEncoder, ensure_ascii=False)
#使用default自定义默认参数
json_str2 = json.dumps(person, default=person_to_dict, ensure_ascii=False)

print(json_str1)
print(json_str2)


#反序列化
def dict_to_person(d):
    if d.get("__type__" ) == "Person":
        return Person(d["name"], d["age"])
    return d

#需指明object_hook
person_from_json = json.loads(json_str1, object_hook=dict_to_person)
print(person_from_json)
print(type(person_from_json))

print("--" * 10)
#常见使用场景
#API数据解析
api_response = """
{
    "code" : 20,
    "message":"success",
    "data":{
        "total":2,
        "items":[
            {"id":1,"title":"测试数据1","price":99},
            {"id":2,"title":"测试数据2","price":88},
            {"id":3,"title":"测试数据3","price":77}
            ]
        }
}
"""
print(api_response)
res = json.loads(api_response)
if res["code"] == 200:
    print("API request succeeded")
else:
    print("APT request failed")



# 类中__repr__和__str__的区别
# 直接打印一个类出来的是一个地址
# repr和str可以重构显示方法
# repr程序员看，str用户看
# 因此repr一般显示更多信息和参数
# print时，程序先查找有没有str，再查repr
# repr和str同时存在时，想调用repr要print(repr(p))
# 等价于print(p.__repr__())
