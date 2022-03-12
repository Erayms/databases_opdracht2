from pymongo import *
import pandas as pd

client = MongoClient()
db = client["huwebshop"]


def products():
    products_col = db["products"]
    col = {'_id': 1, 'category': 1, 'price': 1, 'gender': 1, 'brand': 1, 'sub_category': 1}
    products = [x for x in products_col.find({}, col)]
    df = pd.DataFrame(products)
    df.to_csv("products.csv", index=False)

def profiles():
    profiles_col = db["profiles"]
    col2 = {'_id':1 , 'recommendations':1 , 'previously_recommended':1}
    profiles = [x for x in profiles_col.find({}, col2)]
    df = pd.DataFrame(profiles)
    df.to_csv("profiles.csv", index=False)

def sessions():
    sessions_col = db["sessions"]
    col3 = {'_id': 1, 'buid': 1, 'preferences': 1}
    sessions = [x for x in sessions_col.find({}, col3)]
    df = pd.DataFrame(sessions)
    df.to_csv("sessions.csv", index=False)

profiles()