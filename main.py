from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
import random

url = "https://www.webscraper.io/test-sites/e-commerce/allinone"
source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
details = {"title": [], "price": [], "desc": []}
for product in soup.find_all('div',class_='product-wrapper'):

    name = product.find('a',class_="title").text
    #print(name.text)
    price = product.find('h4',class_="price").text
    # print(price)
    desc = product.find('p', class_="description").text
    # print(desc)
    product_data= f'=== PRODUCT DATA OF {name} === \n Title of product: {name} \n Price: {price} \n Description : {desc} '
    print(product_data)
    details["title"].append(name)
    details['desc'].append(desc)
    details['price'].append(price)
for key, value in details.items():
        print((details[key]),key)
len(details)
data = pd.DataFrame(details)
data.to_csv('product.csv')