from bs4 import BeautifulSoup
import requests

def offer_links(offers):
    for offer in offers:
        link_offer = offer.table.tr.td.div.h3.a.get("href")
        offer_list.append(link_offer)
    return offer_list


def next_page(soup):
    try:
        page = requests.get(
            soup.find("span", class_="fbold next abs large").a.get(
                "href")).text
        return page
    except AttributeError:
        return False

def offer_details(offer_link):
    pass

offer_list = []
url = requests.get("https://www.olx.pl/praca/informatyka/programista/").text

while url:
    soup = BeautifulSoup(url, "lxml")
    offers = soup.find_all("div", class_="offer-wrapper")
    offer_links(offers)
    url = next_page(soup)

for offer_link in offer_list:
    print(offer_link)



print(len(offer_list))
