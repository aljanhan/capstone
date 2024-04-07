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
    signUp = self.driver.find_element("button[type='submit'][form='login-form'] + button")
    signUp.click()
    
       #Locate the input fields and submit button by ID 
    username_input= self.driver.find_element("input[placeholder='username']")
    
    password_input= self.driver.find_element("input[placeholder='password']")
   
    confirm_password_input = self.driver.find_element("input[placeholder='confirm password']")
    
    email_input = self.driver.find_element("input[placeholder='email']") 
    
    
    phonenumber_input = self.driver.find_element("input[placeholder='phone number']")
    
    #Enter valid data into the input fields
    
    username_input.send_keys("drip")
    time.sleep(1)
    
    password_input.send_keys("bloomfield")
    time.sleep(1)
    
    confirm_password_input.send_keys("bloomfield")
    time.sleep(1)
    
    email_input.send_keys("aljanhan_smith@bloomfield.edu")
    time.sleep(1)
    
    phonenumber_input.send_keys("9735177946")
    time.sleep(1)
    
    #Click the button to sign up
    
    signUp = self.driver.find_element("button[type='submit'][form='signup-form'] + button")
    signUp.click()
    time.sleep(2)
    
    #Enter login crendentals and click login
    
    email_input =self.driver.find_element("input[placeholder='email']")
    
    password_input =self.driver.find_element("input[placeholder='password']")
    
    email_input.send_keys("aljanhan_smith@bloomfield.edu")
    time.sleep(2)
    
    password_input.send_keys("bloomfield")
    time.sleep(2) 
    
    #click login
    
    login_button = self.driver.find_element("a[href='/login']")
    login_button.click()
    time.sleep(2)
    self.open("https://wwdev.csproject.org/")
    time.sleep(3)