#!/usr/bin/env python3.6
from user import User
from credentials import Credentials

def create_user(username,firstname,lastname,birthmonth,password):
    '''
    function to create a new account
    '''
    new_user = User(username,firstname,lastname,birthmonth,password)
    return new_user

def save_user(user):
    '''
    Function saves a new user
    '''
    User.save_user()

def user_registered(password):
    '''
    This function will check if a given password exists in the user list
    '''
    return User.user_registered(password)

def main():
    print("Hello Welcome to to the ")



