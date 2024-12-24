import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import os

# 修改GitHub API URL，搜索Ruby语言的项目
URL = 'https://api.github.com/search/repositories?q=language:ruby&sort=stars'

try:
    # 发送GET请求到GitHub API
    r = requests.get(URL)
    r.raise_for_status()  # 如果响应状态码不是200，将抛出异常

    # 解析响应内容为JSON格式
    response_dict = r.json()
    print("Total repositories:", response_dict['total_count'])

    # 提取项目列表
    repo_dicts = response_dict['items']
    names, stars = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])

    # 设置图表样式
    my_style = LS('#333366', base_style=LCS)
    chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
    chart.title = 'Most-Starred Ruby Projects on GitHub'
    chart.x_labels = names
    chart.add('', stars)

    # 打印当前工作目录
    print("Current working directory:", os.getcwd())

    # 指定完整的文件路径
    file_path = 'D:/外星人游戏/shujukeshihua/ruby_repos.svg'
    chart.render_to_file(file_path)
    print("Chart saved as", file_path)

except requests.exceptions.RequestException as e:
    # 处理请求异常
    print(f"Request failed: {e}")
except ValueError as e:
    # 处理JSON解析异常
    print(f"JSON decode failed: {e}")
except Exception as e:
    # 处理其他异常
    print(f"An error occurred: {e}")