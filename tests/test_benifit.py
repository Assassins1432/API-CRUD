import unittest
from app import create_app
from app.services.mongo_service import MongoService

class BenefitTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.mongo_service = MongoService()

    def test_create_benefit_success(self):
        response = self.app.post('/benefits', json={
            'name': 'Test Benefit',
            'description': 'This is a test benefit.',
            'provider': 'Test Provider',
            'expiration_date': '2024-12-31'
        })
        self.assertEqual(response.status_code, 201)

    def test_create_benefit_invalid_data(self):
        response = self.app.post('/benefits', json={
            'name': '',  # Invalid data
            'description': 'This is a test benefit.',
            'provider': 'Test Provider',
            'expiration_date': '2024-12-31'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.json['error'])

    def test_get_benefit_not_found(self):
        response = self.app.get('/benefits/invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json)

    def tearDown(self):
        # Cleanup code can be added here
        pass

if __name__ == "__main__":
    unittest.main()
