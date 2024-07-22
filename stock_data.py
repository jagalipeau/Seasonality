# Imports
import os
import pandas as pd
import yfinance as yf


def tickerData(ticker):
    ticker = ticker.upper()
    if os.path.exists(f"CSV/{ticker}.csv"):
        # print(f"{ticker} already exists")
        data = pd.read_csv(f"CSV/{ticker}.csv", index_col=0)
        return data
    else:
        data = yf.download(tickers=ticker, period="max", interval="1mo")
        pd.DataFrame.to_csv(data, f"CSV/{ticker}.csv")
        # print("Created a new CSV")
        return data


import avg_return as avg


if __name__ == "__main__":
    data = tickerData("GNRC")
    returns = avg.avg_rtn(data, 5)[0]
    print(returns.loc[returns.index == "July"])
