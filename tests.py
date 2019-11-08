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

    def tearDown(self):
        '''
        The tear down method which will clean up after every test case is complete
        '''

        Users.users_list = []
        '''
        This will remove every test user instance after evry test case is complete
        '''

    def test_init(self):
        '''
        To check if the user object is instantiated ocrrectly 
        '''

        self.assertEqual(self.new_user.user_name,"Merciee")
        self.assertEqual(self.new_user.first_name,"Mercy")
        self.assertEqual(self.new_user.last_name,"Nzau")
        self.assertEqual(self.new_user.birth_month,"October")
        self.assertEqual(self.new_user.password,"Mercy10")

    def test_save_users(self):
        '''
        Test case to test if the user objects are saved 
        '''
        self.new_user.save_users()
        self.assertEqual(len(Users.users_list),1)


    f test_save_moreThanOne_USer(self):
        '''
        Testcase to test whether more than one user can be added to the user list
        '''

        self.new_user.save_users()
        test_user = Users("BeckyJ","Becka","Mbulwa","July","Becka7")
        test_user.save_users()
        self.assertEqual(len(Users.users_list),2)

    
     




if __name__ == '__main__':
    unittest.main()