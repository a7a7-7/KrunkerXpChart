import matplotlib.pyplot as plt
from constants.enums.weap_info import *

classes = weapClass.classes

def stat_graph(xp, username):
    # 14개의 값을 입력받기
    values = []
    for i in range(14):
        value = xp[i]
        values.append(value)

    plt.title(username + "'s class XP")
    # 원형 차트 그리기
    plt.pie(values, labels=[f'{classes[i]}' for i in range(14)], autopct='%1.1f%%', startangle=90)
    plt.show()
