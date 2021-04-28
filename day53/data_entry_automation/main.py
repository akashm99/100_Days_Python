from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time

form_url = ""
zillow_url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.613324359755836%2C%22north%22%3A37.936904488209905%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

headers = {
"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
"Accept-Language" : "en-US" #,en;q=0.9
}

response = requests.get(zillow_url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
#links = soup.find_all('a', class_="list-card-link", href=True)
all_link_elements = soup.select(".list-card-top a")
links = []
for link in all_link_elements:
    href = link["href"]
    print(href)
    if "http" not in href:
        links.append(f"https://www.zillow.com{href}")
    else:
        links.append(href)
# address = soup.find_all(class_="list-card-addr")
all_address_elements = soup.select(".list-card-info address")
address = [address.get_text().split(" | ")[-1] for address in all_address_elements]
all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)

prices = all_prices
#prices = [price.split("+")[0] for price in all_prices if "$" in price.text]

# prices = soup.find_all(class_="list-card-price")
# prices = [price.getText() for price in prices]
#links = [link.getText() for link in links if link]
#links = [link for link in links if link != '']
# address = [add.getText() for add in address]

driver = webdriver.Chrome("D:/chromedriver.exe")
driver.get(form_url)
time.sleep(2)

for i in range(len(address)):
    addr = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    addr.send_keys(address[i])
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price.send_keys(prices[i])
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link.send_keys(links[i])
    submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit.click()
    time.sleep(2)
    nextr = driver.find_element_by_link_text("Submit another response")
    nextr.click()

driver.close()

