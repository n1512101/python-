set1 = {1, 2, 3}
set2 = {1, 5, 6}
# set1には存在するが、set2には存在しない要素 set1,set2は変わらない
set3 = set1.difference(set2)
print(set3)

# set1が変わる
set1.difference_update(set2)
print(set1)


set1 = {1, 2, 3}
set2 = {1, 5, 6}
# 2つの集合を合併
set3 = set1.union(set2)
print(set3)

set1 = {1,2,3,4,5}
num = len(set1)
print(num)

for i in set1:
    print(i, end=" ")    # set集合はindexが定義できない為whileでの繰り返しは使えない

print()
set1.add(7)
print(set1)

set1.remove(7)
print(set1)