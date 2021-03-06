# Taken from: http://gouthamanbalaraman.com/blog/european-option-binomial-tree-quantlib-python.html
import QuantLib as ql 
from math import *

# option data
maturity_date = ql.Date(15, 1, 2016)
spot_price = 100#127.62
strike_price = 120#130
volatility = 0.2 #0.20 # the historical variance for a year
dividend_rate =  0.02#0.0163

risk_free_rate = 0.04#0.001 
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

calculation_date = ql.Date(15, 1, 2015)#ql.Date(8, 5, 2015)  
ql.Settings.instance().evaluationDate = calculation_date

option_type = ql.Option.Call

# construct the European Option
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff, exercise)


#The Black-Scholes-Merto process is constructed here.
spot_handle = ql.QuoteHandle(
    ql.SimpleQuote(spot_price)
)
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, risk_free_rate, day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, dividend_rate, day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date, calendar, volatility, day_count)
)
bsm_process = ql.BlackScholesMertonProcess(spot_handle, 
                                           dividend_yield, 
                                           flat_ts, 
                                           flat_vol_ts)

european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_call_price = european_option.NPV()
print (f"The theoretical price (call) is {bs_call_price:.2f}")


option_type = ql.Option.Put

# construct the European Option
payoff = ql.PlainVanillaPayoff(option_type, strike_price)
exercise = ql.EuropeanExercise(maturity_date)
european_option = ql.VanillaOption(payoff, exercise)


#The Black-Scholes-Merto process is constructed here.
spot_handle = ql.QuoteHandle(
    ql.SimpleQuote(spot_price)
)
flat_ts = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, risk_free_rate, day_count)
)
dividend_yield = ql.YieldTermStructureHandle(
    ql.FlatForward(calculation_date, dividend_rate, day_count)
)
flat_vol_ts = ql.BlackVolTermStructureHandle(
    ql.BlackConstantVol(calculation_date, calendar, volatility, day_count)
)
bsm_process = ql.BlackScholesMertonProcess(spot_handle, 
                                           dividend_yield, 
                                           flat_ts, 
                                           flat_vol_ts)

european_option.setPricingEngine(ql.AnalyticEuropeanEngine(bsm_process))
bs_put_price = european_option.NPV()
print (f"The theoretical price is (put) {bs_put_price:.2f}")

#=    Spot      *EXP((Rate          -Div          )*T_Mat)
T_Mat = round(ql.Actual360().yearFraction(calculation_date,maturity_date)) #The round function was added because otherwise T_Mat would be 1.01..
FWD = (spot_price*exp((risk_free_rate-dividend_rate)*T_Mat))
C_P_P = FWD-spot_price-bs_call_price+bs_put_price

print(f"FWD {FWD:.8f} C_P_P {C_P_P:.3f}")

