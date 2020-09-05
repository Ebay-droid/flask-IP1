class User:
  '''
  a class instantiating new users
  '''
  
  user_list = []
  
  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password
    
  def save_user(self):
    '''
    save user function to save users into the user_list
    '''
    User.user_list.append(self)
    
    
  