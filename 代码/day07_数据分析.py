# 导入我们的画图工具
# as是起别名的功能
from matplotlib import pyplot as plt
import matplotlib

# 设置中文,解决中文乱码问题
font = {
    "family": "AR PL UMing CN, SimHei",
    "size": "10"
}
matplotlib.rc("font", **font)

# 描述一下今天10点钟的一个气温分布
x = ["10点00分", "10点10分", "10点20分", "10点30分", "10点40分", "10点50分", "11点00分"]
y = ["15℃", "16℃", "13℃", "14℃", "18℃", "15℃", "17℃"]

# 设置图片的大小
plt.figure(figsize=(20, 10), dpi=80)

# 画图,存放在内存中,并没有显示到屏幕上
plt.plot(x, y)

# 对图片进行详细的说明
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("2017年1月13日 10点到11点的 温度分布图")

# 保存图片
# plt.savefig("2.jpg")

# 把绘制好的图片显示出来
plt.show()
