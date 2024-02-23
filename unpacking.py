# ex1
point = (1, 2, 3)
x, y, z = point
print(x, y, z)

# ex2
a, b, c = "XYZ"
print(a, b, c)

# ex3
numbers = {1, 2, 3}
a, b, c = numbers
print(a, b, c)

# ex4
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
name, age, city = person.values()
print(name, age, city)

# ex5
it = iter([1, 2, 3])
x, y, z = it
print(x, y, z)

# ex6
gen = (x * 2 for x in range(3))
a, b, c = gen
print(a, b, c)

# ex7
matrix = [[1, 2], [3, 4]]
(a, b), (c, d) = matrix
print(a, b, c, d)
