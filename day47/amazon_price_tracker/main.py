import requests
from bs4 import BeautifulSoup

product_url = "https://www.amazon.in/Butterfly-Premium-Vegetable-Chopper-Blue/dp/B085F2HVF9?ref_=Oct_s9_apbd_orecs_hd_bw_b1VPSVT&pf_rd_r=CYGT4AVZSYRZ85GEGTKR&pf_rd_p=b115a9ca-3384-5972-932c-d0e7553ac98b&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=1380267031"
set_price = 300.0
# user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36"
# accept_language = "en-US,en;q=0.9"

response = requests.get(product_url, headers={"User-Agent": "Defined"})
soup = BeautifulSoup(response.text, "html.parser")

deal_price = soup.find("span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText()
price = float(deal_price.split("₹ ")[1])

if price <= set_price:
    import smtplib
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user="", password="")
        connection.sendmail(from_addr="", to_addrs="",
                            msg="Subject: Low Price Alert\n\n"
                                f"price: ₹ {price}"
                                f"link: {product_url}")