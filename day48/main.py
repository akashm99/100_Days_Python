from selenium import webdriver
product_url = "https://www.amazon.in/Butterfly-Premium-Vegetable-Chopper-Blue/dp/B085F2HVF9?ref_=Oct_s9_apbd_orecs_hd_bw_b1VPSVT&pf_rd_r=CYGT4AVZSYRZ85GEGTKR&pf_rd_p=b115a9ca-3384-5972-932c-d0e7553ac98b&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1380267031"
search_url = "https://www.python.org/"
chrome_driver_path = "D:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get(product_url)
# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

driver.get(search_url)
#search = driver.find_element_by_name("q")
# print(search.get_attribute("placeholder"))
time = driver.find_elements_by_css_selector(".event-widget time")
links = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(time)):
    events[n] = {
        "time": time[n].text,
        "event": links[n].text
    }

#driver.close()
print(events)