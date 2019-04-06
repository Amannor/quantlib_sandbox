import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(17) #Todo: run 10K times with different seed s.t. I'll have enough samples to calculate the average on

def get_avg(l):
	return sum(l)/float(len(l))

def get_standardized_normal_dist_samples(mean=0, std=1, num_of_samples=1000):
	"""
	Returning a list of length @num_of_samples of randomly generated numbers with a normal distribution that has the
	given @mean & @std
	"""
	if (std == 0):
		 raise ValueError("std=0 isn't supported since there's no way to standardize the result")
	random_normal_dist_samples = np.random.normal(mean,std,(1,num_of_samples))
	actual_mean = get_avg(random_normal_dist_samples[0])
	#Note this still won't make the new mean equal to the given (required) mean! the difference will probably be smaller than 10^-16
	#Standardizing the mean
	random_normal_dist_samples = random_normal_dist_samples - actual_mean + mean
	
	#Standardizing the std
	actual_std = np.std(random_normal_dist_samples[0])
	random_normal_dist_samples=random_normal_dist_samples*(std/actual_std)
	return random_normal_dist_samples

def getCallOptionReturn(cur_stock_price, strike):
	'''
	Strike is the price at which you have the right to sell the asset
	'''
	return max(cur_stock_price-strike, 0)

def getPutOptionReturn(cur_stock_price, strike):
	'''
	Strike is the price at which you have the right to sell the asset
	'''
	return max(strike-cur_stock_price, 0)

def read_params():
	filename = "input_params_valsFromOldBS.json"
	with open(filename, 'r') as f:
	    dict_from_file = json.load(f)
	initial_stock_price = dict_from_file['initial_stock_price']
	strike_price = dict_from_file['strike_price']
	risk_free_interest_rate = dict_from_file['risk_free_interest_rate']
	stock_annualized_volatility = dict_from_file['stock_annualized_volatility']  #Todo: calaculte this according to what Nitay A. suggested
	time_span_in_years = dict_from_file['time_span_in_years']
	return initial_stock_price, strike_price, risk_free_interest_rate, stock_annualized_volatility, time_span_in_years

initial_stock_price, strike_price, mu, sigma, dt = read_params()
n=1000000
random_normal_dist_samples = get_standardized_normal_dist_samples(num_of_samples=n)



#Todo: Nitay suggested that I'll do cumsum(on random_normal_dist_samples...?) in this stage instead of cumprod after the exponent ince it'll be more accurate
step=np.exp((mu-sigma**2/2)*dt)*np.exp(sigma*random_normal_dist_samples) 
# cumprodCalc = initial_stock_price*step.cumprod()
cumprodCalc = initial_stock_price*step[0]
# print(f"initial_stock_price*step {cumprodCalc}")

estimated_stock_price = get_avg(cumprodCalc)
print(f"get_avg(cumprodCalc) {get_avg(cumprodCalc)}")

call_prices = list(map(lambda x: getCallOptionReturn(x, strike_price), cumprodCalc))
print(f"The average call return is {get_avg(call_prices)}")

put_prices = list(map(lambda x: getPutOptionReturn(x, strike_price), cumprodCalc))
print(f"The average put return is {get_avg(put_prices)}")