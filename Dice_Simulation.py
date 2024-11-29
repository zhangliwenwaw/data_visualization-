import numpy as np
import plotly.express as px

number = 3
size = 1
num_sides = 6  

# 模拟掷骰子的结果
results = np.random.randint(1, num_sides + 1, size=(size, number))  

# 计算每个可能的总点数出现的次数
poss_results = np.arange(number, number * num_sides + 1)  
frequencies = np.zeros(poss_results[-1] - poss_results[0] + 1) 

# 计算频率
for roll in results:
    total = np.sum(roll)
    if total in poss_results:
        frequencies[total - poss_results[0]] += 1

title = f"{number}个骰子{size}次模拟结果"
labels = {'x': '总点数', 'y': '命中次数'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.show()