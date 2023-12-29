str1 = "this is a String example..."
str2 = "this*is*a*String*example..."

# split()  指定文字による分割
print(str1.split())
print(str2.split("*"))

str3 = """Today
is
sunny
"""
# splitlines()   行ごとに分割
print(str3.splitlines())

# join()  指定の文字でlist内の文字を分割
s1 = "-"
list = ['hello', 'everybody', 'nice', 'to', 'meet', 'you']
print(s1.join(list))