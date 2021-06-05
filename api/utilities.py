import os
import json
import requests
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