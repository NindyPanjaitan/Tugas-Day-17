import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

class TestLoginDekorumah(unittest.TestCase):
    
    def setUp(self): 
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    def test_a_login_failed(self): 
        driver = self.driver
        driver.get("https://www.dekoruma.com") #open Website
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH,"//*[@id='content']/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]").click() #click Login Button
        time.sleep(2)
        login_panel = driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[1]") #Validation login panel
        self.assertAlmostEqual(login_panel.text, "Masuk")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/input").send_keys("panjaitannindy@gmail.com")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[4]/div").click() #click masuk button
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[3]/div[2]/input").send_keys("Panjaitannindy!")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[5]/div").click() #click masuk button
        time.sleep(5)


    def test_b_login_failed(self): 
        driver = self.driver
        driver.get("https://www.dekoruma.com") #open Website
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH,"//*[@id='content']/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]").click() #click Login Button
        time.sleep(2)
        login_panel = driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[1]") #Validation login panel
        self.assertAlmostEqual(login_panel.text, "Masuk")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/input").send_keys("panjaitannindy@gmail.com")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[4]/div").click() #click masuk button
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[3]/div[2]/input").send_keys("Panjaitannindy709090!")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[5]/div").click() #click masuk button
        time.sleep(5)
        message_Login_Fail = driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div[2]/div/div[2]/div[2]") #validation error message
        self.assertAlmostEqual(message_Login_Fail.text, "{'non_field_errors': [ErrorDetail(string='Email atau Password yang Anda masukkan salah', code='invalid')]}")
        time.sleep(2)
        
    def test_b_login_failed(self): 
        driver = self.driver
        driver.get("https://www.dekoruma.com") #open Website
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(By.XPATH,"//*[@id='content']/div/div/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]").click() #click Login Button
        time.sleep(2)
        login_panel = driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[1]") #Validation login panel
        self.assertAlmostEqual(login_panel.text, "Masuk")
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[6]/span").click() #daftar
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div[2]/div[2]/input").send_keys("sudarnowong@gmail.com")
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div/div/div[4]/div").click() #click daftar button
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[3]/div[2]/input").send_keys("sudarno") #input nama 
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[4]/div[2]/input").send_keys("Semangat12345") #input password
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[5]/div[2]/input").send_keys("Semangat12345") #input confirm password
        time.sleep(2)
        driver.find_element(By.XPATH,"//*[@id='content']/div/div[1]/span/span/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[7]/div").click() #click daftar button
        time.sleep(2)
        
        
    def tearDown(self): 
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()            