import pandas as pd
from avg_return import avg_rtn
from stock_data import tickerData
import warnings
from pandas.errors import SettingWithCopyWarning

warnings.simplefilter(action="ignore", category=SettingWithCopyWarning)


def get_monthly_returns(stocks_list, month):
    returns = []

    for stock in stocks_list:
        try:
            stock_data = tickerData(stock)
            rtn_data = avg_rtn(stock_data, 5)[0]
            row_data = rtn_data.loc[rtn_data.index == month]
            # print("row data", row_data)
            row = stock_data.iloc[[-1]]

            row["PL%"] = row_data["PL%"].iloc[0]
            row["pos_rate%"] = row_data["pos_rate%"].iloc[0]

            row["Ticker"] = stock
            # row = row.drop("month_no", axis=1)
            # print(row)
            returns.append(row)
        except:
            pass

    df = pd.concat(returns, ignore_index=True).drop("month_no", axis=1)
    df.set_index("Ticker", inplace=True)
    return df
