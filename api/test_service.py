from importlib import reload
from unittest import TestCase
import service
class TestStringMethods(TestCase):

    def setUp(self):
        reload(service)

    def test_add(self):#what's wrong here?
        service.add({"message":"dummy excuse 1"})
        service.add({"message":"dummy excuse 2"})
        excuses = service.get_all()
        self.assertEqual(len(excuses), 2, "length doesn't match")
        excuse = excuses[0]
        self.assertIn('id', excuse.keys(), "id wasn't generated")

    # def test_get_all(self):
    #     pass

    # def test_get_by_id(self):
    #     pass

    # def test_delete_by_id(self):
    #     pass

if __name__ == '__main__':
    unittest.main()