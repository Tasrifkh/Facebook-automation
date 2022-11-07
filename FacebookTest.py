import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# class facebooklogin():
#     def testlog(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://www.facebook.com/")
#         time.sleep(5)
#         print(driver.title)
#         driver.close()
#
#
# fb = facebooklogin()
# fb.testlog()


class facebookloginkey():
    def testlog(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://www.facebook.com/")
        driver.find_element(By.ID, "email").send_keys("abc@abc.com")
        driver.find_element(By.ID, "pass").send_keys("123456")
        driver.find_element(By.NAME, "login").click()

        time.sleep(5)
        # print(driver.title)
        # driver.close()


fb = facebookloginkey()
fb.testlog()
