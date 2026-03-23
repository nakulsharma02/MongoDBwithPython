from pymongo import MongoClient
Client = MongoClient("mongodb+srv://nakulsharmavats123:nakulsharma123@mydb.xkosnvr.mongodb.net/")
database = Client['Students']
collection = database.studentscores
data = [ 
    {"user":"Krish", "subject":"Database", "score":80}, 
    {"user":"Amit",  "subject":"JavaScript", "score":90}, 
    {"user":"Amit",  "title":"Database", "score":85}, 
    {"user":"Krish",  "title":"JavaScript", "score":75}, 
    {"user":"Amit",  "title":"Data Science", "score":60},
    {"user":"Krish",  "title":"Data Science", "score":95}] 
# collection.insert_many(data)
collection.delete_one({'user':'Krish'})
