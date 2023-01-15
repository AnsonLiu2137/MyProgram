#import numpy as np
import pandas as pd
import yfinance as yf
import datetime
import matplotlib.pyplot as plt



# used the selected 30 stocks to test td sequential's performance, transaction costs were also include
#everyday NAV was stored in the list called capital
ratio = 1.5
start = datetime.datetime(2020, 12, 1)
end = datetime.datetime(2022, 12, 1)
df = pd.DataFrame()
df_high = pd.DataFrame()
df_low = pd.DataFrame()
basket = ["DXCM", "OKE", "ETSY", "CF", "NCLH", "AES", "CCL", "NOW", "IPG", "CNC", "MSI", "WTW", "AVGO", "ULTA", "APA", "URI", "UNH", "NWSA", "EXPE", "STE", "KIM", "DHI", "KMI", "EW", "FBHS", "ZBH", "ILMN", "VRTX", "CPB", "TECH"]
#basket = ["IPG", "NOW", "MSI", "NWSA", "INTU", "CF", "UNH", "ETSY", "TECH", "WTW", "F", "STE", "AES", "EW", "DXCM", "NTRS", "FOX", "GILD", "KMB", "BRO", "AVGO", "PLD", "DE", "CNC", "CTRA", "EXPD", "CCL", "PCAR". "CTVA", "NWS"]
for stock in basket:
    ticket = yf.Ticker(stock)
    df_ticket = ticket.history(start = start, end = end)
    df = pd.concat([df, df_ticket["Close"].rename(stock)], axis = 1)

df = df.dropna()
for stock in basket:
    ticket = yf.Ticker(stock)
    df_ticket = ticket.history(start = start, end = end)
    df_high = pd.concat([df_high, df_ticket["High"].rename(stock)], axis = 1)
df_high = df_high.dropna()
for stock in basket:
    ticket = yf.Ticker(stock)
    df_ticket = ticket.history(start = start, end = end)
    df_low = pd.concat([df_low, df_ticket["Low"].rename(stock)], axis = 1)
df_low = df_low.dropna()


AAPL = yf.Ticker("AAPL")
df_aapl = AAPL.history(start = start, end = end)
print(df_aapl.index[0]) # can use it to get back the date

#for stock in basket:
dict_setup_long = {}
dict_setup_short = {}
investing ={}
entry = {}
stop_loss = {}
take_profit = {}
long = {}
short = {}
portfolio = {}
cash = 100000000
nav = 0
long_post = {}
short_post = {}
capital = []
for stock in df.columns:
    dict_setup_long[stock] = 0
    dict_setup_short[stock] = 0
    investing[stock] = False
    long[stock] = False
    short[stock] = False


for i in range(len(df.index)):
    count = 0
    if portfolio == {}:
        nav = cash
    else:
        for ele in portfolio:
            count += portfolio[ele] * df[ele].iloc[i]
        nav = cash + count

    if i <= 3:
        pass
    for stock in df.columns:
        if df[stock].iloc[i] >= df[stock].iloc[i-4]:
            dict_setup_long[stock] = 0
            #if stock in dict_setup_short:
            dict_setup_short[stock] += 1
            #else:
               # dict_setup_short[stock] = 1
        elif df[stock].iloc[i] <= df[stock].iloc[i-4]:
            dict_setup_short[stock] = 0
            #if stock in dict_setup_long:
            dict_setup_long[stock] += 1
            #else:
             #   dict_setup_long[stock] = 1
        else:
            dict_setup_short[stock] = dict_setup_long[stock] = 0
        if dict_setup_short[stock] == 9 and investing[stock] == False:
            if cash >= 1000000:
                entry[stock] = df[stock].iloc[i]
                stop_loss[stock] = df[stock].iloc[i] + 0.272 * (df[stock].iloc[i] - df_low[stock].iloc[i - 8])
                take_profit[stock] = df[stock].iloc[i] - ratio * 0.272 * (df[stock].iloc[i] - df_low[stock].iloc[i - 8])
                investing[stock] = True
                short[stock] = True
                portfolio[stock] = - 0.06 * nav / entry[stock]
                dict_setup_short[stock] = dict_setup_long[stock] = 0
                cash = cash - portfolio[stock] * entry[stock]
                short_post[stock] = i
            else:
                dict_setup_short[stock] = dict_setup_long[stock] = 0
        if dict_setup_long[stock] == 9 and investing[stock] == False:
            if cash >= 0.06 * nav:
                entry[stock] = df[stock].iloc[i]
                stop_loss[stock] = df[stock].iloc[i] - 0.272 * (df_high[stock].iloc[i - 8] - df[stock].iloc[i])
                take_profit[stock] = df[stock].iloc[i] + ratio * 0.272 * (df_high[stock].iloc[i - 8] - df[stock].iloc[i])
                investing[stock] = True
                long[stock] = True
                portfolio[stock] = 0.06 * nav / entry[stock]
                dict_setup_short[stock] = dict_setup_long[stock] = 0
                cash = cash - portfolio[stock] * entry[stock]
            else:
                dict_setup_short[stock] = dict_setup_long[stock] = 0
        if (dict_setup_long[stock] == 9 or dict_setup_short[stock]) and investing[stock] == True:
            dict_setup_long[stock] = dict_setup_short[stock] = 0

        if investing[stock] == True:
            if long[stock] == True:
                if df[stock].iloc[i] <= stop_loss[stock] or df[stock].iloc[i] >= take_profit[stock]:
                    cash = cash + portfolio[stock] * df[stock].iloc[i] - 0.006119 * portfolio[stock] - 0.0000229 * df[stock].iloc[i] * portfolio[stock]
                    portfolio[stock] = 0
                    investing[stock] = False
                    long[stock] = False


            else:
                if df[stock].iloc[i] >= stop_loss[stock] or df[stock].iloc[i] <= take_profit[stock]:
                    cash = cash + portfolio[stock] * df[stock].iloc[i] + 0.006119 * portfolio[stock] + 0.0000229 * entry[stock] * portfolio[stock] + 0.017 * ((i - short_post[stock])/ 365) * entry[stock] * portfolio[stock]
                    portfolio[stock] = 0
                    investing[stock] = False
                    short[stock] = False
    print(df.index[i], portfolio)
    capital.append(nav)

print(capital)









#use dictionary to indicate the trading postion of each stock, and calculate the setup