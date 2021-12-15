from bs4 import BeautifulSoup
import requests
import pandas as pd


def offer_links(offers):
    for offer in offers:
        link_offer = offer.table.tr.td.div.h3.a.get("href")
        offer_links_list.append(link_offer)
    return offer_links_list


def next_page(soup):
    try:
        page = requests.get(
            soup.find("span", class_="fbold next abs large").a.get(
                "href")).text
        return page
    except AttributeError:
        return False


def take_offer_details(offer_link):
    url = requests.get(str(offer_link)).text
    soup = BeautifulSoup(url, "lxml")
    offer_name = soup.find("h1", class_="css-r9zjja-Text eu5v0x0").text
    add_date = soup.find("span", class_="css-19yf5ek").text
    offer_id = soup.find("span", class_="css-9xy3gn-Text eu5v0x0").text
    offer_text = soup.find("div", class_="css-1shxysy").text

    if "python" in offer_text.lower():
        offer_details = {
            "python": True,
            "offer_id": offer_id,
            "offer_name": offer_name,
            "add_date": add_date,
            "offer_link": offer_link,
        }
        return offer_details
    else:
        offer_details = {
            "python": False,
            "offer_id": offer_id,
            "offer_name": offer_name,
            "add_date": add_date,
            "offer_link": offer_link,
        }
        return offer_details


offer_links_list = []
offers_list = []
url = requests.get("https://www.olx.pl/praca/informatyka/programista/").text

while url:
    soup = BeautifulSoup(url, "lxml")
    offers = soup.find_all("div", class_="offer-wrapper")
    offer_links(offers)
    url = next_page(soup)

print("Download all links")

for offer_link in offer_links_list:
    offer_details = take_offer_details(offer_link)
    offers_list.append(offer_details)
    print(f"Pobrano dane: {offer_link}")

print(offers_list)
df = pd.DataFrame(offers_list)
print(df)
df.to_excel("output.xlsx")
