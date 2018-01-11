# 一江夜雨  Python学习  2018
# 列表

list = ["nihao", "woshi", "bill", "zainali", "jianguoni"]
tinylist = [123, 'john']

print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

# 更新列表
list[2] = "一江夜雨"

print(list)

# 删除元素
del list[4]
print(list)

# 长度
print(len(list))

print(list[-1])
