import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
import yfinance as yp
from datetime import date
from talib import abstract
from scipy.signal import argrelextrema

#####################################################
today_SPY_file_name = str(date.today()).replace('-','') + "_SPY" + ".csv"

spy = yp.download("SPY", period = "5y", end = str(date.today()), interval="1wk").to_csv()

f_spy = open(today_SPY_file_name,"w+")

f_spy.write(spy)

f_spy.close()

df_spy = pd.read_csv(today_SPY_file_name)

df_spy.dropna(inplace=True)
df_spy.drop(df_spy.tail(1).index,inplace=True)#drop last row
df_spy.reset_index(drop=True, inplace=True)

df_spy.to_csv(today_SPY_file_name, index=False)


plotDf = pd.read_csv(today_SPY_file_name,index_col=0,parse_dates=True)
plotDf.index.name = 'Date'

sma = abstract.SMA(plotDf["Close"], 5)

#mpf.plot(plotDf, type='candle', mav=(2))


plt.plot(sma)
plt.show()
"""
x = np.random.random(12)

# for local maxima
argrelextrema(x, np.greater)

# for local minima
argrelextrema(x, np.less)
"""