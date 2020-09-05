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
  
  