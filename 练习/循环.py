# 一江夜雨  Python学习  2018


# words = ["你好", "我是", "你", "吗？？"]
#
# for s in words:
#     print(s)
#
# for w in range(4):
#     print(w)
#
# for w in range(0, 10, 3):
#     print(w)


# a = ['Mary', 'had', 'a', 'little', 'lamb']
#
# for i in range(len(a)):
#     print(i, a[i])


for n in range(2, 10):
    if n % 2 == 0:
        print("发现一个偶数" + str(n))
        continue

    print("奇数" + str(n))

# while 循环
# 例子1
i = 1

while i <= 5:
    print("hello world")
    i += 1
print("循环结束后的：i = %d" % i)

# 例子2
count = 0

while count < 9:
    print('The count is:', count)
    count += 1

print("Good bye!")
