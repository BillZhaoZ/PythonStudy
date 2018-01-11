# 一江夜雨  Python学习  2018


# 1.算数运算符
a = 20
b = 10

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)  # a的b次方

# 2.比较远算符
var = a > b
print(var)

var = a >= b
print(var)

var = a == b
print(var)

var = a <= b
print(var)

var = a != b
print(var)

# 3.赋值运算符
c = a + b
print(c)

c += a
print(c)

# 4.逻辑运算符
j = False
K = True

var = j and K
print(var)

var = j or K
print(var)

var = not (j and K)
print(var)

# 5.按位运算符

# 6.成员运算符  测试给定值是否为序列中的成员，例如字符串，列表或元组。 有两个成员运算符，如下所述 -
list = [1, 10, 20, 30]

if a in list:
    print("found")

# 7.身份运算符  比较两个对象的内存位置。常用的有两个身份运算符 is；is not
a = 20
b = 20
c = 50

if a is b:
    print(a is b)

if a is not c:
    print(a is not c)

# 8.运算符优先级
