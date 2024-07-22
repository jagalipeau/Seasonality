# Imports
import math
import pandas as pd
import numpy as np


def avg_rtn(data, years=0):
    """
    Calculate and return average returns for a given stock data.

    Parameters:
    - data (pandas Series): The input data series containing the closing and opening prices of the stock over time.
    - years (int): The number of years to consider when calculating the average returns. Default is 0, which means all available data will be used.

    Returns:
    - A tuple containing two values:
        1) The averaged return series, with each entry representing the average return for a month.
        2) An integer indicating the maximum number of years considered in the calculation.

    """
    # Check if 'years' is provided
    if years == 0:
        pass
    else:
        time = years * 12

    # Limit data to the specified timeframe (if provided)
    if len(data) > time:
        data = data.tail(time)
    elif len(data) < time:
        pass

    max_years = math.ceil(len(data) / 12)

    # Convert index to datetime format for easy sorting and manipulation
    data.index = pd.to_datetime(data.index)

    # Add a column indicating the month number (1-12)
    data["month_no"] = data.index.strftime("%m")

    # Calculate the percentage change in prices between open and close
    data["PL%"] = round(((data["Close"] - data["Open"]) / data["Open"]) * 100, 2)

    # Calculate the percentage of positive returns (i.e., where closing price is higher than opening price)
    data["pos_rate%"] = np.where(data["Open"] - data["Close"] < 0, 1, -1) * 100

    # Group by month and calculate average return for each month
    data_avg_rtn = data.groupby("month_no").mean().sort_index()

    # Replace the index (now a datetime series) with the corresponding month names
    data_avg_rtn.index = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    return data_avg_rtn, max_years
