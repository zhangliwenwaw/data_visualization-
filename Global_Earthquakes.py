from pathlib import Path
import json
import plotly.express as px

data1 = './data/eq_data_1_day_m1.geojson'
data2 = './data/eq_data_7_day_m1.geojson'
data3 = './data/eq_data_30_day_m1.geojson'

#以字符串形式读取数据并转换为Python对象。
path = Path(data3)
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#创建一个更易读的数据文件。
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

#检查数据集中的所有地震。
all_eq_dicts = all_eq_data['features']  # 一个列表，每个元素是一个字典

mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

title = '全球地震'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
        color=mags,
        color_continuous_scale='Viridis',
        labels={'color':'震级'},
        projection='natural earth',
        width=1200, height=800,
    )

fig.show()