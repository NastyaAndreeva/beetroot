import json

def make_country(name, capital):
    country = {name: capital}
    return country

new_country = make_country("Ukraine", "Kiev")

with open("country.json", "w+") as outfile:
    json.dump(new_country, outfile)