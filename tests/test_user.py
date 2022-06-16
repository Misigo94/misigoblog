import unittest
from app.models import User

class UsersTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_user = User(
            "1",
            "martin", 
            "martin@gmail.com", 
            "password"
            )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))
