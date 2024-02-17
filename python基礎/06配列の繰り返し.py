list =["hello", "world", "python","php"]

for item in list:
    print(item)
    
for i in range(0, len(list)):
    print(i, '-->',list[i])
    
for index,item in enumerate(list):
    print(index, item)
    
for index,item in enumerate(list, start=10):
    print(index, item)