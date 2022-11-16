import unittest
import requests
import json

class TestFlaskApiUsingRequests(unittest.TestCase):
    def test_hello_world_without_headers(self):
        response = requests.get('http://localhost:5000')
        assert response.text == "<p>Hello, World</p>"

    def test_hello_world_with_headers(self):
        response = requests.get('http://localhost:5000', headers={"Accept":"application/json"})
        assert response.text.strip() == "{\"message\":\"hello world\"}"


if __name__ == "__main__":
    unittest.main()