from pymongo import *
import pandas as pd

client = MongoClient()
db = client["huwebshop"]


def products():
    products_col = db["products"]
    products = [x for x in products_col.find()]
    col = ['_id', 'category', 'price', 'gender', 'brand', 'sub_category']
    df = pd.DataFrame(products, columns=col)
    df.to_csv("products", index=False)


def profiles():
    profiles_col = db["profiles"]
    profiles = [x for x in profiles_col.find()]
    col2 = ['_id', 'recommendations', 'previously_recommended']
    df = pd.DataFrame(profiles, columns=col2)
    df.to_csv("profiles", index=False)

def sessions():
    sessions_col = db["sessions"]
    sessions = [x for x in sessions_col.find()]
    col3 = ['_id', 'user_agent']
    df = pd.DataFrame(sessions, columns=col3)
    df.to_csv("sessions", index=False)

sessions()