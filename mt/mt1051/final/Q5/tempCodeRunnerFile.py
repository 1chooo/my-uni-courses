import numpy as np
import matplotlib.pyplot as plt

income_src_names = [
    "唱片", 
    "演唱會門票", 
    "廣告合約", 
    "出席典禮活動",
]

singers = [
    "Adam",
    "Bono",
    "Cody",
]

income_src_price = np.array(
    [750, 7_200, 3_000_000, 550_000]
)

income_src_amount = np.array([
    [4_000_000, 79_000, 10, 6],
    [2_500_000, 45_000, 5, 3],
    [150_000, 9_700, 2, 1],
])

# 计算每位歌手的總收入
total_income_per_singer = np.sum(income_src_amount * income_src_price, axis=1)

def draw_bar(singers, total_income_per_singer):
    plt.figure(figsize=(8, 6))  # 设定图形尺寸

    # 设置不同颜色的列表
    colors = ['skyblue', 'salmon', 'lightgreen']

    # 绘制长条图
    bars = plt.bar(singers, total_income_per_singer, color=colors)

    # 添加标题和标签
    plt.title('每位歌手的總收入')
    plt.xlabel('歌手')
    plt.ylabel('總收入')

    # 显示每个长条上的具体数值
    for bar, income in zip(bars, total_income_per_singer):
        plt.text(bar.get_x() + bar.get_width()/2, 
                 bar.get_height() + 10000, 
                 f'{income}', 
                 ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    plt.show()

# 使用函数绘制长条图
draw_bar(singers, total_income_per_singer)
