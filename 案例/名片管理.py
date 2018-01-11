# 一江夜雨  Python学习  2018

# 创建一个名片管理系统
# 1、新建名片   2.显示全部名片   3.查询某人

# 存放名片信息的列表
cards = []


def add_card():
    """
    添加信息
    """
    print("添加信息：")

    name = input("    请输入姓名：")
    age = input("     请输入年龄：")
    tel = input("     请输入电话：")

    # 使用一个字典来标示一个人的详细信息
    card = {
        "姓名": name,
        "年龄": age,
        "电话": tel
    }

    cards.append(card)

    print("添加成功,信息如下:")
    print(card)


def show_all_info():
    """
    展示所有信息
    :return:
    """
    if len(cards) == 0:
        print("系统下还没有名片信息，请添加")
        return

    print("*" * 20)
    print("所有的名片信息如下：")

    for i in cards:
        print(i)

    print("*" * 20)


def search_info():
    """
    查询信息
    """
    name = input("请输入你要查询人的姓名:")

    for i in cards:
        if i["姓名"] == name:
            print("查询到信息如下：")
            print(i)
            break
    else:
        print("查无此人")


def card_system():
    """
    系统入口
    """
    print("*" * 20)
    print("欢迎使用【精英名片管理系统】")
    print("功能如下：")
    print("     1、新建个人名片")
    print("     2、显示名片列表")
    print("     3、查询某人名片")
    print("*" * 20)

    num = input("请输入您的选项：")

    if num == "1":
        add_card()
    elif num == "2":
        show_all_info()
    elif num == "3":
        search_info()
    else:
        print("输入错误!!")


# 开启系统
while True:
    card_system()
