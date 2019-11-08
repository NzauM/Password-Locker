#!/usr/bin/env python3.6
from users import Users
# from credentials import Credentials

def create_user(username,firstname,lastname,birthmonth,password):
    '''
    function to create a new account
    '''
    new_users = Users(username,firstname,lastname,birthmonth,password)
    return new_users

def save_users(Users):
    '''
    Function saves a new user
    '''
    Users.save_users()

def user_registered(password):
    '''
    This function will check if a given password exists in the user list
    '''
    return Users.user_registered(password)

def find_user_byPassword(password):
    '''
    This function will get a user's details using the password
    '''
    return Users.find_user_byPassword(password)

def main():
    print("Hello Welcome to to the password locker.What is your name??")
    name = input()
    print(f"Welcome{name} you will need to create an account first")
    print("/n")

    while True:
        print("Create your account")
        print("/n")
        print("Enter a username of your choice")
        username = input()

        print("First Name ...")
        firstname = input()

        print("Last Name ...")
        lastname = input()

        print("BirthMonth....")
        birthmonth = input()

        print("YOur desired password...")
        password = input()

        save_users(create_user(username,firstname,lastname,birthmonth,password))
        print("/n")

        print(f"{firstname}{lastname} ,Your new account has been created")
        print("/n")
        print("Please login with your credentials")

        print("Enter Username")
        username = input()

        print("Enter password")
        password = input()

        if Users.find_user_byPassword(password).password == password:
            print("Welcome .Press dp-to display passwords,cp-to create a new password, and del to delete a password")
        elif Users.find_user_byPassword(password).password != password:
            print("Wrong credetials")

if __name__ == '__main__':
    main()


