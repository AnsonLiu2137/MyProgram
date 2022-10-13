# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#Q1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel("/Users/ansonliu/Desktop/CUHK Yr4 Term1/FINA4380/HSI.xlsx", "data", index_col = 0, parse_dates = True)
#data.plot()
#plt.show(block=True)

df = df.dropna() #drop the blank entries
#Q2
df_weekly = df.iloc[df.index.dayofweek == 4] #create new weekly dataframe
df_monthly = df.iloc[df.index.is_month_end] #create new monthly dataframe

#Q3 calculate return for the dataframes, and drop the first row of NaN
df_daily_ret = df.pct_change()
df_daily_ret = df_daily_ret.iloc[1:]
df_weekly_ret = df_weekly.pct_change()
df_weekly_ret = df_weekly_ret.iloc[1:]
df_monthly_ret = df_monthly.pct_change()
df_monthly_ret = df_monthly_ret.iloc[1:]
#Q4
df_weekly_cov = df_weekly.cov()
df_weekly_cov.to_csv("covHSI.csv")
#Q5
plt.hist(df_daily_ret["700 HK"].dropna(), bins = 100, density = True) #it doesn't matter if I drop the NA in this line,as I already cleaned the data before
plt.title("700 HK", fontdict = {"fontsize":10})
plt.show()

#Q6
df_std = pd.DataFrame()
df_std2015_06 = pd.DataFrame()
df_std2015_07 = pd.DataFrame()
df_std2015_08 = pd.DataFrame()
df_std2015_09 = pd.DataFrame()
df_std2015_10 = pd.DataFrame()
df_std2015_11 = pd.DataFrame()
df_std2015_12 = pd.DataFrame()
df_std2016_01 = pd.DataFrame()
df_std2016_02 = pd.DataFrame()
df_std2016_03 = pd.DataFrame()
#running for-loop and store monthly data into sub-dataframe in order to calculate std one by one
for date in df_daily_ret.index:
    if date.month == 6 and date. year == 2015:

        df_std2015_06 = pd.concat([df_std2015_06, df_daily_ret.loc[date]], axis = 1)
    if date.month == 7 and date. year == 2015:

        df_std2015_07 = pd.concat([df_std2015_07, df_daily_ret.loc[date]], axis = 1)
    if date.month == 8 and date. year == 2015:

        df_std2015_08 = pd.concat([df_std2015_08, df_daily_ret.loc[date]], axis = 1)
    if date.month == 9 and date. year == 2015:

        df_std2015_09 = pd.concat([df_std2015_09, df_daily_ret.loc[date]], axis = 1)

    if date.month == 10 and date. year == 2015:

        df_std2015_10 = pd.concat([df_std2015_10, df_daily_ret.loc[date]], axis = 1)

    if date.month == 11 and date. year == 2015:

        df_std2015_11 = pd.concat([df_std2015_11, df_daily_ret.loc[date]], axis = 1)

    if date.month == 12 and date. year == 2015:

        df_std2015_12 = pd.concat([df_std2015_12, df_daily_ret.loc[date]], axis = 1)

    if date.month == 1 and date. year == 2016:

        df_std2016_01 = pd.concat([df_std2016_01, df_daily_ret.loc[date]], axis = 1)

    if date.month == 2 and date. year == 2016:

        df_std2016_02 = pd.concat([df_std2016_02, df_daily_ret.loc[date]], axis = 1)
    if date.month == 3 and date. year == 2016:

        df_std2016_03 = pd.concat([df_std2016_03, df_daily_ret.loc[date]], axis = 1)
df_std = pd.concat([df_std2015_06.transpose().std(),
df_std2015_07.transpose().std(),
df_std2015_08.transpose().std(),
df_std2015_09.transpose().std(),
df_std2015_10.transpose().std(),
df_std2015_11.transpose().std(),
df_std2015_12.transpose().std(),
df_std2016_01.transpose().std(),
df_std2016_02.transpose().std(),
df_std2016_03.transpose().std()],axis = 1)
df_std = df_std.transpose()   #combining the result
#change to index into actual date
df_std ["date"] = ["2015-06", "2015-07", "2015-08", "2015-09", "2015-10", "2015-11", "2015-12", "2016-01", "2016-02", "2016-03"]
df_std = df_std.set_index(df_std["date"])
del df_std["date"]
# redo all the steps for each year
df_std2015 = pd.DataFrame()
df_std2016 = pd.DataFrame()
df_std_yearly = pd.DataFrame()
for date in df_daily_ret.index:
    if date.year == 2015:

        df_std2015 = pd.concat([df_std2015, df_daily_ret.loc[date]], axis = 1)
    if date.year == 2016:

        df_std2016 = pd.concat([df_std2016, df_daily_ret.loc[date]], axis = 1)
df_std_yearly = pd.concat([df_std2015.transpose().std(),
df_std2016.transpose().std()],axis = 1)
df_std_yearly = df_std_yearly.transpose()
df_std_yearly["date"] = ["2015", "2016"]
df_std_yearly = df_std_yearly.set_index(df_std_yearly["date"])
del df_std_yearly["date"]
df_std = pd.concat([df_std, df_std_yearly])
df_std.to_csv("HSI_vol.csv")

#Q7
df_daily_ret_std_resample_monthly = df_daily_ret.resample("M").std()
df_daily_ret_std_resample_yearly = df_daily_ret.resample("Y").std()
# we can concat the two dataframes and output a csv just like before. Steps won't be demonstrated here so we will not have duplicate HSI file

""" most convenient way
df_monthly_ret_sd = df_daily_ret.groupby([df_daily_ret.index.year, df_daily_ret.index.month]).std()
print(df_monthly_ret_sd)
print(df_daily_ret.groupby(df_daily_ret.index.month))
"""
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


"""
#Q6 looping
new_dict ={}
for column in df_daily_ret.columns:

    length = len(df_daily_ret[column].index)

    mean = df_daily_ret[column].mean()
    count = 0
    for element in df_daily_ret[column].values:
        count = count + (element - mean)**2


    new_dict[column] = (count/(length-1))**(1/2) #use N-1 to calulate sample SD

df_daily_ret_std = pd.Series(new_dict)
df_daily_ret_std.to_csv("HSI_vol.csv")


"""
