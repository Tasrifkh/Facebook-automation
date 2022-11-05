import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class DemoFindElementById():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID, "login-input").send_keys('test@test.com')
        time.sleep(5)
findbyid = DemoFindElementById()
findbyid.locate_by_id_demo()

# class DemoFindElementByName():
#     def locate_by_Name_demo(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
#         driver.find_element(By.NAME, "login-input").send_keys('test@test.com')
#         time.sleep(5)
# findbyid = DemoFindElementByName()
# findbyid.locate_by_Name_demo()

# class DemoFindElementByXpath():
#     def locate_by_Xpath_demo(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
#         driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys('test@test.com')
#         time.sleep(5)
# findbyid = DemoFindElementByXpath()
# findbyid.locate_by_Xpath_demo()


# class DemoFindElementByCssSelector():
#     def locate_by_CssSelector_demo(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
#         driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys('test@test.com')
#         time.sleep(5)
# findbyid = DemoFindElementByCssSelector()
# findbyid.locate_by_CssSelector_demo()

# class DemoFindElementByCssSelector():
#     def locate_by_CssSelector_demo(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://www.yatra.com/")
#         driver.find_element(By.LINK_TEXT, "Yatra for Business").click()
#         time.sleep(5)
# findbyid = DemoFindElementByCssSelector()
# findbyid.locate_by_CssSelector_demo()

# class DemoFindElementByCssSelector():
#     def locate_by_CssSelector_demo(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://www.yatra.com/")
#         driver.find_element(By.PARTIAL_LINK_TEXT, "Holida").click()
#         time.sleep(5)
# findbyid = DemoFindElementByCssSelector()
# findbyid.locate_by_CssSelector_demo()

# input tag

# class DemoFindElementByCssSelector():
#     def locate_by_CssSelector_demo(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
#         # driver.find_element(By.TAG_NAME, "input").send_keys("abc@tasrif.com")
#         driver.find_element(By.CLASS_NAME, "email-login-box").send_keys("abc@tasrif.com")
#         time.sleep(5)
# findbyid = DemoFindElementByCssSelector()
# findbyid.locate_by_CssSelector_demo()

# Find Elements List

# class DemoFindElementByCssSelector():
#     def locate_by_CssSelector_demo(self):
#         driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#         driver.get("https://www.yatra.com/")
#         lista = driver.find_elements(By.TAG_NAME, 'a')
#         print(len(lista))
#         for i in lista:
#             print(i.text)
#         time.sleep(5)
# findbyid = DemoFindElementByCssSelector()
# findbyid.locate_by_CssSelector_demo()