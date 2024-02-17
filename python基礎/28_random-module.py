import random

random.seed(100)
print(random.random())

print(random.randint(1,100))

for i in range(10):
    print(random.randrange(1,10,3))

print(random.uniform(1,100))

lst = [i for i in range(1,11)]
print(random.choice(lst))

random.shuffle(lst)
print(lst)