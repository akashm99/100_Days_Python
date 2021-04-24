from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

ACCOUNT_ID = ""
ACCOUNT_PWD = ""
# url = "https://www.linkedin.com/jobs"
url = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"
chrome_driver_path = "D:\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)
driver.maximize_window()


sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element_by_id("username")
email_field.send_keys(ACCOUNT_ID)
password_field = driver.find_element_by_id("password")
password_field.send_keys(ACCOUNT_PWD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

# job_search = driver.find_element_by_id("jobs-search-box-keyword-id-ember454")
# job_search.send_keys("python developer")
job_cards = driver.find_elements_by_class_name("job-card-container--clickable")

for job in job_cards:
    time.sleep(1)
    try:
        job.click()
        time.sleep(3)
        job_save = driver.find_element_by_class_name("jobs-save-button")
        job_save.click()
    except NoSuchElementException:
        print("No application form found")
        continue
