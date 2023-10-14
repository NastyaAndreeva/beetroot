import requests

API_KEY = "22d27572f8f4dfcfd42cf8880f3c8c6c"
city = input("Please, enter the city id: ")
url = f"http://api.openweathermap.org/data/2.5/forecast?id={city}&appid={API_KEY}"
requests.get(url)
resp = requests.get(url)
if resp.status_code in {200, 201, 202}:
    print('OK')
    print(resp.text)
else:
    print("KO")
    print(resp.status_code)