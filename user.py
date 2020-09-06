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
    
  @classmethod
  def user_exists(cls,user_name):  
    for user in cls.user_list:
      if user.user_name ==user_name:
        return True
    
    
  