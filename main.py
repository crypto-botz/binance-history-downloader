import ccxt
import pandas as pd
from datetime import datetime

def fetch_binance_data(symbol, start_date, end_date=None, timeframe='1m'):
    """
    Fetch historical data from Binance for a given symbol.

    :param symbol: Trading pair (e.g., "BTC/USDT")
    :param start_date: Start date (format: YYYY-MM-DD)
    :param end_date: End date (format: YYYY-MM-DD), default is the current date
    :param timeframe: Timeframe (e.g., '1m')
    :return: DataFrame with historical data
    """
    exchange = ccxt.binance({'rateLimit': 1200, 'enableRateLimit': True})
    start_timestamp = int(datetime.strptime(start_date, '%Y-%m-%d').timestamp() * 1000)
    end_timestamp = int(datetime.strptime(end_date, '%Y-%m-%d').timestamp() * 1000) if end_date else exchange.milliseconds()

    all_data = []
    limit = 1000

    while start_timestamp < end_timestamp:
        try:
            # Fetch OHLCV data
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, since=start_timestamp, limit=limit)
            if not ohlcv:
                break
            all_data.extend(ohlcv)
            # Update start_timestamp for the next batch
            start_timestamp = ohlcv[-1][0] + 1
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            break

    # Convert data to DataFrame
    df = pd.DataFrame(all_data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Sort data by timestamp in ascending order
    df = df.sort_values(by='timestamp').reset_index(drop=True)
    return df

def download_data_for_tickers(tickers, start_date, end_date=None, save_path="C:\\Users\\user\\Desktop\\history\\crypto\\"):
    """
    Download historical data for a list of tickers and save them as CSV files.

    :param tickers: List of trading pairs (e.g., ['BTC/USDT', 'ETH/USDT'])
    :param start_date: Start date (format: YYYY-MM-DD)
    :param end_date: End date (format: YYYY-MM-DD)
    :param save_path: Directory where the CSV files will be saved
    """
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        df = fetch_binance_data(ticker, start_date, end_date)
        filename = f"{save_path}{ticker.replace('/', '_')}.csv"
        df.to_csv(filename, index=False)
        print(f"Data for {ticker} saved to {filename}.")

# Example usage
if __name__ == "__main__":
    tickers = ["BANANA/FDUSD"]
    # List of tickers
    start_date = '2020-01-01'  # Start date
    end_date = None  # End date (use None for the current date)

    download_data_for_tickers(tickers, start_date, end_date)
