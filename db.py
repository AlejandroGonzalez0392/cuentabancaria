from pymongo import MongoClient

class Database:
    def _init_(self, uri="mongodb://localhost:27017/", db_name="cajero_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.users = self.db["users"]

    def insert_user(self, user_data):
        return self.users.insert_one(user_data)

    def find_user(self, user_id):
        return self.users.find_one({"user_id": user_id})

    def update_balance(self, user_id, new_balance):
        self.users.update_one({"user_id": user_id}, {"$set": {"balance": new_balance}})

    def delete_user(self, user_id):
        return self.users.delete_one({"user_id": user_id})