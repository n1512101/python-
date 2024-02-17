import random
list1 = [item for item in range(10)]
print(list1)

list2 = [item*item for item in range(10)]
print(list2)

list3 = [random.randint(1, 100) for _ in range(10)]
print(list3)

list4 = [i for i in range(10) if i%2==0]
print(list4)