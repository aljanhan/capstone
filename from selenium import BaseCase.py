from selenium import BaseCase

class ConTest(BaseCase):
    def test_contact_page(self):
      #open page
      self.open("https://wwdev.csproject.org/")
      
      
      #Locate the login button by ID 
    loginButton = self.driver.find_element("a[href=/login]")
    loginButton.click()
    
    #Locate sign up button by ID
    signUp = self.driver.find_element("button[type=submit][from=login-form]+ button")
    signUp.click()
    
    
    #Locate the input fields and submit button by ID 
    usaname_input= self.driver.find_element("input[placeholder=username]")
    
    password_input = self.driver.find_element("input[placeholder=confrim password]")
    
    email_input = self.driver.find_element("input[placeholder=email]")

    phone_input = self.driver.find_element("input[placeholder=phone number]")
    
    
    #Enter valid data into the input fields
    
    username_input.send_keys("standard_user")
    time.sleep(2)
    
    password_input.send_keys("secert_sauce")
    time.sleep(2)
    
    confirm_input.send_keys("secret_sauce")
    time.sleep(2)
    
    email_input.send_keys("emailTestAl1@example.com")
    time.sleep(2)
    
    phone_input.send_keys("91123456789")
    time.sleep(2)
    
    #Click the submit button for sign up
    signUp = self.driver.find_elements("button[type=submit][form=login-form]+ button")
    signUp.click()
    
    
    # Enter login credentials and click login
    email_input = self.driver.find_element("input[placeholder=email]")
    password_input = self.driver.find_element("input[placeholder=password]")
    email_input.send_keys("emailTestAl1@example.com")
    time.sleep(2)
    password_input.send_keys("sauce")
    time.sleep(2)
    
    submit_button = self.driver.find_element("a[href=/login]")
    submit_button.click()
    