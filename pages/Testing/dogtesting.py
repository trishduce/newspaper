
import unittest
import dog

class TestDog(unittest.TestCase):

    def setUp(self):
    	self.dog1 = dog.Dog("Dempsey", 3)

    def test_name(self):
        self.assertEqual(self.dog1.name, 'Dempsey')

    def test_age(self):
        self.assertEqual(self.dog1.age, 3)


if __name__ == '__main__':
    unittest.main()
