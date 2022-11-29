from binance.client import Client
from datetime import datetime
import os
import pandas as pd


def download_latest_binance_data(
    symbol="BTCUSDT",
    time_period="4h",
    binance_api_key="Enter your API Key",
    binance_api_secret="Enter your API secret",
    start_time="01 Jan 2017 00:00:00",
):
    # connect Binance
    binance_client = Client(api_key=binance_api_key,
                            api_secret=binance_api_secret)
    binance_client.get_historical_klines(
        "BTCUSDT", "30m", start_str=start_time)

    if not os.path.exists("src/data"):
        os.makedirs("src/data")

    # Check if old file exists
    filename = f"src/data/{symbol}-{time_period}"
    if os.path.isfile(filename):
        data = pd.read_csv(
            filename, index_col="Timestamp", parse_dates=True)
    else:
        data = pd.DataFrame()

    if not data.empty:
        start_time = data.index[-1].to_pydatetime()

    # Download data
    print(f"Date Range: {start_time} to {datetime.now()}")
    print("Downloading...")
    klines = binance_client.get_historical_klines(
        symbol, time_period, start_time)

    # Save data
    new_data = pd.DataFrame(klines, columns=['Timestamp', 'Open', 'High', 'Low', 'Close',
                                             'Volume', 'Close_time', 'Quote_av', 'Trades', 'Tb_base_av', 'Tb_quote_av', 'Ignore'])

    new_data.Timestamp = pd.to_datetime(new_data.Timestamp, unit="ms")
    new_data.set_index("Timestamp", inplace=True)
    new_data = new_data[~new_data.index.duplicated(keep="last")]
    new_data = new_data.astype(float)

    if len(data) > 0:
        data = data.append(new_data)
    else:
        data = new_data

    data.to_csv(filename)
    print("All caught up..!")
    return data

if __name__ == "__main__":
    download_latest_binance_data(symbol="BTCUSDT", time_period="4h")