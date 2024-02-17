try:
    num1 = int(input('数字を入力'))
    num2 = int(input('数字を入力'))
    result = num1/num2

except ZeroDivisionError:
    print('0はダメ')
except ValueError:
    print('ダメ')
except BaseException:
    print('未知')
else:
    print('結果:', result)
finally:
    print('おわり')