# 编写代码，1-7七个数字，分别代表周一到周日，如果输入的数字是6或7，输出“周末”，
# 如果输入的数字是1-5，输出“工作日”，如输入其他数字，输出“错误”。

user_input = int(input("请输入数字1--7"));

if user_input == 6 or user_input == 7:
    print("周末")
elif (user_input >= 1) and (user_input <= 5):
    print("工作日")
else:
    print("错误")
