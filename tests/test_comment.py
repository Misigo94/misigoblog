import unittest
from app.models import Comment

class CommentsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_comment = new_comment(
            "1",
            "martin", 
            "This is Martins project creaet your best pitch here"
            )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment,Comment))
