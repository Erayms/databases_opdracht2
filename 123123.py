from pymongo import *
import pprint
import pandas as pd
from random import randint

client = MongoClient()
db = client["huwebshop"]

products_col = db["products"]
profiles_col = db["profiles"]
sessions_col = db["sessions"]


products = [x for x in products_col.find()]
profiles = [x for x in profiles_col.find()]
sessions = [x for x in sessions_col.find()]

col = ['_id', 'category', 'price', 'gender', 'brand', 'sub_category']
df = pd.DataFrame(products, columns=col)
df.to_csv("products", index=False)

col2 = ['_id', 'recommendations', 'previously_recommended']
df = pd.DataFrame(profiles, columns=col)
df.to_csv("profiles", index=False)

col3 = ['_id', 'recommendations', 'previously_recommended']
df = pd.DataFrame(profiles, columns=col)
df.to_csv("profiles", index=False)

