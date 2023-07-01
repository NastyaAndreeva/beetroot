def make_country(name, capital):
    country = {name: capital}
    for key, value in country.items():
        print(key, ": ", value)

make_country("Ukraine", "Kiev")