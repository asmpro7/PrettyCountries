# Made by Ahmed ElSaeed
# 20/10/2023
# TG: @asmprotk

from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable

HTML = requests.get('https://www.scrapethissite.com/pages/simple/').text
soup = BeautifulSoup(HTML,'lxml')
Countries = soup.find_all('div', class_="col-md-4 country")
CountriesList = []
for index,country in enumerate(Countries):
    countryName = country.find('h3',class_='country-name').text.strip()
    countryCap = country.find('div',class_='country-info').find('span', class_='country-capital').text.strip()
    countryPop = country.find('div',class_='country-info').find('span', class_='country-population').text.strip()
    countryAr = country.find('div',class_='country-info').find('span', class_='country-area').text.strip()
    CountriesList.append([index+1,countryName,countryCap,countryPop,countryPop])
table = PrettyTable(field_names=['ID','Name','Capital','Population','Area'])
table.add_rows(CountriesList)
print(table)