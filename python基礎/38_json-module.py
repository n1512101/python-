import json

lst = [
    {"name":"ysj","age":18,"score":90},
    {"name":"cmm","age":21,"score":99},
    {"name":"zyy","age":19,"score":89}
    ]

s = json.dumps(lst, ensure_ascii=False, indent=4)
print(type(s))
print(s)

lst2 = json.loads(s)
print(type(lst2))
print(lst2)

with open('./file/student.txt', 'w') as file:
    json.dump(lst, file, ensure_ascii=False, indent=4)
    
with open('./file/student.txt') as file:
    lst3 = json.load(file)
    print(type(lst3))
    print(lst3) 