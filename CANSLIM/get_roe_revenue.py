from bs4 import BeautifulSoup
import requests


def get_roe(ticker):
    url = 'https://www.macrotrends.net/stocks/charts/' + \
        ticker.lower() + '//roe'
    web = requests.get(
        url, 'html.parser')

    soup = BeautifulSoup(web.content, features="lxml")

    data = soup.select("td")[3].get_text()[:-1]
    roe = float(data)
    return roe


def get_revenue_quarterly(ticker):
    url = 'https://www.macrotrends.net/stocks/charts/' + \
        ticker.lower() + '//revenue'
    web = requests.get(
        url, 'html.parser')

    soup = BeautifulSoup(web.content, features="lxml")

    data = soup.select("table > tbody")[1].select("tr > td")
    revenue_list = []
    i = 1
    while i < (len(data[:10])):
        revenue = float(data[i].get_text()[1:].replace(',', ''))
        revenue_list.append(revenue)
        i += 2

    # return revenue_list from latest to furthest date (left to right)
    return revenue_list


def get_revenue_annually(ticker):
    url = 'https://www.macrotrends.net/stocks/charts/' + \
        ticker.lower() + '//revenue'

    web = requests.get(
        url, 'html.parser')

    soup = BeautifulSoup(web.content, features="lxml")

    data = soup.select("table > tbody")[0].select("tr > td")
    revenue_list = []
    i = 1
    while i < (len(data[:10])):
        revenue = float(data[i].get_text()[1:].replace(',', ''))
        revenue_list.append(revenue)
        i += 2

    # return revenue_list from latest to furthest date (left to right)
    return revenue_list
