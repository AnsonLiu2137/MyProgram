import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt
#Q1
equity = pd.read_excel("/Users/ansonliu/Downloads/HW2.xlsx", "equity", index_col = 0, parse_dates = True)
factor = pd.read_excel("/Users/ansonliu/Downloads/HW2.xlsx", "factor", index_col = 0, parse_dates = True)
equity_np = equity.to_numpy()
factor_np = factor.to_numpy()
dif_equity = np.diff(equity_np, axis = 0)
equity_np_no_last = np.delete(equity_np, -1, 0)
return_equity = dif_equity/equity_np_no_last
dif_factor = np.diff(factor_np, axis = 0)
factor_np_no_last = np.delete(factor_np, -1, 0)
return_factor = dif_factor/factor_np_no_last

#Q2
reqExp = 0.8
reqCorr = 0.4
reqFcorr = 0.7

#Q3
return_equity_cov = np.cov(np.transpose(return_equity))



w_equity, v_equity = np.linalg.eig(return_equity_cov)

#w_equity: eigenvalue v_equity = eigenvector
sum = 0
num_factor = 0
for i in -np.sort(-w_equity):
    sum = sum + i/np.sum(w_equity)

    num_factor = num_factor + 1
    if sum >= reqExp:
        break


# minimum numer of principal components to cover the reqExp = num_factor = 3
#Q4

pc1 = v_equity[:,0]
pc2 = v_equity[:,1]
pc3 = v_equity[:,2]


pc1 = np.dot(return_equity, pc1)
pc2 = np.dot(return_equity, pc2)
pc3 = np.dot(return_equity, pc3)
lst1 = []
lst2 = []
lst3 = []



for i in range(24):
    flag = True
    rss = stats.pearsonr(pc1, return_factor[:,i])
    if abs(rss.statistic) >= reqCorr and len(lst1) == 0:
        lst1.append(i)
    if abs(rss.statistic) > reqCorr:
        for j in lst1:
            rss_inner = stats.pearsonr(return_factor[:,i], return_factor[:,j])
            if abs(rss_inner.statistic) > reqFcorr:
                flag = False


    if flag == True and abs(rss.statistic) > reqCorr:
        lst1.append(i)

# element in lst are just index number of the factor in spreadsheet [factor]
for i in range(24):
    rss = stats.pearsonr(pc2, return_factor[:,i])
    if -(i in lst1) and abs(rss.statistic) > reqCorr:
        for element in lst1:
            rss_inner = stats.pearsonr(return_factor[:,element], return_factor[:,i])
            if rss_inner > reqFcorr:
                break
        lst1.append(i)

for i in range(24):
    rss = stats.pearsonr(pc3, return_factor[:,i])
    if -(i in lst1) and abs(rss.statistic) > reqCorr:
        for element in lst1:
            rss_inner = stats.pearsonr(return_factor[:,element], return_factor[:,i])
            if rss_inner > reqFcorr:
                break
        lst1.append(i)


#Q5
arr = np.empty([133,10])
count = 0
for element in lst1:

    arr[:,count] =(return_factor[:, element] - np.mean(return_factor[:, element])) / np.std(return_factor[:, element])
    count = count + 1

    #for j in range(len(return_factor[:,element])):
        #return_factor[:,element][j] = (return_factor[:,element][j] - np.mean(return_factor[:,element]))/np.std(return_factor[:,element])

    #arr = np.concatenate(arr, (return_factor[:,element]-np.mean(return_factor[:,element]))/np.std(return_factor[:,element]))

for column in range(return_equity.shape[1]):
    return_equity[:,column] = (return_equity[:,column] - np.mean(return_equity[:,column]))/np.std(return_equity[:,column])

#return_equity has been standardized

#Q6
arr = sm.add_constant(arr)

beta = []
t_value =[]
r_square = []
for column in range(return_equity.shape[1]):
    result = sm.OLS(return_equity[:,column], arr).fit()
    beta.append(result.params)
    t_value.append(result.tvalues)
    r_square.append(result.rsquared)
r_square_df = pd.DataFrame(columns = list(equity.head(0)))
r_square_df.loc[0] = r_square

t_value_df = pd.DataFrame(columns = list(equity.head(0)))
t_value_df.loc[0] = t_value

r_square_df.to_csv("R_square")
t_value_df.to_csv("t_value")
#beta, t_value and r_square are the lists containing the relevant value
#print(return_factor[:,0].shape) 133
#print(len(lst1)) 10














