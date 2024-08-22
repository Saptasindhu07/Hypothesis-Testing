import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import t
import math

'''
Suppose a manufacturer claims that the average weight of their new chocolate bars is something he input,
we highly doubt that and want to check this so we drew out a sample of input chocolate
bars and measured their weight, the sample mean came out to be something he input in your program along with the sample
std deviation. Consider the significance level to be 0.05. Check how true/false claim is.
'''

claim= float(input("Enter your claim weight- "))
sample_size=int(input("Enter Sample Size- "))
experimental_mean_weight=float(input("Mean weight from experiment- "))
experimental_std= float(input("Experimental standard deviation- "))

#Null hypothesis- Claim is correct.

if(claim>experimental_mean_weight):
    t_statistic=(experimental_mean_weight-claim)/(experimental_std/math.sqrt(sample_size))
    degreeoffreedom=sample_size-1
    cdf_value=t.cdf(t_statistic,degreeoffreedom)
    print("CDF= ",cdf_value*2)
    if(2*cdf_value<0.05):
        print("Claim is FALSE")
    else:
        print("Claim is TRUE")
else:
    t_statistic=(claim-experimental_mean_weight)/(experimental_std/math.sqrt(sample_size))
    degreeoffreedom=sample_size-1
    cdf_value=t.cdf(t_statistic,degreeoffreedom)
    print("CDF= ",cdf_value*2)
    if(2*cdf_value<0.05):
        print("Claim is FALSE")
    else:
        print("Claim is TRUE")
    
