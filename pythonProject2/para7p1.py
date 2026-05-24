my_list = [1, 2, 3]
iterator = iter(my_list)
#print(iterator)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # ? 1, 4, error

