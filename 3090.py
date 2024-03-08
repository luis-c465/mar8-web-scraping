import requests
from bs4 import BeautifulSoup

URL = "https://www.ebay.com/itm/375290556773?epid=26053974644&itmmeta=01HRFWK78VZB2JSQ2BG23717A7&hash=item57610f7165:g:YjYAAOSw-GBl4~jF&itmprp=enc:AQAIAAAAwLb5WhLbK+IWb+rBhIc3dxg7M4cjxfGxWMe4WUnaxe51ymu3pGETSP2qJXuL7GE1TVHfx+vEnl7Xm6lpMyscNJPX10uMyOQg3Q/xzhgCwxWTGtjfvAjHX3G/2ToYIt+LwNbD3xzfoSMdMX4hYfQekIyGOCTSdiGsae5XuhGZv8iGLBdIsZwTRv3mLOM2u86kD4yDNxXh9CVaXhANqnkgzALR310ZHe7PlXKcho0S7edLpjF0qKqWg9yzVscX0GwmBg==|tkp:Bk9SR9L0zPzDYw"

html = requests.get(URL).text
page = BeautifulSoup(html, "html.parser")

title = page.find("h1", attrs={"class": "x-item-title__mainTitle"}).text.strip()
price = page.find("div", attrs={"class": "x-price-primary"}).text
quality = page.select_one(".x-item-condition-text .ux-textspans").text
print(title, price, quality)
