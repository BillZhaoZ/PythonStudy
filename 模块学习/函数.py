# # 3. 编写一段代码，定义一个函数求1-100之间所有整数的和，并调用改函数打印出结果。
#
#
# def sum_add(a):
#     i = 0
#     sum = 0
#
#     while i < a:
#         i += 1
#         sum += i
#
#     print(sum)
#     return sum
#
#
# c = str(sum_add(100))
# print("0-100的和为：" + c)
#
# # 定义一个函数 实现99乘法表的打印
#
# for i in range(10):
#     s = ""
#
#     for j in range(1, i + 1):
#         s += str(j) + "*" + str(i) + "=" + str(j * 1) + '\t'
#
#     print(s)


i = 5


def f(arg=i):
    print(arg)


i = 6
f()
