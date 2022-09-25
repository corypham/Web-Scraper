from fileinput import filename
from ullib.request import urlopen
from bs4 import BeautifulSoup

url_to_scrape = "https://www.zillow.com/homes/92620_rb/"

request_page =  urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close

html_soup = BeautifulSoup(page_html, 'html.parser')

house_items = html_soup.find_all('li', class_="ListItem-c11n-8-69-2__sc-10e22w8-0 srp__hpnp3q-0 enEXBq with_constellation")

filename = 'zillow_data.csv'
f = open(filename, 'w')

headers = 'Address, Price \n'

f.write(headers)

for house in house_items:
  address = house.find('address', class_="property-card-addr").text
  price = house.find('span', class_="property-card-price").text

  f.write(address + ',' + price)