import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    #testing1
    def test_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1) 
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

         # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)

    #testing2
    def test_view_product(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1) 
        driver.find_element(By.ID, "login-button").click() # login button
        time.sleep(1)
        driver.find_element(By.ID, "item_4_title_link").click() #click view product
        time.sleep(1)

         # validasi
        response_data = driver.find_element(By.CLASS_NAME,"inventory_details_price").text
        self.assertIn('29.99', response_data)

        #testing3
    def test_success_logout(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        time.sleep(3)
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        time.sleep(1)
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        time.sleep(1) 
        driver.find_element(By.ID, "login-button").click() # login button
        time.sleep(1)
        driver.find_element(By.ID, "react-burger-menu-btn").click() # clik button menu
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click() # clik logout
        time.sleep(1)

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"login_credentials").text
        self.assertIn('Accepted usernames are', response_data)


def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()