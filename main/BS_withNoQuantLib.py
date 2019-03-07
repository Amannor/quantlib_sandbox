import math
import scipy.stats


I_Vol = 0.2
Rate = 0.04
Div = 0.02

Spot = 1
T_Mat = 1

FWD = math.exp((Rate-Div)*T_Mat)


Strike = 1.2
     #(1/  (I_VOL*SQRT(T_Mat)) )  *(LN(Spot/Strike)      + (Rate-Div+0.5*I_VOL^2)         *T_Mat)
d_1 = (1/(I_Vol*math.sqrt(T_Mat)))*(math.log(Spot/Strike) + Rate-Div+0.5*math.pow(I_Vol,2)*T_Mat) 
    #=d_1-I_VOL*SQRT(T_Mat)
d_2 = d_1-I_Vol*math.sqrt(T_Mat)

		  #=EXP(-Rate*T_Mat)*(FWD*NORMDIST(d_1,0,1,TRUE)-Strike*NORMDIST(d_2,0,1,TRUE))
# Call_Price = 
# Put_Price

# C_P_P

# Delta

# Gamma

# Vega

# Theta

print(f"FWD: {FWD} d_1 {d_1} d_2 {d_2}")
