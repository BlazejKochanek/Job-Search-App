from bs4 import BeautifulSoup
import requests

url = requests.get("https://www.olx.pl/praca/informatyka/programista/").text
soup = BeautifulSoup(url, "lxml")

offers = soup.find_all("td", class_ = "title-cell title-cell--jobs")

for offer in offers:
    offer_name = offer.find("strong").text
    print(offer_name)
