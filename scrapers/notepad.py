from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get('https://www.jobs.pl/oferty/it-rozwoj-oprogramowania').text
soup = BeautifulSoup(url, 'lxml')

# Liczba ofert z danej kategorii
number_of_offerts = soup.h2.b.text
offers_links = []
offers_list = []
page = 1

# Pętla dział dopóki liczba pobranych ofert jest mniejsza niż liczba wszystkich ofert
while len(offers_links) < int(number_of_offerts):
    soup = BeautifulSoup(url, 'lxml')
    offers = soup.find_all('div', class_='offer-details')
    # Pobieranie linków i danych wszystkich ofert z danej strony
    for i in offers:
        offer_id = i.a['href']
        offer_link = f'https://www.jobs.pl/{offer_id}'
        # Wejście w daną ofertę
        url = requests.get(offer_link).text
        soup = BeautifulSoup(url, 'lxml')
        offer_name = soup.find('p', class_ = 'offer-view-title-value').text
        company_name = soup.find('p', class_ = 'offer-view-company').text
        city = soup.find('p', class_ = 'offer-view-location').text
        required_experience = soup.find('p', class_ = 'offer-view-label-value').text
        offer_details = {
            'Nazwa oferty' : offer_name,
            'Nazwa firmy' : company_name,
            'Miasto' : city,
            'Wymagane doświadczenie' : required_experience
        }
        print(offer_link)
        offers_list.append(offer_details)
        offers_links.append(str(offer_link))
        print(offers_list)
    page += 1
    url = requests.get(f'https://www.jobs.pl/oferty/it-rozwoj-oprogramowania/p-{page}').text


print(100 * '*')
print(len(offers_links))
print(len(offers_list))
print(number_of_offerts )
df = pd.DataFrame(offers_list)
print(df)