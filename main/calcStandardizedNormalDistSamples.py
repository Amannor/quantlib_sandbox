import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)

def get_standardized_normal_dist_samples(mean=0, std=1, numOfSamples=10):
	if (std == 0):
		 raise ValueError("std=0 isn't suppoerted since there's no way to standardize the result")
	random_normal_dist_samples = np.random.normal(mean,std,(1,numOfSamples))
	# v = np.random.normal(mean,std,(1,n))
	print(f"random_normal_dist_samples before mean fix {random_normal_dist_samples}")
	actual_mean = sum(random_normal_dist_samples[0]) / len(random_normal_dist_samples[0])
	print(f"Expected mean {mean} actual_mean {actual_mean}")
	#Note this still won't make the new mean equal to the given (required) mean! the difference will probably be smaller than 10^-16
	random_normal_dist_samples = random_normal_dist_samples - actual_mean + mean
	
	# print(f"random_normal_dist_samples after mean fix {random_normal_dist_samples}") 
	# mean_after_fix = sum(random_normal_dist_samples[0]) / len(random_normal_dist_samples[0])

	actual_std = np.std(random_normal_dist_samples[0])
	print(f"Expected std {std} actual_std {actual_std}. std/actual_std {std/actual_std}")
	random_normal_dist_samples=random_normal_dist_samples*(std/actual_std)
	print(f"random_normal_dist_samples after std fix {random_normal_dist_samples}")
	print(f"std after fix {np.std(random_normal_dist_samples[0])}")


get_standardized_normal_dist_samples(std=0)