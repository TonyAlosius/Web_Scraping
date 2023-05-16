import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

######################### Computer Laptop #################################
# url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
# r = requests.get(url)
# print(r.status_code)
# print(r.text)

# soup = BeautifulSoup(r.text, "lxml")
# tag = soup.header.div.a.button.span
# print(tag.string)


######################### Computer Tablet ###################################

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r = requests.get(url)
# print(r.status_code)

soup = BeautifulSoup(r.text, 'lxml')
# print(soup.find('h4', {"class": "pull-right price"}))

price = (soup.find('h4', {"class": "pull-right price"}))
# print(price.string)

desc = soup.find('p', {"class": "description"})
# print(desc.string)

desc1 = soup.find('p', class_ = "description")
# print(desc1)

prices = soup.findAll('h4', class_ = 'pull-right price')
# print(prices)

# for price in prices:
#     print(price.string)

desc3 = soup.find_all('p', class_ ="description")
# print(desc3[3])

RegEx = soup.find_all(string="Galaxy Tab")
# print(RegEx)

RegEx1 = soup.find_all(string= re.compile("Galaxy"))
# print(RegEx1)


RegEx1 = soup.find_all(string= re.compile("Idea"))
# print(RegEx1)

# amazon_url = "https://www.amazon.in/s?k=mobiles+under+30000&crid=HKA5CO1K9S1Y&sprefix=mobiles+under+30000%2Caps%2C872&ref=nb_sb_noss_1"
# amazon = requests.get(amazon_url)
# print(amazon.status_code)
# print(amazon.text)

# Web Scraping with Beautiful Soup and Pandas
tablets_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
tablets = requests.get(tablets_url)
soup = BeautifulSoup(tablets.text, 'lxml')
# print(tablets.status_code)

prod_name = soup.find_all("a", class_ = "title")
prod_name_ls = []
for i in prod_name:
    name = i.string
    prod_name_ls.append(name)
# print(prod_name_ls)
# print(prod_name.string)

#  Prices
prices = soup.find_all("h4", class_ = "pull-right price")
prices_ls = []
for i in prices:
    price = i.text
    prices_ls.append(price)
# print(prices_ls)

# Description
desc4 = soup.find_all('p', class_ = "description")
desc_ls = []
for desc in desc4:
    desc_items = desc.text
    desc_ls.append(desc_items)
# print(desc_ls)

# Reviews
reviews = soup.find_all('p', class_ = "pull-right")
review_ls = []
for review in reviews:
    review_items = review.text
    review_ls.append(review_items)
# print(review_ls)

df = pd.DataFrame({"Product Name": prod_name_ls, "Prices": prices_ls, "Description": desc_ls,"Reviews":review_ls})
# print(df)

# df.to_csv("e-commerce.csv")
# df.to_excel("e_commerce.xlsx")

# class="col-sm-4 col-lg-4 col-md-4"
boxes = soup.find_all("div", class_ ="col-sm-4 col-lg-4 col-md-4")
# print(len(boxes))

# class="col-sm-4 col-lg-4 col-md-4"
boxes = soup.find_all("div", class_ ="col-sm-4 col-lg-4 col-md-4")[2]
# print(boxes)

name = boxes.find("a").text
# print(name)


# Scraping the Table Content
t_url = "https://ticker.finology.in/"
ticker = requests.get(t_url)
# print(ticker.status_code)

soup = BeautifulSoup(ticker.text, 'lxml')
table = soup.find_all('table', class_ ="table table-sm table-hover screenertable")
# print(table)

headers = soup.find_all('th')
titles = []
for i in headers:
    title = i.text
    titles.append(title)
# print(titles)
df = pd.DataFrame(columns=titles)
# print(df)
rows = soup.find_all('tr')
# print(rows)

for i in rows[1:]:
    data = i.find_all('td')
    # print(data)
    row = [tr.text for tr in data]
    # print(row)
    # l = len(df)
    # df.loc[l] = row

