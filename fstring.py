# 计算表达式
price = 19.99
quantity = 3
total = f'Total: {price * quantity:.2f}'
print(total)

# 格式化日期和时间
from datetime import datetime
now = datetime.now()
formatted_date = f'Current date: {now:%B %d, %Y}'
print(formatted_date)

# 字典和列表元素访问
person = {'name': 'Hongtu', 'age': 28}
item = ['apple', 'banana', 'cherry']
description = f"{person['name']} likes {item[0]}"
print(description)

# 多行字符串
name = 'Hongtu'
age = 28
hobby = 'coding'
message = f'''Name: {name}
Age: {age}
Hobby: {hobby}'''
print(message)

# 允许使用反斜杠
words = ["Python", "5", "Minutes"]
print(f"{'\\n'.join(words)}")

# 引号一致性
employee = {
    "name": "Hongtu",
    "age": 28,
    "hobby": "coding",
}

print(f"Employee: {employee["name"]}")

# 多层嵌套
product = {
    "name": "T-shirt",
    "options": {
        "color": ["red", "blue", "green"],
        "size": ["S", "M", "L"]
    }
}

user_choice = {
    "color": "blue",
    "size": "M"
}

extra_cost = 2
message = f"""
Selected Product:
    Name: {product['name']}
    Color: {user_choice['color']} (extra cost: {f'${extra_cost}' if user_choice['color'] != 'red' else 0})
    Size: {user_choice['size']}
"""
print(message)
