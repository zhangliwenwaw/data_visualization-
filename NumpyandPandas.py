import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 正确的GitHub API URL
URL = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

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

    # 使用 Pandas 创建 DataFrame
    df = pd.DataFrame({'Repository Name': names, 'Star Count': stars})

    # 打印 DataFrame
    print(df)

    # 使用 Matplotlib 进行数据可视化
    plt.figure(figsize=(10, 8))
    plt.barh(df['Repository Name'], df['Star Count'], color='skyblue')
    plt.xlabel('Star Count')
    plt.title('Most-Starred Python Projects on GitHub')
    plt.gca().invert_yaxis()  # 反转y轴，使得星标最多的项目在上方
    plt.show()

except requests.exceptions.RequestException as e:
    # 处理请求异常
    print(f"Request failed: {e}")
except ValueError as e:
    # 处理JSON解析异常
    print(f"JSON decode failed: {e}")
except Exception as e:
    # 处理其他异常
    print(f"An error occurred: {e}")