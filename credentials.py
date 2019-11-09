class Credentials:
    '''
    This class will generate new instances of the credentials class
    '''
    credentials_list = []

    def __init__ (self,app_name,app_username,app_password):
        self.app_name = app_name
        self.app_username = app_username
        self.app_password = app_password

