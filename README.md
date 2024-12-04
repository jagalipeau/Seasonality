# Seasonality Analyzer v2

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Latest-brightgreen)](https://pandas.pydata.org/)

## Overview

Seasonality Analyzer is a Python tool that identifies stocks with consistent positive returns during specific months over a historical period. It analyzes stock performance patterns and returns a pandas DataFrame containing stocks that meet user-defined criteria for average returns and consistency.

> **Note**: This tool is designed for preliminary stock analysis and research purposes only. It is not intended to be used as a standalone investment strategy.

## Features

- Analyze stocks for seasonal patterns
- Configurable lookback period (default: 5 years)
- Customizable return thresholds
- Flexible stock list input (pre-configured with S&P 500)
- Monthly performance analysis

## Prerequisites

- Python 3.6 or higher
- Required Python packages (install via pip):
  ```bash
  pip install pandas yfinance
  ```
- Directory structure:
  ```
  seasonality-v2/
  ├── main.py
  ├── stock_data.py
  └── csv/              # Required folder for storing stock data
  ```

> **Note**: Create a `csv` folder in the root directory if it doesn't exist. The script will read existing CSV files from this folder to avoid re-downloading data unnecessarily.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/jagalipeau/Seasonality.git
   cd Seasonality
   ```

2. Run the main script:
   ```bash
   python main.py
   ```

### Customization Options

You can customize the analysis by modifying the following parameters in the code:

- **Stock List**: Modify the `stocks` variable in `main.py` to analyze different stocks
- **Lookback Period**: Adjust the years parameter in `avg_returns_list.py`:
  ```python
  rtn_data = avg_rtn(stock_data, 5)[0]  # Change 5 to desired number of years
  ```
- **Target Month**: Update the month variable in `main.py`:
  ```python
  # Change month (1 = January, 12 = December)
  month = 12  # Example: Set to December
  ```
- **Positive Return Threshold**: Modify the threshold in `main.py`:
  ```python
  # Change threshold (0.8 = stock must be positive 80% of the time)
  threshold = 0.8  # Example: Set to 80% positive returns
  ```

## Maintenance

- Clear the contents of the `CSV` folder on the 2nd day of each month to ensure fresh data analysis

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## Disclaimer

This tool is for educational and research purposes only. It is not financial advice, and should not be used as the sole basis for investment decisions. Always conduct thorough research and consult with financial professionals before making investment choices.
