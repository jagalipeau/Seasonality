# Seasonality

This script returns a pandas dataframe containing stocks that over the past x years has an average return of y and is postive every time. The user can change the montht that is looks at as well as the number of years to look back. The default is 5 years.

The point of this script is to give users a start point of stocks to look at in the coming months. This is not meant to be an investment strategy.

### Running the script

- Run main.py
- Change the **stocks** variable to the list of stocks you want to look at. It is currently set up with the SP500.
- Can change threshold of how often a stock is postive on line 304.
- To change x number of years change **rtn_data = avg_rtn(stock_data, 5)[0]** in avg_returns_list.py

### Notes

- Must create a relative directory called **CSV**
- Should delete the items inside of the CSV folder the 2nd of every month.
