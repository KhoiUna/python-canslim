from datetime import date
import pandas as pd
from get_eps import get_quarterly_eps
from get_roe_revenue import get_roe, get_revenue_quarterly


columns = ['TICKER', 'Q1', 'Q2', 'Q3', 'Q4',
           "Q1'", 'EPS%', 'ROE', 'REV%', 'UPDATED DATE']
tickers_row = []
tickers_dict = {}


def get_revenue_growth_quarterly(revenue_list):
    try:
        revenue_growth = round(
            (revenue_list[0] - revenue_list[4]) / revenue_list[4] * 100, 2)
        return revenue_growth
    except:
        pass


def get_stock_df(tickers_to_analyze):
    try:
        global tickers_row

        i = 0
        while i < len(tickers_to_analyze):
            quarterly_eps = get_quarterly_eps(
                tickers_to_analyze[i])  # get a list of quarterly eps

            eps_growth_pct = round(
                (quarterly_eps[4] - quarterly_eps[0]) / abs(quarterly_eps[0]) * 100, 2)  # calculate eps growth btwn current quarter and same quarter last year

            roe = get_roe(tickers_to_analyze[i])

            revenue_list = get_revenue_quarterly(tickers_to_analyze[i])
            revenue_growth_pct = get_revenue_growth_quarterly(
                revenue_list)

            # Append EPS growth percentage to  eps_growth list
            tickers_row.append(tickers_to_analyze[i].upper())
            tickers_row.append(quarterly_eps[0])
            tickers_row.append(quarterly_eps[1])
            tickers_row.append(quarterly_eps[2])
            tickers_row.append(quarterly_eps[3])
            tickers_row.append(quarterly_eps[4])
            tickers_row.append(eps_growth_pct)
            tickers_row.append(roe)
            tickers_row.append(revenue_growth_pct)
            tickers_row.append(date.today().strftime("%m/%d/%Y"))

            tickers_dict[i] = tickers_row
            tickers_row = []
            i += 1

        # Put data to DataFrame
        stock_df = pd.DataFrame.from_dict(tickers_dict, orient='index')
        stock_df.columns = columns
        return stock_df
    except:
        pass
