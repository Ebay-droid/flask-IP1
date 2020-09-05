#!/usr/bin/env python3.8
from user import User
from credentials import Credentials


def create_user(user_name, password):
    '''
    creating a new password locker account
    '''
    new_user = User(user_name,password)
    return new_user
  
def save_user(user):  
    '''
    save user
    '''
    user.save_user()
  
def create_credentials(account,user_id,pass_code):
    '''
    save user credentials
    '''  

    new_credentials =Credentials(account,user_id,pass_code)
    return new_credentials
  
def save_credentials(credentials):
    '''
    save credentials
    '''
    credentials.save_credentials()
    
def delete_credentials(credentials):
  '''
  to delete your credentials
  '''
  credentials.delete_credentials()    
  
def display_credentials():
  '''
  returns all saved credentials
  '''
  Credentials.display_credentials
  
def main():
  print ("Hello and welcome to Password Locker. ")
        
  
    
      
  
  
  