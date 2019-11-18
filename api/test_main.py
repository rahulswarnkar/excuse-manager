import unittest
import main

class TestStringMethods(unittest.TestCase):

    def test_add(self):
        with main.app.test_client() as c:
            response = c.post("/excuses",
                data = '{"message":"dummy excuse"}',
                headers={'content-type':'application/json'})
            self.assertEqual(response.status_code, 201, 'status code do not match')

    def test_list(self):
        with main.app.test_client() as c:
            response = c.get("/excuses")
            self.assertEqual(response.status_code, 200, 'status code do not match')

if __name__ == '__main__':
    unittest.main()