import requests
from bs4 import BeautifulSoup
import pandas as pd

names_ls = []
prices_ls = []
desc_ls = []
reviews_ls = []
for i in range(1, 11):
    url = "https://www.flipkart.com/search?q=mobiles+under+30000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_13_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_5_13_na_na_ps&as-pos=5&as-type=RECENT&suggestionId=mobiles+under+30000&requestId=4d622f0e-f5e1-4fff-bcd2-2df07904c0c0&as-searchtext=mobiles+under&page="
    flipkart = requests.get(url)
    print(flipkart)
    soup = BeautifulSoup(flipkart.text, 'lxml')
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
    # Names
    names = box.find_all('div', class_ = "_4rR01T")
    for i in names:
        names_ls.append(i.text)
    # print(names_ls)
    print(len(names_ls))

    # Prices
    prices = box.find_all('div', class_ = "_30jeq3 _1_WHN1")
    for i in prices:
        prices_ls.append(i.text)
    # print(prices_ls)
    print(len(prices_ls))


    # Desc
    desc = box.find_all('ul', class_ = "_1xgFaf")
    for i in desc:
        desc_ls.append(i.text)
    # print(desc_ls)
    print(len(desc_ls))


    # Reviews
    reviews = box.find_all('div', class_ = "_3LWZlK")
    for i in reviews:
        reviews_ls.append(i.text)
    # print(reviews_ls)
    print(len(reviews_ls))

df = pd.DataFrame({"Product_Name": names_ls, "Product_prices": prices_ls, "Product_desc": desc_ls, "Product_review": reviews_ls})
df.to_csv("flipkart.csv")





# Multiple Web Pages

# for i in range(2, 11):
#     url = "https://www.flipkart.com/search?q=mobiles+under+10000+rupees&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_14_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles+under+10000+rupees%7CMobiles&requestId=394e63c9-e79b-45db-973e-225627c81e69&as-backfill=on&page="+str(i)
#     flipkart = requests.get(url)
#     # print(flipkart)
#
#     soup = BeautifulSoup(flipkart.text, 'lxml')
#     np = soup.find("a", class_ = "_1LKTO3").get("href")
#     cnp = "https://www.flipkart.com" + np
#     print(cnp)
#
#     # url = cnp
#     # r = requests.get(url)
#     # soup = BeautifulSoup(r.text, 'lxml')
