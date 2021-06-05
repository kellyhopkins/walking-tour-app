import os
import json
import random
import requests
import pandas as pd
from faker import Faker
fake = Faker()

profile = lambda: {"username": fake.user_name(), "password": fake.dga(length=10)}

categories = ["Restaurants", "Retail", "Public Landmark", "Parks/Recreation", "Religious"]
location = lambda: {
    "loc_name": fake.company() + " " + fake.company_suffix(), 
    "loc_address": fake.address(), 
    "loc_description": fake.catch_phrase(), 
    "loc_category": fake.random_element(categories)
}

loc_data = pd.read_csv("data/GeoIDs - City.csv")
loc_data["citystate"] = loc_data.apply(lambda x: x.cityname + ", " + x.stateabbrev, axis=1)
fake.random_element(loc_data.citystate)

tour = lambda: {
    "tour_name": fake.sentence(nb_words=5).replace(".", ""),
    "tour_location": fake.random_element(loc_data.citystate),
    "tour_num_stops": random.randint(1,10)
}



print(json.dumps(profile(), indent=4))

os.environ['NO_PROXY'] = '127.0.0.1'
r = requests.get('http://127.0.0.1:5000')
print(r.content)

url = 'http://127.0.0.1:5000'
headers = {
    "Content-Type": "application/json"
}
payload = profile()
r = requests.post(url, data=payload)