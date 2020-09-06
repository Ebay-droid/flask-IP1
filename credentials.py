class Credentials:
  '''
  class containing the user credentials
  '''
  
  credentials_list = []
  
  def __init__(self, account,user_id, passcode):
    
    self.account = account
    self.user_id = user_id
    self.passcode = passcode
    
  def save_credentials(self):
    Credentials.credentials_list.append(self)  
    
  def delete_credentials(self):
    Credentials.credentials_list.remove(self)  
    
  @classmethod
  def display_credentials(cls):
      '''
      retuns the credentials list
      '''
      return cls.credentials_list  
    
  @classmethod
  def find_by_account(cls,account):
    '''
    will take an account and return the credentiakls associated with it
    '''
    for credentials in cls.credentials_list:
      if credentials.account == account:
        return credentials
      
  
  