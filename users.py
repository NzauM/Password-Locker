class Users:
    '''
    Class that generates new instances of users
    '''
    users_list = []
    

    
    def save_users(self):
        '''
        This method will save all users to the user list
        '''
        Users.users_list.append(self)



    def __init__ (self,user_name,first_name,last_name,birth_month,password):
        '''
        This is a blueprint that every user instance must conform to
        '''
        self.user_name = user_name
        self.first_name = first_name
        self.last_name = last_name
        self.birth_month = birth_month
        self.password = password

    @classmethod
    def find_user_byPassword(cls,password):
        '''
        This method will take in a password and check if the password exists to find the user
        '''

        for user in cls.users_list:
            if user.password == password:
                return user
        

    @classmethod
    def user_registered(cls,user_name,password):
        '''
        Method that checks if a user exists in the user list.Will help in authentication
        '''

        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return True
            
            return False
