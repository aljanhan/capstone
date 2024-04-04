from typing import Self
from selenium import webdriver
import time

# driver = webdriver.Firefox(executable_path="C:\\Grid\\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\\Grid\\IEdriverserver.exe")
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(30)
driver.set_page_load_timeout(50)
driver.get("https://wwdev.csproject.org")
assert "Warewise" in driver.title
driver.find_element(By.LINK_TEXT, "LOGIN").click()

from seleniumbase import BaseCase\
class HomeTest(BaseCase):
    def test_home_page(self):

# open home page  

self.open("https://wwdev.csproject.org")
        
# assert page title

self.assert_tittle("Warwise")




# assert logo

self .assert_element ("")









driver.save_screenshot("")
time.sleep(3)
driver.quit()  


