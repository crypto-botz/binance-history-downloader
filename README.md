# Binance Data Downloader

This script fetches historical trading data for specified symbols from Binance and saves it as CSV files. It uses the `ccxt` library to access Binance's API.

## Features
- Download historical OHLCV (Open, High, Low, Close, Volume) data.
- Supports custom timeframes (default: 1-minute candles).
- Fetch data for multiple trading pairs.
- Automatically saves data as CSV files.
- Handles large date ranges by breaking requests into smaller intervals.

## Requirements
- Python 3.7 or higher.
- Install required Python libraries using:
  ```bash
  pip install -r requirements.txt
  ```

## Installation
1. Clone the repository or copy the script to your local environment.
2. Install the dependencies listed in `requirements.txt`.
3. Run the script by executing:
   ```bash
   python script_name.py
   ```

## Usage
1. Define the list of trading pairs in the `tickers` variable.
2. Set the desired start and end dates (`start_date`, `end_date`).
   - `start_date`: Required, in the format `YYYY-MM-DD`.
   - `end_date`: Optional; use `None` for the current date.
3. Specify the directory where CSV files should be saved in the `save_path` variable.
4. Run the script.

## Example
To fetch data for the trading pairs `BTC/USDT` and `ETH/USDT` from January 1, 2020, to the current date:

```python
if __name__ == "__main__":
    tickers = ["BTC/USDT", "ETH/USDT"]
    start_date = '2020-01-01'
    end_date = None

    download_data_for_tickers(tickers, start_date, end_date)
```

The data will be saved in the specified folder as CSV files named after the trading pairs (e.g., `BTC_USDT.csv`).

## Notes
- Ensure you have an active internet connection.
- Avoid requesting large datasets at once to prevent API rate limit issues.
- For extended historical data, the script automatically breaks requests into smaller intervals.

## Dependencies
- `ccxt`: Used for interacting with Binance's API.
- `pandas`: For data manipulation and saving CSV files.

## Troubleshooting
If you encounter errors:
1. Verify your Python version (>= 3.7).
2. Check if the `ccxt` and `pandas` libraries are installed.
3. Ensure the Binance API is accessible from your network.
4. Look for error messages in the console to diagnose the issue.

## License
This project is licensed under the MIT License.
