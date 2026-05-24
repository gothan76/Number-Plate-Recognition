from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
# MongoDB connection
CONNECTION_STRING = os.getenv("MONGO_URI")
# CONNECTION_STRING = "mongodb+srv://gothandaraman314_db_user:XRiPTPoFnyLXnCxX@gothan.mgapygv.mongodb.net/?appName=Gothan"

# Connect to MongoDB Atlas
client = MongoClient(CONNECTION_STRING)

db = client["number_plate_recognition"]
users_collection = db["users"]


# Function to find all users
def find_all_users():
    users = users_collection.find()

    for user in users:
        print(user)


# Call the function
find_all_users()