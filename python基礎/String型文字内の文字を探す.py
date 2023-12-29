str1 = "ldaekfnnghaoijfi343102312laldfuuOHIYUHIJOi1924102310ijfoadfhqp"

# find()   文字が位置する最初のインデックスを返す,無ければ-1をかえす
print(str1.find("o"))
print(str1.find("A"))

# 指定の範囲内で探す
print(str1.find("o",2,30))

# index()  find()と似てるが、文字が見つからなければエラーになる
print(str1.index("o"))
# print(str1.index("A"))

# rfind()  文字が位置する最後のインデックスを返す、なければ-1を返す
print(str1.rfind("o"))

# ASCII値で取得  max()  min()
print(max(str1))
print(min(str1))