import requests

url = "https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol"
requests.get(url)
resp = requests.get(url)
if resp.status_code in {200, 201, 202}:
    print('OK')
    with open("robots.txt", "w+") as file:
        file.write(str(resp.content))
else:
    print("KO")