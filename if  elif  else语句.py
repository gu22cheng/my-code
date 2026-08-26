"""
演示if eliy else 多条件判断语句的使用
"""

print("欢迎来到黑马动物园")
height=int(input("请输入您的身高(cm)："))
vip_level=int(input("请输入您的vip级别（1~5）"))
if height<120:
    print("您的身高低于120cm,可以免费游玩")
# elif可以使用多个
elif vip_level>3:
    print("您的vip级别大于3，可以免费游玩")
else:
    print("不好意思，您所有条件都不满足，需要购票30元")
print("祝您游玩愉快")

# 更简便的写法
if int(input("请输入要您的身高（cm）:"))<120:
    print("您的身高小于120cm,可以免费游玩")
elif int(input("请输入您的vip级别（1~5）"))>5:
    print("您的vip级别大于3，可以免费游玩")
elif int(input("请告诉我今天是几号"))==1:
    print("今天是1号免费日，可以游玩")
else:
    print("不好意思，所有条件都不满足，需要买票30元")
print("祝您游玩愉快")

#  猜猜心里数字
if int(input("请输入第一次猜想的数字："))==10:
    print("恭喜你猜对了")
elif int(input("不对，再猜一次"))==10:
    print("恭喜你猜对了")
elif int(input("不对，再猜最后一次："))==10:
    print("恭喜你猜对了")
else:
    print("Sorry,全部猜错啦，我想的是：10")