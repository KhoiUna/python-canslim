# Introduction

- A Python scraping program to find & visualize stocks that follow [CANSLIM](https://www.investopedia.com/terms/c/canslim.asp) criteria by William J.O'Neil, also includes a calculator to find entry points to add more positions to portfolio (Pyramid Buying).

## Tech stack

- Python: [python-fire](https://github.com/google/python-fire) to automatically generate command line interfaces.

## Instructions

1. `git clone https://github.com/KhoiUna/python_canslim.git`
2. `python CANSLIM/main.py analyze [TICKER] [TICKER]...` to analyze stocks using the CANSLIM method.
   - You can run `python CANSLIM/main.py -h` or `python CANSLIM/main.py analyze -h` to learn more.
3. `cd Pyramid_Profit_Calculator && python main.py` for Pyramid Buying calculator GUI

### Notes:

- Data are scraped from [Macrotrends](https://www.macrotrends.net/)
