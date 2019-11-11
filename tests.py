import unittest
from users import Users
from credentials import Credentials

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
        self.new_credential = Credentials("Facebook","Mercy Nzau","M2001")
    def tearDown(self):
        '''
        The tear down method which will clean up after every test case is complete
        '''

        Users.users_list = []
        Credentials.credentials_list = []
       
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

    def test_credentials_init(self):
        '''
        To check if the credentials object is correctly instantiated
        '''
        self.assertEqual(self.new_credential.aname,"Facebook")
        self.assertEqual(self.new_credential.ausername,"Mercy Nzau")
        self.assertEqual(self.new_credential.apassword,"M2001")

    def test_save_users(self):
        '''
        Test case to test if the user objects are saved 
        '''
        self.new_user.save_users()
        self.assertEqual(len(Users.users_list),1)

    def test_save_credentials(self):
        '''
        Test_save_credentials a tes tcase to see if a credential object has been saved
        '''

        self.new_credential.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1) 

    def test_save_moreThanOne_USer(self):
        '''
        Testcase to test whether more than one user can be added to the user list
        '''

        self.new_user.save_users()
        test_user = Users("BeckyJ","Becka","Mbulwa","July","Becka7")
        test_user.save_users()
        self.assertEqual(len(Users.users_list),2)

    def test_save_multiple_credentials(self):
        '''
        TO test if more than one objects of the credentials can be saved
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials("Instagram","Miss Nzau","M8742")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_find_user_byPassword(self):
        '''
        To see if we can find he details of a user by using their username
        Will help us to match users to their passwords
        '''
        self.new_user.save_users()
        test_user = Users("BeckyJ","Becka","Mbulwa","July","Becka7")
        test_user.save_users()

        User_found = Users.find_user_byPassword("Becka7")
        self.assertEqual(User_found.password,test_user.password)

    def test_find_credentials_using_appname(self):
        '''
        This test wil check if a user can find their saved credentials using 
        the respective appname
        '''

        self.new_credential.save_credentials()
        test_credentials = Credentials("Instagram","Miss Nzau","M8742")
        test_credentials.save_credentials()

        credentials_found = Credentials.find_credentials_using_appname("Instagram")
        self.assertEqual(credentials_found.app_username,test_credentials.app_username)

    def test_user_registered(self):
        '''
        To check if a user is already registered
        '''
        self.new_user.save_users()
        test_user = Users("BeckyJ","Becka","Mbulwa","July","Becka7")
        test_user.save_users()

        user_registered = Users.user_registered("BecKyJ","Becka7")
        
        self.assertFalse(user_registered)

    def test_display_credentials(self):
        '''
        Test_Display_credentials will check if all redential of a user can be displayed
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)



    


     





if __name__ == '__main__':
    unittest.main()