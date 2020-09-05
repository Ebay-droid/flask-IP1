class Credentials:
  '''
  class containing the user credentials
  '''
  
  credentials_list = []
  
  def __init__(self, account,user_id, passcode):
    
    self.account = account
    self.user_id = user_id
    self.passcode = passcode
  
  