# 常用操作符号杂谈

# 符号*
# 数值乘法
result = 3 * 4

# 列表重复
repeated_list = [1, 2] * 2

# 字符串重复
repeated_string = 'ab' * 3

# 字典合并
# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}

# merged_dict = {**dict1, **dict2}
# print(merged_dict)

# 参数解包


# def multiply(a, b, c):
#     return a * b * c


# numbers = [2, 3, 4]
# result = multiply(*numbers)
# print(result)

# 关键字参数解包


# def test_function(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# test_function(name="John", age=30)

# 符号%
# 判断奇偶数
# is_even = 4 % 2 == 0

# 列表旋转


# def rotate(nums, k):
#     k %= len(nums)
#     nums[:] = nums[-k:] + nums[:-k]


# nums = [1, 2, 3, 4, 5]
# k = 3
# rotate(nums, k)
# print(nums)

# 字符串格式化
# name = 'John'
# age = 30

# print('Hello, my name is %s and I am %s years old' % (name, age))

# 符号_
# 解包时忽略值
# a, _, c = (1, 2, 3)

# 循环忽略值
# for _ in range(5):
#     print("Hello, World!")

# 符号@
# 矩阵的乘法运算
# import numpy as np
# a = np.array([[1, 2], [3, 4]])
# b = np.array([[5, 6], [7, 8]])
# result = a @ b
# print(result)

# 装饰器
# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper


# @my_decorator
# def say_hello():
#     print("Hello!")


# say_hello()

# 符号...
# 多维数组切片中所有未明确指定的维度
# import numpy as np
# a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# a_slice = a[..., 1]
# print(a_slice)
