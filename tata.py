import pandas as pd
import requests
from bs4 import BeautifulSoup

tata_url = "https://www.iplt20.com/auction"
tata = requests.get(tata_url)
# print(tata.status_code)

soup = BeautifulSoup(tata.text, 'lxml')
table = soup.find('table', class_ ="ih-td-tab auction-tbl")
# print(table)

header = table.find_all('th')
# print(header)
header_ls = []
for head in header:
    h = head.text
    header_ls.append(h)
# print(header_ls)

df = pd.DataFrame(columns=header_ls)

rows = table.find_all('tr')
# print(rows[1:])
for row in rows[1:]:
    first_td = row.find_all('td')[0].find('div', class_ = "ih-pt-ic").text.strip()
    head = row.find_all('td')
    e_row = [tr.text for tr in head]
    e_row.insert(0,first_td)
    l = len(df)
    df.loc[l] = e_row
print(df)

# df.to_csv("tata.csv")