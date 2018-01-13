import requests

# 向百度发送请求
# r = requests.get("https://b.bdstatic.com/boxlib/20171226/2017122616190866254209261.jpg")
r = requests.get(
    "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1515849818105&di=63880c6b9778fe3450d2d8a1eac1bee2&imgtype=0&src=http%3A%2F%2Fwww.deskcar.com%2Fdesktop%2Fstar%2Fchina%2F200967234621%2F1.jpg")

my_content = r.content

# 创建一个文件
f = open("picture.png", "wb")

# 写入数据到这个文件里面
f.write(my_content)

# 文件关闭
f.close()
