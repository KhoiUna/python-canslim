from bs4 import BeautifulSoup
import requests


def get_quarterly_eps(ticker):
    url = 'https://www.macrotrends.net/stocks/charts/' + \
        ticker.lower() + '//eps-earnings-per-share-diluted'
    web = requests.get(
        url, 'html.parser')

    soup = BeautifulSoup(web.content, features="lxml")

    try:
        data = soup.select("table > tbody")[1].select("tr > td")
        quarterly_eps = []
        i = 1
        while i < (len(data[:10])):
            eps = float(data[i].get_text()[1:])
            quarterly_eps.append(eps)
            i += 2
        return quarterly_eps[::-1]
    except:
        pass


def get_annually_eps(ticker):
    url = 'https://www.macrotrends.net/stocks/charts/' + \
        ticker.lower() + '//eps-earnings-per-share-diluted'
    web = requests.get(
        url, 'html.parser')

    soup = BeautifulSoup(web.content, features="lxml")

    try:
        data = soup.select("table > tbody")[0].select("tr > td")
        quarterly_eps = []
        i = 1
        while i < (len(data[:10])):
            eps = float(data[i].get_text()[1:])
            quarterly_eps.append(eps)
            i += 2
        return quarterly_eps[::-1]
    except:
        pass
