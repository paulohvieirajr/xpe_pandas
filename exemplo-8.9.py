import pandas as pd
import yfinance as yf

df = yf.download('AAPL', start='2022-01-01', end='2022-12-31')
print('\nDownload e DataFrame de dados do Yahoo Finance: \n')
print(df)

