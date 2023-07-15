# Day 47
# Amazon Price Tracker 

EMAIL = "YOUR EMAIL_ID"
SMTP_ADDRESS = "smtp.gmail.com"
PASSWORD = "xxx"


from smtplib import SMTP
from bs4 import BeautifulSoup
import requests
import lxml

URL = "https://www.amazon.com/Ace-Data-Science-Interview-Questions/dp/0578973839/ref=sr_1_1_sspa?crid=2YVWHA7P3N5F7&" \
      "keywords=DATA+SCIENCE&qid=1689429152&sprefix=data+sci%2Caps%2C531&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.content, parser="lxml", features="lxml")
price = soup.find(class_="a-size-base a-color-price a-color-price").get_text()
price_without_currency = price.split("$")[1][:-2]
print(price_without_currency)
price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 30

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result= connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
