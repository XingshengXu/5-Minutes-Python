# 变量注解

age: int = 25
print(type(age))

# 函数参数类型和返回值类型


# def greet(name: str) -> str:
#     return 'Hello, ' + name


# def get_length(item: list) -> int:
#     return len(item)


# typing 库
# 可迭代对象类型
# from typing import List, Tuple, Dict, Set
# numbers: List[int] = [1, 2, 3] # 内含整数的列表
# coordinates: Tuple[float, float] = (10.0, 20.5) # 内含浮点数的元组
# translations: Dict[str, str] = {'hello': 'hola', 'thank you': 'gracias'} # 内含字符串的字典
# unique_numbers: Set[int] = {1, 2, 3} # 内含整数的集合

# 特殊类型
# from typing import Any, Optional, Union

# uncertain_value: Any = 123  # 可以是任何类型
# maybe_name: Optional[str] = None  # 可以是字符串或None
# mixed_value: Union[int, str] = 'Hello'  # 可以是整数或字符串

# 泛型和类型变量
# from typing import Generic, TypeVar, List

# T = TypeVar('T')

# class Box(Generic[T]):
#     def __init__(self):
#         self.items: List[T] = []

#     def put(self, item: T):
#         self.items.append(item)

#     def take(self) -> T:
#         return self.items.pop()


# # 创建一个存储苹果的箱子
# apple_box = Box[str]()
# apple_box.put('红苹果')
# apple_box.put('青苹果')

# # 从箱子里取出一个苹果
# taken_apple = apple_box.take()
# print(f"我从箱子里取出了一个苹果：{taken_apple}")
