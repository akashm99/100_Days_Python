import time

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

EMAIL = ""
PASS = ""


class InternetTwitterBot:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.maximize_window()

    def get_internet_speed(self):
        url = 'https://www.speedtest.net/'
        self.driver.get(url)
        start_button = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_button.click()
        time.sleep(5)
        for i in range(10):
            time.sleep(2)
            try:
                down = self.driver.find_element_by_class_name('download-speed').text
                up = self.driver.find_element_by_class_name('upload-speed').text
                result = {
                    'download_speed': down,
                    'upload_speed': up
                }
                break

            except NoSuchElementException:
                continue

        return result

    def tweet_provider(self, tweet_message):
        url = 'https://twitter.com'
        # url = 'https://twitter.com/login?username_disabled=false&redirect_after_login=%2F'
        self.driver.get(url=url)

        # logging
        sleep(2)
        login_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div')
        login_button.click()

        sleep(2)
        username = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

        username.send_keys(EMAIL)
        password.send_keys(PASS)
        sleep(2)
        password.send_keys(Keys.ENTER)

        # posting
        sleep(5)
        tweet_input = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div')

        tweet_input.send_keys(tweet_message)

        sleep(3)
        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

