import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select


class FacebookSignupButton():
    def testlog(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://en-gb.facebook.com/reg/")
        driver.find_element(By.NAME, "firstname").send_keys("name")
        time.sleep(0)
        driver.find_element(By.NAME, "lastname").send_keys("name")
        time.sleep(0)
        driver.find_element(By.NAME, "reg_email__").send_keys("demo@gmail.com")
        time.sleep(0)
        driver.find_element(By.NAME, "reg_email_confirmation__").send_keys("demo@gmail.com")
        time.sleep(0)
        driver.find_element(By.NAME, "reg_passwd__").send_keys("test123A@")
        time.sleep(0)
        # Drop down selection date starts
        select = driver.find_element(By.XPATH, "//select[@id='day']")
        drop = Select(select)
        drop.select_by_index(10)
        time.sleep(0)
        # Drop down closes date ends

        # Drop down selection month starts
        select = driver.find_element(By.XPATH, "//select[@id='month']")
        drop = Select(select)
        drop.select_by_index(5)
        time.sleep(0)
        # Drop down closes month ends

        # Drop down selection year starts
        select = driver.find_element(By.XPATH, "//select[@id='year']")
        drop = Select(select)
        drop.select_by_value("2000")
        time.sleep(0)
        # Drop down closes year ends
        driver.find_element(By.XPATH, "//span[2]").click()
        time.sleep(0)
        fbsignup = driver.find_element(By.NAME, "websubmit")
        # clicking on the button
        fbsignup.click()
        time.sleep(10)
        driver.close()


fbsignupbtn = FacebookSignupButton()
fbsignupbtn.testlog()


