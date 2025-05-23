from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read URI from environment
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = AsyncIOMotorClient(MONGO_URI)

# Select the database and collection
db = client["social_db"]  # Replace with your DB name
collection = db["replies"]  # Replace with your collection name
