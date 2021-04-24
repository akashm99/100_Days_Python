from selenium import webdriver
from selenium.webdriver.common.keys import Keys
url = "https://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(url)

cookie = driver.find_element_by_id("cookie")
ids = [i.get_attribute('id') for i in driver.find_elements_by_css_selector("#store div")]
ids = ids[0:-1]

#store = driver.find_elements_by_css_selector("#store .grayed b")
# price = []
ids_money = {}

def purchase():
    price = []
    store = driver.find_elements_by_css_selector("#store .grayed b")

    for i in range(len(store[0:-1])):
        price.append(int(store[i].text.split("- ")[1].replace(",", "")))
        ids_money[ids[i]] = price[i]

    money = driver.find_element_by_id("money")
    money = int(money.text.replace(",", ""))

    for purchase in ids[-1:0:-1]:
        if money >= ids_money[purchase]:
            pur = driver.find_element_by_id(purchase)
            pur.click()

while True:
    cookie.click()
    purchase()