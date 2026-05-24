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

# Function to add a new user and update the database with the QR code path
def add_new_user():
    # Get user details interactively
    user_id = int(input("Enter User ID: "))
    license_no = input("enter the license plate number : ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    mobile_number = int(input("Enter Mobile Number: "))
    wallet_balance = float(input("Enter Wallet Balance: "))

    # Create user data (without the QR code path for now)
    user_data = {
        "user_id": user_id,
        "number_plate":license_no,
        "user_name": name,
        "age": age,
        "mobile_number": mobile_number,
        "wallet_balance": wallet_balance
    }

    # Insert the user data into MongoDB
    users_collection.insert_one(user_data)

add_new_user()