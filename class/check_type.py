# 检查类型
# issubclass(cls,class_or_tuple) 检查cls是否为后一个类或元组包含的多个类中任意类的子类
# isinstance(obj,class_or_tuple) 检查obj是否为后一个类或元组包含的多个类中任意类的对象

hello = 'Hello'
print("hello是否是str的实例", isinstance(hello, str))
print("hello是否是object的实例", isinstance(hello, object))

print("str是否是object的子类", issubclass(str, object))

# 第二个参数可以传元组
data = [1, 2]
print("data是否是列表或者元组的实例", isinstance(data, (list, tuple)))