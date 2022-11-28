from backtesting import Strategy
import pandas as pd
from pandas_ta import momentum, sma, ema


def is_above_price(data, price):
    return True if data.Open[-1] > price and data.High[-1] > price and data.Low[-1] > price and data.Close[-1] > price else False


def is_below_price(data, price):
    return True if data.Open[-1] < price and data.High[-1] < price and data.Low[-1] < price and data.Close[-1] < price else False


class DoubleMAWithRSIStrategy(Strategy):
    rsi_length = 14
    sma_length = 10
    ema_length = 10
    tp_sl_ratio = 1.5

    def init(self):
        super().init()

        self.rsi = self.I(momentum.rsi, pd.Series(
            self.data.Close), self.rsi_length)
        self.sma = self.I(sma, pd.Series(self.data.Close), self.sma_length)
        self.ema = self.I(ema, pd.Series(self.data.Close), self.ema_length)
        self.count = 0

    def next(self):
        if not self.position.is_long and not self.position.is_short:
            if 50 < self.rsi[-1] < 70 and is_above_price(self.data, self.sma[-1]) and self.sma[-1] > self.ema[-1] and self.data.Close[-1] > self.data.Open[-1]:
                self.buy(
                    sl=self.sma[-1], tp=self.data.Close[-1] +
                    self.tp_sl_ratio * (self.data.Close[-1] - self.sma[-1])
                )
            elif 30 < self.rsi[-1] < 50 and is_below_price(self.data, self.sma[-1]) and self.sma[-1] < self.ema[-1] and self.data.Close[-1] < self.data.Open[-1]:
                self.sell(
                    sl=self.sma[-1], tp=self.data.Close[-1] -
                    self.tp_sl_ratio * (self.sma[-1] - self.data.Close[-1])
                )
