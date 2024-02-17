try:
    gender = input('性別を入力してください:')
    if gender != 'boy' and gender!='girl':
        raise Exception('only boy or girl')
    else:
        print('you are', gender)
except Exception as e:
    print(e)