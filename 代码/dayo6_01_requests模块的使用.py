import requests

# 向百度发送请求
# r = requests.get("http://www.baidu.com")

# 向理性人发起请求
r = requests.get("https://www.lixinger.com/profile/599e31fbc4c455574556137d/stock?group-id=590ad461e462ea9389115e94")

# # 编码
# r.encoding = "utf-8"

# # 获取响应的数据
# my_content = r.text

# 获取响应的数据 二进制类型(推荐)
my_content = r.content.decode("utf-8")

print(my_content)
