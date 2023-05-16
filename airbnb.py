import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.airbnb.co.in/s/Delhi--India/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-06-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=1&channel=EXPLORE&search_type=autocomplete_click&date_picker_type=flexible_dates&checkin=2023-05-19&checkout=2023-05-20&source=structured_search_input_header&query=Delhi%2C%20India&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&adults=1"
airbnb = requests.get(url)
soup = BeautifulSoup(airbnb.text, 'lxml')


np = soup.find('a', class_ = "l1j9v1wn c1ytbx3a dir dir-ltr").get("href")
cnp = "https://www.airbnb.co.in" + np
print(cnp)

url = cnp
r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')


names_ls = []
prices_ls = []
desc_ls = []
reviews_ls = []
for i in range(1, 11):
    url = "https://www.airbnb.co.in/s/Delhi--India/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-06-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=1&channel=EXPLORE&search_type=autocomplete_click&date_picker_type=flexible_dates&checkin=2023-05-19&checkout=2023-05-20&source=structured_search_input_header&query=Delhi%2C%20India&place_id=ChIJLbZ-NFv9DDkRzk0gTkm3wlI&adults=1"
    airbnb = requests.get(url)
    soup = BeautifulSoup(airbnb.text, 'lxml')

    # Names
    names = soup.find_all('div', class_ = "t1jojoys dir dir-ltr")
    for i in names:
        names_ls.append(i.text)
    # print(names_ls)
    print(len(names_ls))

    # Prices
    prices = soup.find_all('span', class_ = "_1y74zjx")
    for i in prices:
        prices_ls.append(i.text)
    # print(prices_ls)
    print(len(prices_ls))


    # # Desc
    # desc = soup.find_all('ul', class_ = " dir dir-ltr")
    # for i in desc:
    #     desc_ls.append(i.text)
    # # print(desc_ls)
    # print(len(desc_ls))
    #
    #
    # # Reviews
    # reviews = soup.find_all('div', class_ = "r1dxllyb dir dir-ltr")
    # for i in reviews:
    #     reviews_ls.append(i.text)
    # # print(reviews_ls)
    # print(len(reviews_ls))

df = pd.DataFrame({"Product_Name": names_ls, "Product_prices": prices_ls})
# df.to_csv("airbnb.csv")
