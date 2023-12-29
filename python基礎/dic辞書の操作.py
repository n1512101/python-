my_dict = {"Bob":77, "Jack":88, "Tom":99}

# 要素を増やす
my_dict["Jerry"] = 50
print(my_dict)

# pop()
score = my_dict.pop("Bob")
print(my_dict)
print(score)

my_dict.clear()
print(my_dict)

my_dict = {"Bob":77, "Jack":88, "Tom":99}

# keys()　すべてのkeyを取得
keys = my_dict.keys()
print(keys)

# forによる繰り返し
for key in keys:
    print(f'my_dictのkeyは{key}')
    print(f'my_dictのvalueは{my_dict[key]}')

# 上のfor文と動作がまったく同じの書き方
for key in my_dict:
    print(f'my_dictのkeyは{key}')
    print(f'my_dictのvalueは{my_dict[key]}')


print(len(my_dict))