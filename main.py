import requests
from bs4 import BeautifulSoup

URL = "https://luis-c465.github.io/scraping-site-live/"
html = requests.get(URL).text
page = BeautifulSoup(html, "html.parser")

infoBoxes = page.find_all("div", attrs={"class": "info"})
information = {}

for infoElm in infoBoxes:
    key = infoElm.select(".key")[0].text
    value = infoElm.select(".value")[0].text
    print(key, value)
    information[key] = value

print(information)

print(information['Price'])
