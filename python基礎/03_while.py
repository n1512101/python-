i=0
while i<3:
    user_name = input('入力')
    password=input('pass')

    if user_name=='ysj' and password=='eeee':
        print("ok")
        i=8
    else:
        if i<2:
            print('wrong,',2-i,'chance')
        i+=1
        
if i==3:
    print("no chance")