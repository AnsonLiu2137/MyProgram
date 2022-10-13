import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, gaussian_kde, t, laplace

data = pd.read_excel ("/Users/ansonliu/Desktop/CUHK Yr4 Term1/FINA4380/700HK.xlsx",index_col=0, parse_dates=True)
data.index = pd.to_datetime(data.index)
data_new = data.pct_change().dropna(how="all")
data_new = np.log(data/data.shift()).dropna(how="all")
data_new.dropna(axis=1, how="all", inplace=True)

mu = data_new.mean()[0]
sig = data_new.std()[0]

yRet=np.array(data_new)
plt.show(block=True)
plt.subplot(221)

plt.title("Fig.1.1a")
plt.hist(yRet,density=True, bins=100, color="grey")
distance = np.linspace(min(yRet), max(yRet))
plt.plot(distance, norm.pdf(distance, mu, sig), color="red",label="pdf")
plt.ylabel("density")
plt.legend(loc="upper right", fontsize=8)

plt.subplot(222)
plt.title('Fig.1.2b. Using Gaussian Kernel to represent empirical returns', fontsize=8)
yNRet = (yRet-mu)/sig
distanceN = np.squeeze(np.linspace(min(yNRet), max(yNRet)))
kernel = gaussian_kde(np.squeeze(yNRet))
plt.plot(distanceN, norm.pdf(distanceN, 0, 1), label='Normal')
plt.plot(distanceN, kernel(distanceN), label='empirical')
plt.legend(loc='upper right', fontsize=8)

plt.subplot(223)
plt.title('Fig.1.2c Adding the Student t-destiny', fontsize=8)
plt.plot(distanceN, norm.pdf(distanceN, 0, 1), label='Normal')
plt.plot(distanceN, kernel(distanceN), label='empirical')

plt.plot(distanceN, t.pdf(distanceN, 3), label='t-dist, df=3')
plt.legend(loc='upper right', fontsize=8)

plt.subplot(224)
plt.title('Fig.1.2d Adding Laplace density', fontsize=8)
plt.plot(distanceN, norm.pdf(distanceN, 0, 1), label='Normal')
plt.plot(distanceN, kernel(distanceN), label='empirical')
plt.plot(distanceN, t.pdf(distanceN, 3), label='t-dist, df=3')
plt.plot(distanceN, laplace.pdf(distanceN), label='laplace-dist')
plt.legend(loc='upper right', fontsize=8)
plt.show(block=True)



