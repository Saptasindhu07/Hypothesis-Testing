import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.random import normal
import seaborn as sns
from scipy.stats import chi2


'''
Suppose we have a six-sided fair die, and we want to test if the die is indeed fair. We roll the
die 60 times and record the number of times each side comes up. We'll use the Chi-Square
Goodness-of-Fit test to determine if the observed frequencies are consistent with a fair die
(i.e., a uniform distribution of the sides).
Observed frequencies:
○ Side 1: 12 times
○ Side 2: 8 times
○ Side 3: 11 times
○ Side 4: 9 times
○ Side 5: 10 times
○ Side 6: 10 times
'''
observed=[]
expected=10
for i in range(6):
    input_=int(input("Enter side count: "))
    observed.append(input_)

statistic=0
for i in range(0,6):
    statistic+=((observed[i]-expected)**2)/expected

cdf=chi2.cdf(statistic,5)
pValue=1-cdf
if(pValue<0.05):
    print("P-Value is ",pValue," and so Null Hypothesis Overthrown")
else:
    print("P-Value is ",pValue," and so Null Hypothesis stands")