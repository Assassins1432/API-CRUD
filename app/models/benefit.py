from pymongo import MongoClient

class Benefit:
    def __init__(self, data):
        self.name = data.get('name')
        self.description = data.get('description')
        self.provider = data.get('provider')
        self.expiration_date = data.get('expiration_date')

    @staticmethod
    def to_json(benefit):
        return {
            'name': benefit.name,
            'description': benefit.description,
            'provider': benefit.provider,
            'expiration_date': benefit.expiration_date
        }
