import requests
import html5lib
import csv
from bs4 import BeautifulSoup
import unicodedata

urls = ['https://www.yellowpages.com/search?search_terms=dentists&geo_location_terms=New+York%2C+NY',
        'https://www.yellowpages.com/search?search_terms=dentists&geo_location_terms=New%20York%2C%20NY&page=2'
        ]

with open('dentist.csv', 'wb') as csvfile:
    fieldnames = ['url', 'title', 'name', 'phone number', 'rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for url in urls:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html5lib")

        name = soup.find(attrs={'class': 'search-results organic'}).findAll(attrs={'itemprop': 'name'})
        rating = soup.find(attrs={'class': 'search-results organic'}).findAll(attrs={'class': 'count'})
        phone = soup.find(attrs={'class': 'search-results organic'}).findAll(attrs={'class': 'phones phone primary'})

        for index, doctor in enumerate(name):
            name = unicodedata.normalize('NFKD', doctor.text).encode('ascii', 'ignore')
            try:
                count = rating[index].text
            except IndexError:
                count = 0
            writer.writerow({'url': url,
                             'title': soup.title.text,
                             'name': name if name else "None",
                             'phone number': phone[index].text if phone[index] else "None",
                             'rating': count,
                             })
            print [
                name if name else "None",
                phone[index].text if phone[index] else "None"
            ]
