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

    def __init__ (self,aname,ausername,apassword):
        self.aname = aname
        self.ausername = ausername
        self.apassword = apassword

    @classmethod
    def find_credentials_using_appname(cls,app_name):
        '''
        The find credentials by appname method will return the credentials
        that match the appname for the user.

        The arguments include the appname to search for.
        
        It will return the credentials that match the appname for that user.

        '''

        for credentials in cls.credentials_list:
            if credentials.app_name == app_name:
                return credentials

    @classmethod
    def display_credentials(cls):
        '''
        This method will return the credential list
        '''

        return cls.credentials_list

