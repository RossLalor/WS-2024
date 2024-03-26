import unittest
import requests
import random
import string

class TestAPIEndpoints(unittest.TestCase):
    # Base URL of your Flask application
    BASE_URL = 'http://localhost:5000'
    ENDPOINT = '/'  # Replace with your actual endpoint

    # Test 01: Ping the pages

    def test_home(self):
        """Test the home endpoint."""
        response = requests.get(f'{self.BASE_URL}/')
        self.assertEqual(response.status_code, 200)

    def test_get_products(self):
        """Test the getProducts endpoint."""
        response = requests.get(f'{self.BASE_URL}/getProducts')
        self.assertEqual(response.status_code, 200)

    def test_get_titles(self):
        """Test the getTitles endpoint."""
        response = requests.get(f'{self.BASE_URL}/getTitles')
        self.assertEqual(response.status_code, 200)
        
    

if __name__ == '__main__':
    unittest.main()