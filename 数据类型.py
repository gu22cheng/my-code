# 方式1：使用print直接输出类型信息
print(type("芙蓉之花"))
print(type(520))
print(type(13.14))


#方式2：使用变量存储type()语句的结果
string_type=type("芙蓉之花")
int_type=type(520)
float_type=type(13.14)
print(string_type)
print(int_type)
print(float_type)


# 方式3：使用type()语句，查看变量中存储的数据类型
name="芙蓉之花"
name_type=type(name)
print(name_type)


# 将数字类型转换成字符串
num_str=str(520)
print(type(num_str),num_str)

float_str=str(13.14)
print(type(float_str),float_str)
# 将字符串转换成数字
num=int("520")
print(type(num),num)

num2=float("13.14")
print(type(num2),num2)

# 想要将字符串转换成数字，必须要求字符串内的内容都是数字

#整数转浮点数
float_num=float(11)
print(type(float_num),float_num)

# 浮点数转整数
int_num=int(13.14)
print(type(int_num),int_num)

