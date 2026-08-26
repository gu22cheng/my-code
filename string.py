# 字符串字面量之间的拼接
print("学IT来黑马"+"月薪过万")
# 字符串字面量和字符串变量的拼接,用”+“数字不行
name="黑马程序员"
address="建材城东路9号院"
print("我是："+name+",我的地址是："+address)

# 通过占位的形式，完成数字和字符串拼接
class_num=57
avg_salary=16781
message="Python计算机科学与技术，北京%s期,毕业平均工资：%s"%(class_num,avg_salary)
print(message)
name="传智播客"
set_up_year=2006
stock_price=19.99
message="我是:%s,我成立于：%d,我今天的股价是：%f"%(name,set_up_year,stock_price)
print(message)


num1=11
num2=11.345
print("数字11宽度限制5，结果：%5d"%num1)
print("数字11宽度限制1，结果：%1d"%num1)
print("数字11.345宽度限制7，小数精度2,结果：%7.2f"%num2)
print("数字11.345不宽度限制，小数精度2，结果：%.2f"%num2)


name="传智播客"
set_up_year=2006
stock_price=19.99
print(f"我是{name},我成立于：{set_up_year},我今天的股价是:{stock_price}")