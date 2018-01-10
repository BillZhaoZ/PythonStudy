# 一江夜雨  Python学习  2018
import random

while True:
    # 机器人
    computer = random.randint(1, 3)

    # 人类
    person = int(input("请你出拳： 1、石头  2、剪刀  3、布"))

    # 比赛判断
    if (person == 1 and computer == 2) or (person == 2 and computer == 3) or (person == 3 and computer == 1):
        print("我赢了，厉害吧！！！哈哈哈")
    elif person == computer:
        print("平局了，再来，决战到天亮")
    else:
        print("你小子很厉害，再来！！！")
