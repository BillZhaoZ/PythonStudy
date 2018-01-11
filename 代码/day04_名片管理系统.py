# 需求分析
# 1 新建名片
# 2 显示全部名片
# 3 查询某个人的信息

# 所有的数据放这里
cards = []


# 查找一个人的信息
def find_card():
    name = input("请输入你想查找的人的名字:")

    for i in cards:
        if i["姓名"] == name:
            print("这个人的信息是:")
            print(i)
            break
    else:
        print("查无此人...")


# 显示所有的名片信息
def show_all_card():
    print("@" * 50)
    print("所有的名片信息如下:")
    for temp in cards:
        print(temp)
    print("@" * 50)


# 增加一个名片
def add_card():
    name = input("请输入你的姓名:")
    age = input("请输入你的年龄:")
    tel = input("请输入你的电话:")

    # 使用一个字典来标示一个人的详细信息
    card = {
        "姓名": name,
        "年龄": age,
        "电话": tel
    }

    # 向cards里添加一个信息
    cards.append(card)

    print("添加成功,这个人的信息是:")
    print(card)


def show_menue():
    print("#" * 50)
    print("____欢迎使用[名管理系统]____")
    print("1 新建名片")
    print("2 显示全部名片")
    print("3 查询某个人的信息")
    print("#" * 50)

    num = input("请输入你的选项:")
    if num == "1":
        add_card()
    elif num == "2":
        show_all_card()
    elif num == "3":
        find_card()
    else:
        print("输入错误...")


while True:
    show_menue()
