from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['airmont']

collection = db['members']

# CRUD operations

document = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}
# result = collection.insert_one(document) # create

documents = [
    {"name": "Ethan", "age": 25, "city": "Los Angeles"},
    {"name": "Uriah", "age": 27, "city": "San Francisco"},
    {"name": "Ricky", "age": 35, "city": "Chicago"}
]
# results = collection.insert_many(documents) # create

results = collection.find({"age": {"$gt": 28}}) # read operation specifies age > 28

print("Users > age 28 in the database")
for doc in results:
    print(doc)

collection.update_one({"name": "John Doe"}, {"$set": {"name": "Joe"}})	# Update

collection.delete_one({"name": "Joe"})						# Delete

print("All current users")
for doc in collection.find():
    print(doc)

client.close()