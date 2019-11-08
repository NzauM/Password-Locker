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


        