from urllib import response
import requests
from plotly.graph_objs import bar
from plotly import offline


url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers) 
print (f"status code: {r.status_code}")
response_dict = r.json()

print(f"Response keys are: {response_dict.keys()}")
print(f"Rotal count is: {response_dict['total_count']}")

repo_dicts = response_dict["items"]
repo_dict = repo_dicts[0]

print(f"\nKeys: {len(repo_dict)}")
for x in sorted(repo_dict.keys()):
    print(x)

repo_name,repo_stars = [],[]
for repo in repo_dicts:
    repo_name.append(repo['name'])
    repo_stars.append(repo['stargazers_count'])
print(repo_name,repo_stars)

data = {
    'type': 'bar',
    'x': repo_name,
    'y': repo_stars,
}
layout = {
    'title': 'Most Starred Python Repos',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
    }
fig = {'data':data, 'layout':layout}
offline.plot(fig,filename="python_repos.html")

