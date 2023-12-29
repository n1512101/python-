str = "I miss you Very Much"

# 大文字　小文字
print(str.upper())
print(str.lower())

# swapcase()  大文字と小文字を入れ替える
print(str.swapcase())

# title()  各単語の先頭を大文字にする
print(str.title())

# center()
str1 = "ニトリ速くきて"
print(str1.center(50))
print(str1.center(50,"*"))

# ljust()
print(str1.ljust(50,"*"))
# rjust()
print(str1.rjust(50,"*"))
# zfill()
print(str1.zfill(60))