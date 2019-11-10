#!/usr/bin/env python3.6
from users import Users
from credentials import Credentials
import random

def create_user(username,firstname,lastname,birthmonth,password):
    '''
    function to create a new account
    '''
    new_users = Users(username,firstname,lastname,birthmonth,password)
    return new_users

def create_credentials(nameapp,usernameapp,passwordapp):
    '''
    Function to create new passwords for the application
    '''
    new_credentials = Credentials(nameapp,usernameapp,passwordapp)
    return new_credentials

def save_users(Users):
    '''
    Function saves a new user
    '''
    Users.save_users()
def save_credentials(Credentials):
    '''
    This function will save all instances of the credentials
    '''
    Credentials.save_credentials()



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

def allow_user(username,password):
    return Users.user_registered(username,password)

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
        # print("Please login with your credentials")

        # print("Enter Username")
        # userlogin = input()

        # print("Enter password")
        # passwordlogin = input()

        if username=='' or firstname=='' or lastname=='' or password=='':
            print("Please fill all the fields")
        else:
            save_users(create_user(username,firstname,lastname,birthmonth,password))
            print(f"{firstname}{lastname} Your account has been created,Your new user name is{username}")

            print("Now login with your credentials")
            print('/n')

            print("Enter your username")
            userlogin = input()
            print('/n')

            print("Enter your password")
            passwordlogin = input()
            

            if allow_user(userlogin,passwordlogin):
                print(f"{userlogin} welcome to password locker")


                while True:
                    print("""
                    Use the following codes to navigate:
                    cp - To create a password for a new application
                    vp - To view all your passwords
                    del _ TO delete a certain application and its passwords
                    """
                    )
                    shortcode = input().lower()
                    if shortcode == "cp":
                        print("Create password for a new app")

                        print("App name")
                        aname = input()

                        print("Your username in the app")
                        ausername = input()

                        print("Press gen - for the system to generate password or cr _ to create your own")
                        # random_number = random.randint(0,20)
                        choice = input().lower()
                        if choice == "gen":
                            print("Enter your lucky number")
                            lucky_number = str(input())
                            apassword = (f"{ausername}{lucky_number}")
                            print(f"Your password is {apassword}")

                        else:
                            print("Enter Your desired password")
                            apassword = input()

                        save_credentials(create_credentials(aname,ausername,apassword))
                        print(f"New password for {aname} has been created")

                    elif shortcode == "vp":
                        if display_credentials():
                            print("Here is a list of all your passwords")

                            for credentials in display_credentials():
                                print(f"{credentials.aname}{credentials.ausername}{credentials.apassword}")

                        else:
                            print("That password does not exist")

                else:
                    break

            else:
                print("Please login using the right credentials")


if __name__ == '__main__':
    main()


