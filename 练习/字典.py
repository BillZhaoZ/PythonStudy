# 一江夜雨  Python学习  2018

dict_my = {}

dict_my['one'] = "This is one"
dict_my[2] = "This is my"

tinydict = {'name': 'maxsu', 'code': 1024, 'dept': 'IT Dev'}

print("dict['one'] = ", dict_my['one'])  # Prints value for 'one' key
print('dict[2] = ', dict_my[2])  # Prints value for 2 key
print('tinydict = ', tinydict)  # Prints complete dictionary
print('tinydict.keys() = ', tinydict.keys())  # Prints all the keys
print('tinydict.values() = ', tinydict.values())  # Prints all the values

for w in tinydict.keys():
    print(w)
