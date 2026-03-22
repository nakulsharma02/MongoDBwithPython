import pymongo 
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')# Establish a connection b/w mongodb server and python
mydb = client['Employee'] # Make a Database
empinfo = mydb.employeeinformation # Make a Collection
record = {
    'firstname' : 'Nakul',
    'lastname' : 'Sharma',
    'department' : 'Analytics',
    'qualification' : 'BTech',
    'age' : 23
}
# empinfo.insert_one(record)
records = [{
        'firstname':'John',
        'lastname':'Doe',
        'department':'Analytics',
        'qualification':'statistics',
        'age':35
        
        },
         {
        'firstname':'John ',
        'lastname':'Smith',
        'department':'Analytics',
        'qualification':'masters',
        'age':30
        
        },
        {
        'firstname':'Manish',
        'lastname':'Sen',
        'department':'Analytics',
        'qualification':'phd',
        'age':34
        
        },
        {
        'firstname':'Ram',
        'lastname':'Singh',
        'department':'Analytics',
        'qualification':'master',
        'age':32
        
        }]
# empinfo.insert_many(records)
# # Simple way of Querying 
a = empinfo.find_one() # Give the first document object
# print(a)
# # Select * from employeeinformation
records_ = empinfo.find() # it only gives a cursor or provide a cursor
# print(records_)
'''for record_ in records:
    print(record_)
'''
# Or we can use for record_ in empinfo.find({})

# # Querying the json documents based on Equality Conditions
# Select * from employeeinformation where firstname=Nakul
'''for record_ in empinfo.find({'firstname':'Nakul'}):
    print(record_)
'''

# # Query documents using query Operators($in,$lt,$gt)
'''for record in empinfo.find({'qualification':{'$in':['phd','masters']}}):
    print(record)
'''

# # And & Query Operators 
'''for record in empinfo.find({'qualification':'master','age':{'$lt':35}}):
    print(record)
'''

# # Or & Query Operators 
'''for record in empinfo.find({'$or':[{'firstname':'Nakul'},{'qualification':'master'}]}):
    print(record)
'''

inventory = mydb.inventory
'''inventory.insert_many( [
   { 'item': "journal", 'qty': 25, 'size': { 'h': 14, 'w': 21,'uom': "cm" }, 'status': "A" },
   { 'item': "notebook", 'qty': 50,'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "A" },
   { 'item': "paper", 'qty': 100, 'size': { 'h': 8.5, 'w': 11,'uom': "in" },'status': "D" },
   { 'item': "planner", 'qty': 75, 'size': { 'h': 22.85,'w': 30,'uom': "cm" },'status': "D" },
   { 'item': "postcard", 'qty': 45, 'size': { 'h': 10, 'w': 15.25,'uom': "cm" },'status': "A" }
])
'''
#  Insert some more data 
'''
for record in inventory.find({'size':{'h':14,'w':21,'uom':'cm'}}):
    print(record)'''

'''inventory.insert_many([
    {"item": "canvas",
     "qty": 100,
     "size": {"h": 28, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "journal",
     "qty": 25,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "mat",
     "qty": 85,
     "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
     "status": "A"},
    {"item": "mousepad",
     "qty": 25,
     "size": {"h": 19, "w": 22.85, "uom": "cm"},
     "status": "P"},
    {"item": "notebook",
     "qty": 50,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "P"},
    {"item": "paper",
     "qty": 100,
     "size": {"h": 8.5, "w": 11, "uom": "in"},
     "status": "D"},
    {"item": "planner",
     "qty": 75,
     "size": {"h": 22.85, "w": 30, "uom": "cm"},
     "status": "D"},
    {"item": "postcard",
     "qty": 45,
     "size": {"h": 10, "w": 15.25, "uom": "cm"},
     "status": "A"},
    {"item": "sketchbook",
     "qty": 80,
     "size": {"h": 14, "w": 21, "uom": "cm"},
     "status": "A"},
    {"item": "sketch pad",
     "qty": 95,
     "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
     "status": "A"}])
'''

# # pymongo.collection.Collection.update_one()
#  Update one item
'''inventory.update_one({'item':'sketch pad'},
                     {'$set':{'size.uom':'m','status':'p'},
                      '$currentDate':{'lastModified':True}})
'''

# # pymongo.collection.Collection.update_many()
# Update many items
'''inventory.update_many(
    {'qty':{'$lt':50}},
    {'$set':{'size.uom':'in','status':'P'},
    '$currentDate':{'lastModified':True}}
)
'''

# # pymongo.collection.Collection.replace_one()
# replace overall variable or item
'''inventory.replace_one({'item':'paper'},
                      {'item':'paper',
                       'instock':[
                           {'warehouse':'A','qty':60},
                           {'warehouse':'B','qty':40}
                       ]})'''
inventory.replace_one({'item':'paper','qty':100},
                      {'item':'paper',
                       'instock':[
                           {'warehouse':'A','qty':60},
                           {'warehouse':'B','qty':40}
                       ]})
