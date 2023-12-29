str = "ハンバーグおいしい"

for i in str:
    print(i, end = "-")

print()

# len関数を使う
for i in range(len(str)):
    print(str[i],end="")

print()

# enumeate関数を使う   [key value]の形になる 
for k,v in enumerate(str):
    print(k,v,end="-")

print()

for k,v in enumerate(str):
    print(v,end="")

print()

str1 = "study hard and make progress every day"

print(str1[0:16])
print(str1[1:])
print(str1[:13])
print(str1[:])
print(str1[::])
print(str1[0:10:2])
print(str1[::-1])    # str1を裏返し

# count関数
print(str1.count("e"))
print(str1.count("e",3,25))

my_str = "hello world python"

my_str_list = my_str.replace(" ", "|")
print(my_str_list)