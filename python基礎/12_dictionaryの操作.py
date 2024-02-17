d={"hello":10, "world":20, "python":30}

print(d["hello"])
print(d.get("hello"))

for item in d.items():
    print(item)
    
for key,value in d.items():
    print(key, '--->', value)
    
keys = d.keys()
print(keys)

values = d.values()
print(values)

print(d.items())

print(d.pop("hello"))
print(d)

print(d.popitem())
print(d)

d.clear()
print(d)