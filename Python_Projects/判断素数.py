num=int(input("请输入一个数："))
if num<2:
    print("不是素数")
else:
    i=2
    while num>i:
        if num%i==0:
            print("不是素数")
            break
        i+=1
    else:
        print("是素数")