from pymongo import MongoClient

from django.conf import settings


# Connect Django to the MongoDB server

client = MongoClient(
    settings.MONGODB["HOST"]
)


# Select the database

database = client[
    settings.MONGODB["DATABASE"]
]


# Create/select MongoDB collections

freshers_collection = database[
    "freshers"
]


progress_collection = database[
    "daily_progress"
]


assignments_collection = database[
    "assignments"
]


projects_collection = database[
    "projects"
]