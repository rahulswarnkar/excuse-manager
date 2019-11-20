from unittest import TestCase
from unittest.mock import patch, Mock
import main

class TestStringMethods(TestCase):

    @patch('service.add')
    def test_add(self, mock):
        with main.app.test_client() as c:
            c.post("/excuses",
                data = '{"message":"dummy excuse"}',
                headers = {'content-type':'application/json'})
            mock.assert_called_once()

    @patch('service.add')
    def test_add_status(self, mock):
        with main.app.test_client() as c:
            response = c.post("/excuses",
                data = '{"message":"dummy excuse"}',
                headers = {'content-type':'application/json'})
            self.assertEqual(response.status_code, 201, 'status code do not match')
            #assert response content and content type

    @patch('service.get_all')
    def test_list(self, mock):
        with main.app.test_client() as c:
            mock.return_value = [{"id": 1, "message":"dummy excuse"}]
            response = c.get("/excuses")
            mock.assert_called_once_with()

    @patch('service.get_all')
    def test_list_status(self, mock):
        with main.app.test_client() as c:
            mock.return_value = [{"id": 1, "message":"dummy excuse"}]
            response = c.get("/excuses")
            self.assertEqual(response.status_code, 200, 'status code do not match')
            #assert response content and content type

    @patch('service.get_by_id')
    def test_get_by_id(self, mock):
        with main.app.test_client() as c:
            mock.return_value = {"id": 1, "message":"dummy excuse"}
            response = c.get("/excuses/1")
            mock.assert_called_once_with(1)

    # @patch('service.get_by_id')
    # def test_get_by_id_200(self, mock):
    #     pass

    # @patch('service.get_by_id')
    # def test_get_by_id_404(self, mock):
    #     pass

    # @patch('service.delete_by_id')
    # def test_delete(self, mock):
    #     pass

    @patch('service.delete_by_id')
    def test_delete_200(self, mock):
        with main.app.test_client() as c:
            mock.return_value = True
            response = c.delete("/excuses/1")
            self.assertEqual(response.status_code, 200, 'status code do not match')

    # @patch('service.delete_by_id')
    # def test_delete_404(self, mock):
    #     pass

if __name__ == '__main__':
    unittest.main()
