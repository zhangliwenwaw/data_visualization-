import requests
import plotly.express as px

url = (
    "https://api.github.com/search/repositories"
    + "?q=language:python+sort:stars+stars:>10000"
)
headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)

# Convert the response object to a dictionary.
response_dict = r.json()

# Explore information about the repositories.
repo_dicts = response_dict['items']

# Examine the first repository.
repo_dict = repo_dicts[0]

repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    # Turn repo names into active links.
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}' style='color: black;'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    # Build hover texts.
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# Make visualization.
title = "GitHub最受欢迎的仓库排行"
labels = {'x': '仓库名', 'y': '访问量'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels,
        hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20,
        yaxis_title_font_size=20)

fig.show()