import requests
import json

base_url = "https://russianwarship.rip/api/v2"

r_war = requests.get(f"{base_url}/war-info/status")
data = json.loads(r_war.text)
# print(data["data"]["alias"])

r_war_statistics = requests.get(f"{base_url}/statistics")
statistics =json.loads(r_war_statistics.text)
statistics_data = statistics["data"]["records"]
# for el in statistics_data:
#     print("------", el)

r_war_statistics_by_date = requests.get(f"{base_url}/statistics/2022-04-18")
statistics_data_by_date = json.loads(r_war_statistics_by_date.text)
# print(statistics_data_by_date["data"]["stats"])

r_war_terms = requests.get(f"{base_url}/terms/ua")
terms_data = json.loads(r_war_terms.text)
terms_dict = terms_data["data"]
# for key, value in terms_dict.items():
#     print(key, ": ", value["title"])

r_war_terms_by_term = requests.get(f"{base_url}/terms/ua/tanks")
terms_data_by_term = json.loads(r_war_terms_by_term.text)
terms_dict_by_term = terms_data_by_term["data"]
print(terms_dict_by_term)