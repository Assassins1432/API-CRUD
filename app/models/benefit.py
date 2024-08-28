from pymongo import MongoClient

class Benefit:
    def __init__(self, data):
        self.title = data.get('title')
        self.description = data.get('description')
        self.expirationDate = data.get('expirationDate')
        self.link = data.get('link')
        self.ubication = data.get('ubication')
        self.termsConditions = data.get('termsConditions')
        self.image = data.get('image')

    @staticmethod
    def to_json(benefit):
        return {
            'title': benefit.title,
            'description': benefit.description,
            'expirationDate': benefit.expirationDate,
            'link': benefit.link,
            'ubication': benefit.ubication,
            'termsConditions': benefit.termsConditions,
            'image': benefit.image
        }
