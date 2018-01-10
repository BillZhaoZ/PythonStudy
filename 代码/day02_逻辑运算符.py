# 判断年龄是否在0 到 120 之间

age = int(input("请输入你的年龄:"))

if 0 < age < 120:
    print("符合要求1")

if age == 20 or age == 25:
    print("符合要求2")

is_ok = False  # bool 布尔类型的数据

if not is_ok:
    print("符合要求3")
