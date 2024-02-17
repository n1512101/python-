d={10:"cat", 20:"dog", 30:"pet", 20:"zoo"}
print(d)

list1 = [10,20,30,40]
list2 = ["cat", "dog", "pet", "zoo", "car"]

zipobj=zip(list1, list2)
print(zipobj)
# print(list(zipobj))
print(dict(zipobj))

d1 = dict(cat=10, dog=20)
print(d1)

print(max(d), min(d), len(d))
del(d)