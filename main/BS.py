# import QuantLib as ql # version 1.5
# import matplotlib.pyplot as plt
# %matplotlib inline
import QuantLib as ql 
# import QuantLib-Python as ql #

print ("Hello world")
date = ql.Date(31, 3, 2015)
print(date)

# option data
maturity_date = ql.Date(15, 1, 2016)
spot_price = 100#127.62
strike_price = 120#130
volatility = 0.2 #0.20 # the historical vols for a year
dividend_rate =  0.02#0.0163
option_type = ql.Option.Call

risk_free_rate = 0.04#0.001
day_count = ql.Actual365Fixed()
calendar = ql.UnitedStates()

calculation_date = ql.Date(8, 5, 2015)
ql.Settings.instance().evaluationDate = calculation_date

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
bs_price = european_option.NPV()
print (f"The theoretical price is {bs_price}")