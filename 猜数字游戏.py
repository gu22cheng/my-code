import random
answer=random.randint(1,100)
times=0
while True:
    num=int(input("请输入您猜测的数字："))
    times+=1
    if num<answer:
        print("您猜小了")
    elif num>answer:
        print("您猜大了")
    else:
        print("您猜对了")
        print("您猜了%d次"%times)
        break
