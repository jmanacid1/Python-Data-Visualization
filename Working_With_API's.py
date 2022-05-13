from urllib import response
import requests


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
print('\n')
print(repo_dict['trees_url'])
