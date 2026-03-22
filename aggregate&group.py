'''
1. Average
2. Sum 
3. Project

'''
from pymongo import MongoClient 
Client = MongoClient("mongodb://127.0.0.1:27017/")
mydatabase = Client['Students']
collection = mydatabase.scores
data =  [ 
    {"user":"Krish", "subject":"Database", "score":80}, 
    {"user":"Amit",  "subject":"JavaScript", "score":90}, 
    {"user":"Amit",  "title":"Database", "score":85}, 
    {"user":"Krish",  "title":"JavaScript", "score":75}, 
    {"user":"Amit",  "title":"Data Science", "score":60},
    {"user":"Krish",  "title":"Data Science", "score":95}] 
# collection.insert_many(data)
# # # Total Numbers of Records 
'''agg_result = collection.aggregate(
    [{
        '$group':
        {
            '_id':'$user',
            'TotalSubjects':{'$sum':1}
        }
    }]
)
for i in agg_result:
    print(i)
'''

'''# # # Calculate Total Scores based on user
agg_result = collection.aggregate([
    {
        '$group':{
            '_id' : '$user',
            'Total Marks':{'$sum':'$score'}

        }
    }
])
for i in agg_result:
    print(i)
'''

# Calculate the average score based on user 
'''agg_result = collection.aggregate([
    {
        '$group':{
            '_id':'$user',
            'Student_Scores_Average' : {'$avg':'$score'}
        }
    }
])
for i in agg_result:
    print(i)
'''

# Working on some date time
import datetime as datetime
# # # Create a new collection
'''data=[{ "_id" : 1, "item" : "abc", "price" : 10, "quantity" : 2, "date" : datetime.datetime.now()},
{ "_id" : 2, "item" : "jkl", "price" : 20, "quantity" : 1, "date" : datetime.datetime.now() },
{ "_id" : 3, "item" : "xyz", "price" : 5, "quantity" : 5, "date" : datetime.datetime.now() },
{ "_id" : 4, "item" : "abc", "price" : 10, "quantity" : 10, "date" : datetime.datetime.now() },
{ "_id" : 5, "item" : "xyz", "price" : 5, "quantity" : 10, "date" :datetime.datetime.now() }]
mycollection = mydatabase['stores']'''
# mycollection.insert_many(data)

# # # Calculate the average quantity and average price
'''agg_result = mycollection.aggregate([
    {
        '$group':{
            '_id':'$item',
            'avgAmount':{
                '$avg':{'$multiply':['$price','$quantity']}
            },
            'avgQuantity':{'$avg':'$quantity'}
        }
    }
])

for i in agg_result:
    print(i)
'''

# # # # $project - [It is just give results like a Select Statement]
data=[{
  "_id" : 1,
  "title": "abc123",
  "isbn": "0001122223334",
  "author": { "last": "zzz", "first": "aaa" },
  "copies": 5
},
{
  "_id" : 2,
  "title": "Baked Goods",
  "isbn": "9999999999999",
  "author": { "last": "xyz", "first": "abc", "middle": "" },
  "copies": 2
}
]
collection = mydatabase.Books
# collection.insert_many(data)
for row in collection.aggregate([{'$project':{'title':1,'isbn':1}}]):
    print(row)