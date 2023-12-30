y = [1, 2, 3]
x = y.copy()
print(id(x))

x[1] = 999
print(id(x))

x.append(77)

print(id(x))
x.clear()

print(id(x))

x = [1, 2]

print(id(x))

print(y)