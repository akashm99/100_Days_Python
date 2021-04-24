from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
url2 = "http://secure-retreat-92358.herokuapp.com/"
url3 = "https://orteil.dashnet.org/experiments/cookie/"
chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(url2)

#url1
# count = driver.find_element_by_css_selector("#articlecount a")
# print(count.text)
# count.click()

#url1
# all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

# search = driver.find_element_by_name("search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

# url2
fname = driver.find_element_by_name("fName")
fname.send_keys("Akash")

lname = driver.find_element_by_name("lName")
lname.send_keys("mali")

email = driver.find_element_by_name("email")
email.send_keys("Akash@gmail.com")

button = driver.find_element_by_class_name("btn-block")
button.click()



