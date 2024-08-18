import requests

result = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
final = result.json()

for i in range(len(final)):
    print(final[i]["user"]["login"])