# 去除字符串两端的空白字符
fruit = "   香蕉, 苹果, 樱桃   "
print(fruit.strip())
print(fruit.lstrip())
print(fruit.rstrip())

# 结合列表理解处理空白字符
fruits = ["   橘子 ", " 梨  ", "  芒果 "]
cut_fruits = [fruit.strip() for fruit in fruits]
print(cut_fruits)

# 处理自CSV文件的数据
data = " 西瓜, 菠萝 , 桃子 "
fruits = [fruit.strip() for fruit in data.split(",")]
print(fruits)

# 处理文件中的数据右侧不需要的换行符
with open('feedback.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

clean_lines = [line.rstrip('\n') for line in lines]
print(lines)
print(clean_lines)
