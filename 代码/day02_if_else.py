# 需求
# 定义一个整数变量记录年龄
# input函数 : 接收数据(键盘)
# 注意 input函数在接受的数据 全部默认是字符串类型
age = input("请输入你的年龄:")  # 字符串类型 str
age = int(age)                   # 整形 int

# 判断是否满 18 岁 （>=）
# 如果满 18 岁，允许进网吧嗨皮
if age >= 18:
    print("进网吧玩耍")
else:
    print("小哥哥 你还不满18岁")