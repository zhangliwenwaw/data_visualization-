from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

chose1 = './data/sitka_weather_07-2021_simple.csv'
chose2 = './data/sitka_weather_2021_simple.csv'
title1 = '2021年7月温度'
title2 = '2021年温度'
highs = []
lows = []
dates, highs = [], []
path = Path(chose2)
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(current_date)
    high = int(row[4])
    low = int (row[5])
    highs.append(high)
    lows.append(low)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

ax.plot(dates, highs,color = 'red')
ax.plot(dates, lows, color = 'blue')
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
# 设置标题大小
ax.set_title(title2, fontsize=24)
ax.set_xlabel("日期", fontsize=14)
ax.set_ylabel("温度", fontsize=14)
#设置小字大小
ax.tick_params(labelsize=10)
plt.show()