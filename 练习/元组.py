# 一江夜雨  Python学习  2018
# 元组

tuple = ("welcome", "to", "101", "家庭")

tinytuple = (999.0, 'maxsu')

print('tuple = ', tuple)  # Prints complete tuple
print('tuple[0] = ', tuple[0])  # Prints first element of the tuple
print('tuple[1:3] = ', tuple[1:3])  # Prints elements starting from 2nd till 3rd
print('tuple[-3:-1] = ', tuple[-3:-1])  # 输出结果是什么？
print('tuple[2:] = ', tuple[2:])  # Prints elements starting from 3rd element
print('tinytuple * 2 = ', tinytuple * 2)  # Prints tuple two times
print('tuple + tinytuple = ', tuple + tinytuple)  # Prints concatenated tuple


# tuple[2] = 1000    # 无法更新值，程序出错
