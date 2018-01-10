import random
# 机器人
computer = random.randint(1,3)

# 人类
people = int(input("请你出拳:1 石头 2 剪刀 3 布:"))

# 比赛判断
if (people == 1 and computer == 2) or (people == 2 and computer == 3) or (people == 3 and computer == 1):
    print("我赢了 好开心哦!!!")
elif people == computer:
    print("平局了 决战到天亮!!!")
else:
    print("你小子挺厉害 再来啊!!!")