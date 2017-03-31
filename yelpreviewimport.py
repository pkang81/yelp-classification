import json, requests
from pymongo import MongoClient

#put the s3 here
url = "https://awebsite.com/afile.json"

resp = requests.get(url=url)
data = json.loads(response.read())
data = json.loads(resp.read())
x = resp.json()

client = MongoClient()
db = client.yelp


for item in x:
    db.yelp.insert_one(item)
