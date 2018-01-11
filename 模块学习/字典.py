# 一江夜雨  Python学习  2018
# 字典

dict_my = {'one': "This is one", 2: "This is my", 3: "哈哈嗯"}

tinydict = {'name': 'maxsu', 'code': 1024, 'dept': 'IT Dev'}

print("dict['one'] = ", dict_my['one'])  # Prints value for 'one' key
print('dict[2] = ', dict_my[2])  # Prints value for 2 key
print('tinydict = ', tinydict)  # Prints complete dictionary
print('tinydict.keys() = ', tinydict.keys())  # Prints all the keys
print('tinydict.values() = ', tinydict.values())  # Prints all the values

# 循环打印  key value
for w in tinydict.keys():
    print(w)

for w in tinydict.values():
    print(w)

# 更改
dict_my[2] = "yijiangyu"
print(dict_my)

# 添加
dict_my["four"] = "业余"
print(dict_my)

# 根据key删除
del dict_my["four"]
print(dict_my)

# 清除所有
dict_my.clear()
print(dict_my)

print(type(dict_my))
