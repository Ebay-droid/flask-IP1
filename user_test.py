import unittest
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class defines test cases for the contact class behaviours
  '''
  
  def setUp(self):
    '''
    this method will run before every test case
    '''
    self.new_user = User("Ebay", "3214")
    
    
  def test_init(self): 
    '''
    this to test if the object is initialized properly
    '''
    
    self.assertEqual(self.new_user.user_name, "Ebay") 
    self.assertEqual(self.new_user.password,"3214" ) 
    
  def test_save_user(self):
    '''
    test if user object can be saved on the user_list
    '''
    
    self.new_user.save_user()
    self.assertEqual(len(User.user_list),1)
    
     
    
if __name__ == "__main__":
    unittest.main()  