from pymongo import MongoClient

# Connect to MongoDB using the container name as the host
client = MongoClient('mongodb://localhost:27017/')

# Specify the database and collection
db = client['mydatabase']
collection = db['mycollection']

# Sample data to insert
data = {
    "name": "John D455345oe 1234",
    "email": "johndoe@example.com",
    "age": 30
}

# Insert data into the collection
insert_result = collection.insert_one(data)

# Print the inserted ID to confirm success
print(f"Data inserted with ID: {insert_result.inserted_id}")