a=float(input("请输入第一个数字："))
b=float(input("请输入第二个数字："))
op=input("输入运算符：")
if op=="+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="/":
    print(a/b)
elif op=="//":
    print(a//b)
elif op=="**":
    print(a**b)
elif op=="%":
    print(a%b)
else :
    print("计算失败")

