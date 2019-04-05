import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mu=1
n=5
dt=0.1
x0=100
x=pd.DataFrame()
np.random.seed(1)

for sigma in np.arange(0.8,2,0.2):
	print(f"sigma {sigma}")
	step=np.exp((mu-sigma**2/2)*dt)*np.exp(sigma*np.random.normal(0,np.sqrt(dt),(1,n)))
	print(f"step {step}")
	temp=pd.DataFrame(x0*step.cumprod())
	print(f"temp {temp}")
	x=pd.concat([x,temp],axis=1)
	print(f"x {x}")

x.columns=np.arange(0.8,2,0.2)
plt.plot(x)
plt.legend(x.columns)
plt.xlabel('t')
plt.ylabel('X')
plt.title('Realizations of Geometric Brownian Motion with different variances\n mu=1')
plt.show()