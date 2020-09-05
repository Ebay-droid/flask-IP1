#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(user_name, password):
    '''
    creating a new password locker account
    '''
    new_user = User(user_name,password)
    return new_user
  
def create_credentials(account,user_id,pass_code):
    