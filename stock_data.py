import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


yahoo_url = "https://finance.yahoo.com/quote/{}?p={}"


def get_stock_data(symbol):
    html = urlopen(yahoo_url.format(symbol, symbol))
    soup = BeautifulSoup(html, "lxml")
    pre_market = get_pre_market_data(soup)
    after_hours = get_after_hours_data(soup)
    current_data = get_current_data(soup)
    if pre_market:
        return pre_market
    if after_hours:
        return after_hours
    if current_data:
        return current_data
    return (500, 500)


def get_pre_market_data(soup):
    if len(list(soup.findAll(text="Pre-Market:"))) > 0:
        values = list(soup.findAll(text="Pre-Market:")
                      [0].parent.parent.parent.children)
        pre_market_price = float(values[0].text.replace(",", ""))
        pre_market_change = float(values[4].text.split(" (")[1][:-2])
        return (pre_market_price, pre_market_change)
    else:
        return None


def get_after_hours_data(soup):
    if len(list(soup.findAll(text="After hours:"))) > 0:
        values = list(soup.findAll(text="After hours:")
                      [0].parent.parent.parent.children)
        ah_price = float(values[0].text.replace(",", ""))
        ah_change = float(values[4].text.split(" (")[1][:-2])
        return (ah_price, ah_change)
    else:
        return None


def get_current_data(soup):
    if len(soup.findAll(id="quote-market-notice")) > 0:
        values = list(list(soup.findAll(id="quote-market-notice"))
                      [0].parent.children)
        current_value = float(list(list(soup.findAll(
            id="quote-market-notice"))[0].parent.parent.children)[0].text.replace(",", ""))
        current_change = float(list(list(soup.findAll(
            id="quote-market-notice"))[0].parent.children)[0].text.split(" (")[1][:-2])
        return (current_value, current_change)
    else:
        return None
