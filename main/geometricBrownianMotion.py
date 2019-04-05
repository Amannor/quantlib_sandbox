import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)

def get_avg(l):
	return sum(l)/float(len(l))

def get_standardized_normal_dist_samples(mean=0, std=1, numOfSamples=1000):
	if (std == 0):
		 raise ValueError("std=0 isn't supported since there's no way to standardize the result")
	random_normal_dist_samples = np.random.normal(mean,std,(1,numOfSamples))
	# v = np.random.normal(mean,std,(1,n))
	print(f"random_normal_dist_samples before mean fix {random_normal_dist_samples}")
	actual_mean = get_avg(random_normal_dist_samples[0])
	print(f"Expected mean {mean} actual_mean {actual_mean}")
	#Note this still won't make the new mean equal to the given (required) mean! the difference will probably be smaller than 10^-16
	random_normal_dist_samples = random_normal_dist_samples - actual_mean + mean
	
	# print(f"random_normal_dist_samples after mean fix {random_normal_dist_samples}") 
	# mean_after_fix = sum(random_normal_dist_samples[0]) / len(random_normal_dist_samples[0])

	actual_std = np.std(random_normal_dist_samples[0])
	print(f"Expected std {std} actual_std {actual_std}. std/actual_std {std/actual_std}")
	random_normal_dist_samples=random_normal_dist_samples*(std/actual_std)
	# print(f"random_normal_dist_samples after std fix {random_normal_dist_samples}")
	# print(f"std after fix {np.std(random_normal_dist_samples[0])}")
	return random_normal_dist_samples

def getCallOptionReturn(stock_price, strike):
	'''
	Strike is the price at which you have the right to sell the asset
	'''
	return max(stock_price-strike, 0)

def getPutOptionReturn(stock_price, strike):
	'''
	Strike is the price at which you have the right to sell the asset
	'''
	return max(strike-stock_price, 0)


mu=1 #risk-fre interest rate 
n=50
dt=0.1
x0=100
x=pd.DataFrame()
sigma = 1.0 #Stock annualized volatility

random_normal_dist_samples = get_standardized_normal_dist_samples(numOfSamples=n)



# for sigma in np.arange(0.8,2,0.2):
step=np.exp((mu-sigma**2/2)*dt)*np.exp(sigma*random_normal_dist_samples)
cumprodCalc = x0*step.cumprod()
print(f"x0*step.cumprod() {cumprodCalc}")

call_prices = list(map(lambda x: getCallOptionReturn(x, 1), cumprodCalc))
print(f"The average call return is {get_avg(call_prices)}")
# temp=pd.DataFrame(cumprodCalc)
# x=pd.concat([x,temp],axis=1)



# x.columns=np.arange(0.8,2,0.2)
# plt.plot(x)
# plt.legend(x.columns)
# plt.xlabel('t')
# plt.ylabel('X')
# plt.title('Realizations of Geometric Brownian Motion with different variances\n mu=1')
# plt.show()