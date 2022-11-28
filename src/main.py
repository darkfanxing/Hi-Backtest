import yfinance as yf
from backtesting import Backtest
from strategy import DoubleMAWithRSIStrategy
import os

code = "BTC-USD"

for interval in ["5m", "15m", "60m"]:
    cash = 100_000

    data = yf.Ticker(code)
    data = data.history(period="1mo", interval=interval)
    for _ in range(50):
        backtest = Backtest(data, DoubleMAWithRSIStrategy, cash=cash, commission=0.0)
        stat = backtest.run()
        backtest.optimize(
            sma_length=range(5, 101),
            ema_length=range(5, 101),
            rsi_length=range(10, 31),
            # tp_sl_ratio=linspace(1.1, 2.0, 10).tolist(),
            maximize="Equity Final [$]",
            max_tries=100
        )

        if not os.path.exists(f"src/results/{code}/{interval}"):
            os.makedirs(f"src/results/{code}/{interval}")

        backtest.plot(
            open_browser=False,
            filename=f"src/results/{code}/{interval}/{backtest._results['# Trades']}Trades, {100 * round((backtest._results['Equity Final [$]'] - cash) / cash, 2)}%, sma{backtest._results._strategy.sma_length}, ema{backtest._results._strategy.ema_length}, rsi{backtest._results._strategy.rsi_length}"
        )
