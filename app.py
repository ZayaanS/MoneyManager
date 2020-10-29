import pymongo
from tkinter import *
from login import *

__author__ = "Zayaan"
mongodb_uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(mongodb_uri)
database = client['MoneyManager']
collection = database['Users']
user = current_user

# set main screen
main_screen = Tk()

# create start screen
create_start_screen(user, database, collection, main_screen)


