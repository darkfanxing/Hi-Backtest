<!-- omit in toc -->
Hi-Backtest
=================
Just a backtest trading strategies project.

<!-- omit in toc -->
Table of contents
=================
- [Environment Setup](#environment-setup)
- [Get Data](#get-data)
- [Strategies](#strategies)
- [Reference](#reference)

Environment Setup
=================
```bash
pip install pipenv
pipenv shell
pipenv install
```

Then, you can run the `src/main.py`
```bash
python src/main.py
```

Get Data 
=================
1. Refer to Binance's symbol and time period
2. Modify the paramters (symbol and time) @ `src/utils/download_latest_binance_data.py`
3. Run the python file
    ```
    python  src/utils/download_latest_binance_data
    ```
4. You get the historical klines data @ `src/data/`

Strategies
=================
|               Name              |                                               Description                                              |
|:-------------------------------:|:------------------------------------------------------------------------------------------------------:|
| SMA + EMA + RSI (SMAEMAWithRSI) | Refer to the DMA (Double Moving Average) System. Looks for big trends. Default SMA 10, EMA 10, RSI 14. |
|       Waiting to be added       |                                           Waiting to be added                                          |

Reference
=================
- [crypto_backtrader - koreal6803](https://github.com/koreal6803/crypto_backtrader)
- [python-binance - sammchardy](https://github.com/sammchardy/python-binance)
- [backtesting.py - kernc](https://github.com/kernc/backtesting.py)