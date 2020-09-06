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
  
def find_account(account):
  '''
  find an account
  '''
  return Credentials.find_by_account(account)  
  
def main():
  print ("Hello and welcome to Password Locker. Please enter your name")
  user_name = input()
  
  print(f"Welcome {user_name},how do you wanna continue")
  print('\n')
  
  while True:
    print("Enter one of these short codes to go forward : ca - create an account, lg - to login, ex - to exit")
    
    short_code = input().lower
    
    if short_code == 'ca':
          print ("create username")
          created_username = input()
          
          print ("create password")
          created_password = input ()
          
          print ("confirm password")
          confirm_password = input()
          
          while created_password == confirm_password :
            
            save_user(create_user(created_username, created_password))
          else:
            print("ENter correct password")  
            
            print(f"Account for {created_username} successfully created. Proceed to Login")
            print('/n')
            print("Username")
            entered_username = input()
            print("Password")
            entered_password = input()
            
          while entered_username == created_username :
            print(f"Karibu {entered_username} to your account. Please select one of these short codes to go on cc - to create your credentials,  del  - to delete your credentials, dc - to display contacts, ex - to exit") 
            
            if  short_code == 'cc':
              print("Enter the account whose password you want to save")
              created_account =input()
              
              print("ENter account User_id")
              account_user_id = input ()
              
              print("enter account password")
              account_passcode = input()
              
              save_credentials(create_credentials(created_account,account_user_id, account_passcode))
              
            elif short_code == 'del':
              print ("Enter account of credential to delete")
              search_account = input()
              if find_account(search_account):
                delete_credentials(search_account)
                print (f"credentials deleted")
                
              else:
                print(f"Enter valid account name")  
            
    elif short_code == 'lg':
            print("Enter your Username and password below")
            print("Username")
            entered_username = input()
            print("Password")
            entered_password = input()
            
    while entered_username == created_username:
            print(f"Karibu {entered_username} to your account. Please select one of these short codes to go on cc - to create your credentials,  del  - to delete your credentials, dc - to display contacts, ex - to exit") 
            
            if  short_code == 'cc':
              print("Enter the account whose password you want to save")
              created_account =input()
              
              print("ENter account User_id")
              account_user_id = input ()
              
              print("enter account password")
              account_passcode = input()
              
              save_credentials(create_credentials(created_account,account_user_id, account_passcode))
              
            elif short_code == 'del':
              print ("Enter account of credential to delete")
              search_account = input()
              if find_account(search_account):
                delete_credentials(search_account)
                print (f"credentials deleted")
                
              else:
                print(f"Enter valid account name")  
                
            elif short_code  == 'ex':
              print("See you next time")
              break  
          
    else  :
            print ("Please use valid short_code")   
            
            
if __name__ == '__main__':
  
    main()            
            
             
                 

                
            
            
            
         
  
    
      
  
  
  