import requests #built_in-i alla laadimine ning enda faili importimine

API = "https://dashboard.elering.ee/api/nps/price?start=2026-09-29T00%3A00%3A00.000Z&end=2026-09-29T23%3A59%3A59.999Z"
response = requests.get(API)

data = response.json()

for el in data['data']['ee']:
    print(el)
