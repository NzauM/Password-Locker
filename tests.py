import unittest
from users import Users

class TestUsers(unittest.TestCase):
    '''
    The test class defines test cases for the user class behaviors

    The unittest.TestCase helps in creating new test cases.
    '''
    def setUp(self):
        '''
        This method will run before each class
        '''
        self.new_user = Users("Merciee","Mercy","Nzau","October","Mercy10")


    def test_init(self):
        '''
        To check if the user object is instantiated ocrrectly 
        '''

        self.assertEqual(self.new_user.user_name,"Merciee")
        self.assertEqual(self.new_user.first_name,"Mercy")
        self.assertEqual(self.new_user.last_name,"Nzau")
        self.assertEqual(self.new_user.birth_month,"October")
        self.assertEqual(self.new_user.password,"Mercy10")
     




if __name__ == '__main__':
    unittest.main()