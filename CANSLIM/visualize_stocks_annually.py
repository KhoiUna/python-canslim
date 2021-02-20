import matplotlib.pyplot as plt
import numpy as np
from get_eps import get_annually_eps
from get_roe_revenue import get_revenue_annually


def get_pct_change(eps_list):
    eps_list = np.array(eps_list)
    pct_change = np.diff(eps_list) / abs(eps_list)[:len(eps_list) - 1] * 100
    return pct_change


def visualize_eps(stock_list):
    x_val = ['Q1', 'Q2', 'Q3', 'Q4', "Q1'"]
    legends = []

    plt.title('Annually EPS Comparison')
    plt.ylabel('EPS')

    i = 0
    while i < len(stock_list):
        legends.append(stock_list[i].upper())
        eps_list = get_annually_eps(stock_list[i])
        plt.plot(x_val, eps_list, marker='o')
        i += 1

    plt.legend(legends)
    return


def visualize_eps_growth(stock_list):
    x_val = ['Q1-2', 'Q2-3', 'Q3-4', "Q4-1'"]
    legends = []
    avg_data = []

    plt.title('Annually EPS Growth Comparison')
    plt.ylabel('Growth (%)')

    i = 0
    while i < len(stock_list):
        legends.append(stock_list[i].upper())
        eps_list = get_annually_eps(stock_list[i])  # get eps_list
        eps_pct_change = get_pct_change(
            eps_list)
        avg_data.append(eps_pct_change)
        plt.plot(x_val, eps_pct_change, alpha=0.5, marker='o')
        i += 1

    plt.plot(x_val, np.array(avg_data).mean(axis=0),
             linestyle='--', marker='o')
    legends.append('Avg Line')
    plt.legend(legends)
    return


def visualize_revenue(stock_list):
    x_val = ['Q1', 'Q2', 'Q3', 'Q4', "Q1'"]
    legends = []

    plt.title('Annually REV. Comparison')
    plt.ylabel('Revenue (million $)')

    i = 0
    while i < len(stock_list):
        legends.append(stock_list[i].upper())
        revenue_list = get_revenue_annually(stock_list[i])
        plt.plot(x_val, revenue_list[::-1], marker='o')
        i += 1

    plt.legend(legends)
    return


def visualize_revenue_growth(stock_list):
    x_val = ['Q1-2', 'Q2-3', 'Q3-4', "Q4-1'"]
    legends = []
    avg_data = []

    plt.title('Annually REV. Growth Comparison')
    plt.ylabel('Growth (%)')

    i = 0
    while i < len(stock_list):
        legends.append(stock_list[i].upper())
        revenue_list = get_revenue_annually(stock_list[i])  # get revenue_list
        revenue_pct_change = get_pct_change(
            revenue_list[::-1])
        avg_data.append(revenue_pct_change)
        plt.plot(x_val, revenue_pct_change, alpha=0.5, marker='o')
        i += 1

    plt.plot(x_val, np.array(avg_data).mean(axis=0),
             linestyle='--', marker='o')
    legends.append('Avg Line')
    plt.legend(legends)
    return


def visualize_stocks_annually(stock_list):
    # Plot eps comparison
    plt.subplot(2, 2, 1)
    visualize_eps(stock_list)

    # Plot eps growth
    plt.subplot(2, 2, 2)
    visualize_eps_growth(stock_list)

    # Plot revenue comparison
    plt.subplot(2, 2, 3)
    visualize_revenue(stock_list)

    # Plot revenue growth
    plt.subplot(2, 2, 4)
    visualize_revenue_growth(stock_list)

    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.show()
    return
