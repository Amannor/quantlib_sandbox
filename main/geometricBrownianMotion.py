#!/usr/bin/python

import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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

def calc_prices(random_seed):
	initial_stock_price, strike_price, mu, sigma, T = read_params()
	n=100000
	dt = T/n
	np.random.seed(random_seed)
	random_normal_dist_samples = get_standardized_normal_dist_samples(num_of_samples=n)[0] #We take [0] because the return object is an array of size 1 with the desired list as its memeber

	#Todo: Nitay suggested that I'll do cumsum(on random_normal_dist_samples...?) in this stage instead of cumprod after the exponent ince it'll be more accurate
	series_formula = (mu-sigma**2/2)*dt + sigma*random_normal_dist_samples
	series_cumsum = series_formula.cumsum()
	estimated_stock_price_series = initial_stock_price * np.exp(series_cumsum)
	estimated_stock_price = estimated_stock_price_series[-1]

	estimated_call_price = getCallOptionReturn(estimated_stock_price, strike_price)
	estimated_put_price = getPutOptionReturn(estimated_stock_price, strike_price)

	return estimated_stock_price, estimated_call_price, estimated_put_price

# def main():
# 	seed =  int(sys.argv[1])
# 	print(f"Seed {seed}")
# 	np.random.seed(seed) #Todo: run 10K times with different seed s.t. I'll have enough samples to calculate the average on
# 	return calc_prices()


# if __name__ == '__main__':
#     main()
