tuple_A = (1, 2, 3, 5, 8)
tuple_B = (8, 2, 5)

tuple_C = tuple_A[:2] + tuple_B + tuple_A[2:]
print(tuple_C)

tuple_A = list(tuple_A)
for num in tuple_B[::-1]:
    tuple_A.insert(2, num)
tuple_A = tuple(tuple_A)
print(tuple_A)