# ex1
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)

# ex2
numbers = [1, 2, 3, 4, 5]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

# ex3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

# ex4


def add(x, y):
    return x + y


result1 = add(1, 2)
result2 = add(3, 4)
result3 = add(5, 6)

result1 = 1 + 2
result2 = 3 + 4
result3 = 5 + 6
