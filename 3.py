import pandas as pd
import matplotlib.pyplot as plt

# 读取CSV文件
df = pd.read_csv('world_fires_1_day.csv')

# 数据预处理
# 选择需要的列
data = df[['latitude', 'longitude', 'brightness']]

# 绘制散点图
plt.figure(figsize=(10, 8))
plt.scatter(data['longitude'], data['latitude'], c=data['brightness'], cmap='inferno', s=10)
plt.colorbar(label='Fire Brightness')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Global Fire Locations')
plt.grid(True)
plt.show()