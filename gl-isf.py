from bs4 import BeautifulSoup
import urllib.request
import requests

# sauce = urllib.request.urlopen("https://pythonprogramming.net/parsememcparseface/").read()
# soup = bs.BeautifulSoup(sauce, "lxml")
sauce = urllib.request.urlopen("https://www.allkeyshop.com/blog/buy-xcom-2-cd-key-compare-prices/").read()
# sauce = urllib.request.urlopen("https://www.allkeyshop.com/blog/buy-gta-5-cd-key-compare-prices/").read()
soup = BeautifulSoup(sauce, "lxml")

# print(soup.title)
# print(soup.prettify())
# print(soup.get_text())

# for link in soup.find_all('a'):
#     print(link.get('href'))

# <meta content="5.39" itemprop="lowPrice"/>
# <span content="5.39" itemprop="lowPrice">

# print(soup.find(itemprop="lowPrice"))

rawprice = soup.find(itemprop="lowPrice")

# print(rawprice)
ff = False
sf = False
price_str = ""
for char in str(rawprice):
    # print(char)
    if char == '"' and ff == False:
        ff = True
    elif char == '"' and ff == True:
        sf = True
    elif ff == True and sf == False:
        price_str += char
    else:
        pass
print(price_str)