import pandas as pd
from get_stock_df import get_stock_df
from visualize_stocks_quarterly import visualize_stocks_quarterly
from visualize_stocks_annually import visualize_stocks_annually
import matplotlib.pyplot as plt


def main():
    tickers_to_analyze = []
    tickers_list = []

    try:
        question = input('Type tickers (tt) or Use list (ul): ')

        if question == 'tt':
            x = True
            print('Type tickers (type \d when done):')
            while x:
                tickers_to_analyze.append(input())
                if tickers_to_analyze[len(tickers_to_analyze) - 1] == '\d':
                    print('----------DONE----------')
                    print()
                    tickers_to_analyze.pop(-1)
                    x = False
            stock_df = get_stock_df(tickers_to_analyze)
        elif question == 'ul':
            print()
            print('----------ANALYZING----------')
            stock_df = get_stock_df(tickers_list)

        print(stock_df)
        # visualize_stocks_quarterly(stock_df['TICKER'].tolist())
        # visualize_stocks_annually(stock_df['TICKER'].tolist())

        # Select good stocks
        # You can set your good_stocks_criteria here
        good_stocks_criteria = 20
        good_stocks = stock_df[(stock_df['EPS%'] > good_stocks_criteria)
                                & (stock_df['REV%'] > good_stocks_criteria)]
        print()
        if good_stocks['TICKER'].count() > 0:
            print('----------GOOD STOCKS----------')
            print()
            print(good_stocks)
            print()

            visualize_stocks_quarterly(good_stocks['TICKER'].tolist())
            visualize_stocks_annually(good_stocks['TICKER'].tolist())

            save = input('Do you want to save DataFrame (y/n) ? ')
            if save.lower() == 'y':
                good_stocks.to_csv('../python_good_stocks_df.csv', index=False)
                print('----------SAVED !!!----------')
            else:
                print('----------OK----------')
        else:
            print('----------NO GOOD STOCKS----------')
    except:
        pass 


main()
