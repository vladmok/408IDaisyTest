from pymongo import MongoClient
import datetime

client = MongoClient(mongodb://Vlad:password@ds253889.mlab.com:53889/records)
db = client.test_database

collection = db.test_collection

record = {"Name": "Vlad",
        "Score": "500",
        "Date": datetime.datetime.utcnow()}
records = db.record
record_id = records.insert_one(record).inserted_id
