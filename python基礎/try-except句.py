try:
    num = 3/0
    print(num)
except Exception as a:
    print(a)
else:
    print("異常なし")
finally:
    print("最後です。")