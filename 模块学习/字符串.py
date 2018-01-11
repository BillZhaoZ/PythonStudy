# 一江夜雨  Python学习  2018
# 字符串

str_my = "alibaba"

print("str = " + str_my)  # 全部打印
print("str[0] = " + str_my[0])  # 0位置
print("str[2:5] = " + str_my[2:5])  # iba   2.3.4  不包含5
print("str[2:] = " + str_my[2:])  # 2到结尾
print("str * 2 = " + str_my * 2)  # 打印两边

######################  分割  ##################

var1 = 'Hello World!'
var2 = "Python Programming"

# 访问字符串的值
print("var1[0]: ", var1[0])
print("var2[1:5]: ", var2[1:5])  # 切片加索引

# 更新字符串
print("Updated String :", var1[:6] + 'Python')  # 更新索引5以后的值

# 特殊运算符

a = "hello"
b = "python"

print("a + b = " + a + b)
print("a * b = " + a * 2)
print("a[1] = " + a[1])
print("h" in a)
