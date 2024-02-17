A={10,20,30,40,50}
B={30,50,88,76,20}

print(A&B)
print(A|B)
print(A-B)
print(A^B)

s={10,20,30}
s.add(100)
print(s)

s.remove(20)
print(s)

s.clear()
print(s)

s={10,20,30}
for index,item in enumerate(s):
    print(index, item)