str1 = "   today is a nice day   "
str2 = "***today is a nice day***"

print(str1)
# 前後のスペースを削除する
print(str1.strip())

print(str2)
# 前後の指定の文字を削除する
print(str2.strip("*"))

# lstrip()
print(str1.lstrip())
print(str2.lstrip("*"))

# rstrip()
print(str1.rstrip())
print(str2.rstrip("*"))