import time 
from selenium import webdriver
from seleniumbase import BaseCase
from selenium.webdriver.common.by import By

class ConTest(BaseCase):

  def test_pytest(self):
      #open page
  
  
    self.open("https://wwdev.csproject.org/")
    
    self.assert_title("Warewise")
  
#Locate the login button by ID 
    loginButton = self.driver.find_element("a[href='/login']")
    loginButton.click() 
      
#Locate sign up button by ID
    signUp = self.driver.find_element("button[type='submit'][form'=login-form']+ button")
    signUp.click()
    
       #Locate the input fields and submit button by ID 
    username_input= self.driver.find_element("input[placeholder=username]")
    
    password_input = self.driver.find_element("input[placeholder=confrim password]")
    
    email_input = self.driver.find_elemen