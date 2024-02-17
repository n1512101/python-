list = ["hello", "world", "python"]

print(list, id(list))

list.append('sql')
print(list, id(list))

list.insert(1, 100)
print(list)

list.remove('world')
print(list, id(list))

print(list.pop(1))
print(list)

# list.clear()
# print(list, id(list))

list.reverse()
print(list)

new_list = list.copy()
print(list, id(list))
print(new_list, id(new_list))

list[1] = 'mysql'
print(list)

