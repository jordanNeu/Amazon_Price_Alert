from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

SITE_URL = "https://www.amazon.com/AMD-Ryzen-7800X3D-16-Thread-Processor/dp/B0BTZB7F88/ref=sr_1_3?crid=291MR0A99B6C4&dib=eyJ2IjoiMSJ9.mU27cwptUy7PTxaJ31s2PTz6W9NS1RNDp9tVT82UIfTnecEpueYZZgmWfYbv-nRhM8NoaiyxbBORrnRZgD74jLYOTBQH9Pp90t2usYrjtR9tZL8Zd1cDonyL8vU5JMNuXP8bGjgP2nRBLLP5owmLd48aojhkXl48KvGJkwE-FGb_S-VUjm_cYTH1c3k6apIT7qjlX4n5Jx3e9ZdLJNFj2VYm9a_G4kfPDFZuZhQWDWk.4MMEp0XTBtEpU7HFsnbysWnC9rbYPafDYiLk_i5vHok&dib_tag=se&keywords=amd+cpu&qid=1714485403&sprefix=amd+cpu%2Caps%2C81&sr=8-3"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36', 'Accept-Language': 'en-US,en;q=0.9'}

MY_EMAIL = "jneumannpython@gmail.com"
MY_PASS = "zubwvjwrnasljhxi"

response = requests.get(SITE_URL, headers=HEADERS)
amazon_page = response.text
# print(amazon_page)
soup = BeautifulSoup(amazon_page, "lxml")

# print(soup)

price = soup.find(class_="a-offscreen").getText()
price_value = float(price.split("$")[1])
if price_value < 370:
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASS)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs="jneumann26@gmail.com",
        msg=f"Subject:Amazon Price Alert\n\nAMD Ryzen 7 7800X3D 8-Core, 16-Thread Desktop Processor is now {price}, by now at \n{SITE_URL}!"
    )


