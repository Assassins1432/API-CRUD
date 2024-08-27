import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

class MongoService:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client['taller_fastapi']
        self.collection = self.db['beneficios']

    def create_benefit(self, benefit):
        return self.collection.insert_one(benefit).inserted_id

    def get_benefit(self, benefit_id):
        return self.collection.find_one({"_id": benefit_id})

    def update_benefit(self, benefit_id, data):
        return self.collection.update_one({"_id": benefit_id}, {"$set": data})

    def delete_benefit(self, benefit_id):
        return self.collection.delete_one({"_id": benefit_id})

    def get_all_benefits(self):
        return list(self.collection.find())
