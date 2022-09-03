# Introduction

- A Python scraping program to analyze & visualize stocks using the [CANSLIM](https://www.investopedia.com/terms/c/canslim.asp) method by William J.O'Neil, also includes a calculator to find entry points to add more positions to your portfolio (Pyramid Buying).

## Tech stack

- Python:
  - pandas, numpy, matplotlib
  - [python-fire](https://github.com/google/python-fire) to automatically generate command line interfaces.
  - [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#) to scrap HTML data.

## Instructions

1. `git clone https://github.com/KhoiUna/python_canslim.git && cd python_canslim`
2. `pip install -r requirements.txt` to install the required dependencies
3. `python CANSLIM/main.py analyze [TICKER] [TICKER]...` to analyze stocks using the CANSLIM method.
   - You can run `python CANSLIM/main.py -h` or `python CANSLIM/main.py analyze -h` to learn more about available command.
   - The program will return **-GOOD STOCKS-** that fit the CANSLIM criteria.
4. `python Pyramid_Profit_Calculator/main.py` to start the Pyramid Buying calculator GUI.

### Notes:

- Data are scraped from [Macrotrends](https://www.macrotrends.net/)
