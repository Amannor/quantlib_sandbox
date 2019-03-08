""" Taken from: http://janroman.dhis.org/stud/I2014/BS2/BS_Daniel.pdf
Calculating the partial derivatives for a Black Scholes Option (Call)
# S - Stock price
# K - Strike price
# T - Time to maturity
# r - Riskfree interest rate
# d - Dividend yield
# v - Volatility
Return:
Delta: partial wrt S
Gamma: second partial wrt S
Theta: partial wrt T
Vega: partial wrt v
Rho: partial wrt r """
from scipy.stats import norm
from math import *

def Black_Scholes_Greeks_Call(S, K, r, v, T, d):
	T_sqrt = sqrt(T)
	d1 = (log(float(S)/K)+((r-d)+v*v/2.)*T)/(v*T_sqrt)
	d2 = d1-v*T_sqrt
	Delta = norm.cdf(d1)
	Gamma = norm.pdf(d1)/(S*v*T_sqrt)
	Theta =- (S*v*norm.pdf(d1))/(2*T_sqrt) - r*K*exp( -r*T)*norm.cdf(d2)
	Vega = S * T_sqrt*norm.pdf(d1)
	Rho = K*T*exp(-r*T)*norm.cdf(d2)
	return Delta, Gamma, Theta, Vega, Rho


I_Vol = 0.2
Rate = 0.04
Div = 0.02
Spot = 1
T_Mat = 1
Strike = 1.2

bs_greeks_call = list(map(lambda x: f"{x*100:.2f}%", Black_Scholes_Greeks_Call(Spot, Strike, Rate, I_Vol, T_Mat, Div)))
delta, gamma, theta, vega, rho = bs_greeks_call
print(f"Greeks (call): Delta {delta}, Gamma {gamma}, Theta {theta}, Vega {vega}, Rho {rho}")



def Black_Scholes_Greeks_Put(S, K, r, v, T, d):
	T_sqrt = sqrt(T)
	d1 = (log(float(S)/K)+((r-d)+v*v/2.)*T)/(v*T_sqrt)
	d2 = d1-v*T_sqrt
	Delta = norm.cdf(d1)-1
	Gamma = norm.pdf(d1)/(S*v*T_sqrt)
	Theta =- (S*v*norm.pdf(d1))/(2*T_sqrt) + r*K*exp( -r*T)*norm.cdf(d2)
	Vega = S * T_sqrt*norm.pdf(d1)
	Rho = -K*T*exp(-r*T)*norm.cdf(d2*(-1))
	return Delta, Gamma, Theta, Vega, Rho

bs_greeks_put = list(map(lambda x: f"{x*100:.2f}%", Black_Scholes_Greeks_Put(Spot, Strike, Rate, I_Vol, T_Mat, Div)))
delta, gamma, theta, vega, rho = bs_greeks_put
print(f"Greeks (put): Delta {delta}, Gamma {gamma}, Theta {theta}, Vega {vega}, Rho {rho}")