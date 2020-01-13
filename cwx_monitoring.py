import unittest
import glob, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import random
import string
from datetime import datetime
import sys
import HtmlTestRunner

user=("cwx_monitoring") # change user
userId=(user+"@yopmail.com")
Env=("https://cwxtest-apptinuum.choiceworx.io/")

class ApptinuumTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-notifications")
        preferences = {"download.default_directory": "C:\Users\canum\PycharmProjects\python","safebrowsing.enabled": "false"}  # Change the path
        options.add_experimental_option("prefs", preferences)
        cls.driver = webdriver.Chrome(executable_path="C:\DRIVERS\chromedriver_win32\chromedriver.exe",chrome_options=options)  # Change the path
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_1_AddUser(self):
        self.driver.get(Env)
        self.driver.implicitly_wait(10)
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@type='email']").send_keys(userId)
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        print ("User added for registration process: "+userId)

    def test_2_UserRegistration(self):
        self.driver.get("http://www.yopmail.com/en/")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name='login']").send_keys(userId)
        time.sleep(3)
        self.driver.find_element_by_xpath('html/body/center/div/div/div[3]/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td/div[1]/form/table/tbody/tr[1]/td[3]/input').click()
        self.driver.get('http://www.yopmail.com/en/inbox.php?login='+user+'&p=1&d=&ctrl=&scrl=&spam=true&yf=005&yp=RZwZ5AQLmAmNkAmZ3AGVjBQL&yj=YAQH3BGH4AGt1Zwp3BQR3AQN&v=2.9&r_c=&id=')
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Apptinuum Signup')]").click()
        time.sleep(7)
        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(3)
        links = self.driver.find_elements(By.TAG_NAME, "a")
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Sign Up").click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[2])
        time.sleep(3)
        user_pwd = self.driver.find_element_by_xpath("//input[@placeholder='Password']")
        user_pwd.send_keys("Test@1234")
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)
        company = self.driver.find_element_by_xpath("//input[@placeholder='Company']")

        def randomString(stringLength=3):
            letters = string.ascii_uppercase
            return ''.join(random.choice(letters) for i in range(stringLength))

        company.send_keys(randomString()+' Pvt. '+'Ltd.')
        time.sleep(10)
        self.driver.find_element_by_xpath("//input[@placeholder='Industry']").send_keys("IT")
        time.sleep(2)
        self.driver.find_element_by_xpath("//select[@id='number-of-employees']/option[text()='0-100']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(5)
        self.driver.find_element_by_id("firstName").send_keys(user)
        time.sleep(2)
        self.driver.find_element_by_id("lastName").send_keys("Admin")
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@placeholder='Job']").send_keys("CEO")
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("//label[contains(text(),'Tom')]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='btn invite-them-later']").click()
        time.sleep(5)
        self.driver.find_element_by_id("userEmail").send_keys(userId)
        time.sleep(3)
        self.driver.find_element_by_id("password").send_keys("Test@1234")
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='btn waves-effect waves-light login-submit-button']").click()
        time.sleep(7)
        self.driver.find_element_by_xpath("/html/body/app-root/login/div/eula-modal/div/div/div[2]/label").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[@class='continue']").click()
        time.sleep(7)
        self.driver.find_element_by_xpath("//div[contains(text(),'Add Device')]").click()
        self.driver.find_element_by_xpath("//select[@name='deviceType']/option[text()='Desktop']").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//select[@name='deviceManufacturer']/option[text()='Lenovo']").click()
        time.sleep(3)
        device_ele = self.driver.find_element_by_xpath("//input[@name='friendlyName']")
        device_ele.send_keys("admin")
        time.sleep(10)
        self.driver.find_element_by_xpath("/html/body/app-root/dashboard/main/devices/div/manager-devices/div[4]/div/add-component/div/div/div/div[3]/add-device/div/form/div[2]/button").click()
        time.sleep(7)
        print ("User Registration - Working fine for " + userId+"\n")
        print(" Device added successfuly"+"\n")
        time.sleep(3)

    def test_3_BotDownload(self):
        self.driver.get('http://www.yopmail.com/en/inbox.php?login='+ user+'&p=1&d=&ctrl=&scrl=&spam=true&yf=005&yp=OZmxjBQH4AQRmAQZkAmxjZmt&yj=MZGN0ZQR0AGx0ZwRlBQN5ZwN&v=2.9&r_c=&id=')
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.driver.find_element_by_xpath("//span[contains(text(),'Apptinuum - Agent Download')]").click()
        time.sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[3])
        self.driver.find_element_by_xpath("//a[contains(text(),'Download')]").click()
        time.sleep(10)
        self.driver.switch_to.window(self.driver.window_handles[4])
        self.driver.find_element_by_xpath("//button[contains(text(),'Download')]").click()
        time.sleep(50)
        print("Bot download - Successful (in local machine)"+"\n")
        time.sleep(21)

    def test_4_BotInstallation(self):
        s = os.system("cd C:\Users\canum\PycharmProjects\python & ls Support*.exe >url.txt")  # change the path
        f = open("C:\Users\canum\PycharmProjects\python\url.txt", "r")  # change the path
        time.sleep(5)
        g = f.read()
        h = (g[0:47])
        os.system(h + ' /install /quiet /passive')
        time.sleep(17)
        print('Bot installation - successful')
        self.driver.find_element_by_xpath("//button[contains(text(),'Login')]").click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.driver.refresh()

    def test_5_DeviceSync(self):
        self.driver.get(Env)
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()
        time.sleep(5)
        t = str(datetime.date(datetime.now()))
        sync_ele = self.driver.find_element_by_xpath("//a[contains(text(),'Last powered state')]")
        if sync_ele.is_displayed():
            print("Device sync Successful - Last powered state: " + t)
        time.sleep(3)

    def test_6_Remediation(self):
        self.driver.get(Env)
        time.sleep(3)
        self.driver.find_element_by_xpath("//button[contains(text(),'Log In')]").click()
        self.driver.find_element_by_xpath("/html/body/app-root/dashboard/main/div/input").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//button[contains(text(),'admin')]").click()
        time.sleep(10)
        self.driver.find_element_by_xpath("/html/body/app-root/dashboard/main/div/ul/li/component-chat/div/div[2]/div/div[7]/div/div[2]/div/button[1]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/app-root/dashboard/main/div/ul/li/component-chat/div/div[2]/div/div[9]/div/div[2]/div/button[1]").click()
        time.sleep(10)
        time.sleep(50)
        s_ele = self.driver.find_element_by_xpath("//div[contains(text(),'successfully')]")
        if s_ele.is_displayed():
            print("Remediation - Working fine checked with My printers remediation")
            self.driver.save_screenshot("./screenshot/remediation.png")

if __name__== '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/canum/PycharmProjects/python/Report'))