from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
import time

CHROME_PATH = "D:/chromedriver.exe"
USER_ID = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username = self.driver.find_element_by_name("username")
        username.send_keys("")
        password = self.driver.find_element_by_name("password")
        password.send_keys("")
        enter = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        enter.click()

    def find_followers(self):
        time.sleep(5)
        target_name = "amitabhbachchan"
        #self.driver.get(f"https://www.instagram.com/{target_name}")
        self.driver.get(f"https://www.instagram.com/{target_name}")
        time.sleep(3)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
        followers.click()

        time.sleep(2)
        # modal = self.driver.find_element_by_css_selector('.isgrP')
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


insta_bot = InstaFollower(CHROME_PATH)
insta_bot.login()
insta_bot.find_followers()