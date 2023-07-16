# We can't write something using Beautifulsoup
'''
Selenium
Automate browsers depending on the code
example-play web based games automatically, without any manual action
example- automatically do repetitive tasks like filling forms
'''
from selenium import webdriver
from selenium.webdriver.common.by import By

'''
# Different ways to find multiple elements 
find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")
'''
# chrome_driver_path = "C:/Users/detec/Dropbox/My PC (LAPTOP-9TATNMO3)/Downloads/chromedriver_win32/chromedriver.exe"

driver = webdriver.Chrome()
URL = "https://www.amazon.com/Ace-Data-Science-Interview-Questions/dp/0578973839/ref=sr_1_1_sspa?crid=2YVWHA7P3N5F7&keywords=DATA+SCIENCE&qid=1689429152&sprefix=data+sci%2Caps%2C531&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
# price_bar = driver.find_element(By.ID,"tmmSwatches")
# price = price_bar.text[9:24]
# print(price)
test_url = "https://www.python.org/"
driver.get(test_url)
# date =

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     print(time.text)

event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for event in event_names:
#     print(event.text)
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# driver.close() #closes the active tab
driver.quit() # quits the entire browser (more than  one window)

# Day 48
# Automatically fill in details on a website

from selenium import webdriver
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)

test_url = "http://secure-retreat-92358.herokuapp.com/"
driver.get(test_url)

# Search
first_name = driver.find_element(By.NAME,"fName")
first_name.send_keys("Riya")

last_name = driver.find_element(By.NAME,"lName")
last_name.send_keys("Chhikara")

email = driver.find_element(By.NAME,"email")
email.send_keys("youremail@gmail.com")
# email.send_keys(Keys.ENTER)

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()


from selenium.webdriver.common.keys import Keys
import time
# cookie_link = "https://orteil.dashnet.org/experiments/cookie/"
# driver.get(cookie_link)
# cookie = driver.find_element(By.ID, "cookie")
#
# # Get upgrade item ids.
# items = driver.find_elements(By.CSS_SELECTOR, "#store div")
# items_ids = [item.get_attribute("id") for item in items]
#
# timeout = time.time() + 5
# five_min = time.time() + 60*5
#
# while True:
#     cookie.click()
#
#     # Every 5 seconds:
#     if time.time() > timeout:
#         # Get all upgrade <b> tags
#         all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
#         item_prices = []
#
#         # Convert <b> text into an integer price.
#         for price in all_prices:
#             element_text = price.text
#             if element_text != "":
#                 cost = int(element_text.split("-")[1].strip().replace(",", ""))
#                 item_prices.append(cost)
#
#         # Create dictionary of store items and prices
#         cookie_upgrades = {}
#         for n in range(len(item_prices)):
#             cookie_upgrades[item_prices[n]] = item_ids[n]
#
#         # Get current cookie count
#         money_element = driver.find_element(By.ID, "money").text
#         if "," in money_element:
#             money_element = money_element.replace(",", "")
#         cookie_count = int(money_element)
#
#         # Find upgrades that we can currently afford
#         affordable_upgrades = {}
#         for cost, id in cookie_upgrades.items():
#             if cookie_count > cost:
#                 affordable_upgrades[cost] = id
#
#         # Purchase the most expensive affordable upgrade
#         highest_price_affordable_upgrade = max(affordable_upgrades)
#         print(highest_price_affordable_upgrade)
#         to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
#
#         driver.find_element(By.ID, "to_purchase_id").click()
#
#         # Add another 5 seconds until the next check
#         timeout = time.time() + 5
#
#         # After 5 minutes stop the bot and check the cookies per second count.
#     if time.time() > five_min:
#         cookie_per_s = driver.find_element(By.ID, "cps").text
#         print(cookie_per_s)
#         break

# wiki_url = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(wiki_url)
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# print(article_count.text)

# How to click on a link
# article_count.click()
# or
# content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()

# How to enter text in a search bar
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)



