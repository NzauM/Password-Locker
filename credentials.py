class Credentials:
    '''
    This class will generate new instances of the credentials class
    '''
    credentials_list = []

    def save_credentials(self):
        '''
        This method saves credential objects to the credential_list
        '''

        Credentials.credentials_list.append(self)

    def __init__ (self,app_name,app_username,app_password):
        self.app_name = app_name
        self.app_username = app_username
        self.app_password = app_password

