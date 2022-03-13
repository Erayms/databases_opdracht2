from pymongo import *
import pandas as pd

client = MongoClient()
db = client["huwebshop"]

#pakt de info van de mongodb uit de collection products
def products():
    products_col = db["products"]
    col = {'_id': 1, 'brand': 1, 'category': 1, 'gender': 1, 'sub_category': 1, 'sub_sub_category': 1}
    #pakt hier alleen de dingen met een 1 erbij
    products = [x for x in products_col.find({}, col)]
    df = pd.DataFrame(products)
    df.to_csv("products.csv", index=False, sep=";")
    #maakt er een csv file van om dan die in te lezen in postgresql

#pakt de info van de mongodb uit de collection profiles
def profiles():
    profiles_col = db["profiles"]
    col2 = {'_id':1 , 'buids': 1, 'recommendations':1 , 'previously_recommended':1}
    #pakt hier alleen de dingen met een 1 erbij
    profiles = [x for x in profiles_col.find({}, col2)]
    df = pd.DataFrame(profiles)
    df.to_csv("profiles.csv", index=False, sep=";")
    #maakt er een csv file van om dan die in te lezen in postgresql

#pakt de info van de mongodb uit de collection profiles
def sessions():
    sessions_col = db["sessions"]
    col3 = {'buid': 1, 'preferences': 1}
    #pakt hier alleen de dingen met een 1 erbij
    sessions = [x for x in sessions_col.find({}, col3)]
    df = pd.DataFrame(sessions)
    df.to_csv("sessions.csv", index=False, sep=";")
    #maakt er een csv file van om dan die in te lezen in postgresql



