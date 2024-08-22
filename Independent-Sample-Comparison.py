'''
Suppose a website owner claims that there is no difference in the average time spent on their
website between desktop and mobile users. To test this claim, we collect data from 30
desktop users and 30 mobile users regarding the time spent on the website in minutes. The
sample statistics are as follows:
desktop_users = [12, 15, 18, 16, 20, 17, 14, 22, 19, 21, 23, 18, 25, 17, 16, 24, 20, 19, 22, 18, 15,14, 23, 16, 12, 21, 19, 17, 20, 14]
mobile_users = [10, 12, 14, 13, 16, 15, 11, 17, 14, 16, 18, 14, 20, 15, 14, 19, 16, 15, 17, 14, 12,11, 18, 15, 10, 16, 15, 13, 16, 11]

○ Sample size (n1): 30
○ Sample mean (mean1): 18.5 minutes
○ Sample standard deviation (std_dev1): 3.5 minutes
Desktop users:

○ Sample size (n2): 30
○ Sample mean (mean2): 14.3 minutes
○ Sample standard deviation (std_dev2): 2.7 minutes
Mobile users:

We will use a significance level of 0.05 for the hypothesis test.
'''

### Checking normality using the shapiro will test.

from scipy.stats import shapiro
from scipy.stats import levene
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from numpy.random import normal
import seaborn as sns
from scipy.stats import t


desktop_users = [12, 15, 18, 16, 20, 17, 14, 22, 19, 21, 23, 18, 25, 17, 16, 24, 20, 19, 22, 18, 15,14, 23, 16, 12, 21, 19, 17, 20, 14]
mobile_users = [10, 12, 14, 13, 16, 15, 11, 17, 14, 16, 18, 14, 20, 15, 14, 19, 16, 15, 17, 14, 12,11, 18, 15, 10, 16, 15, 13, 16, 11]

if((shapiro(desktop_users).pvalue>0.05) and (shapiro(mobile_users).pvalue>0.05)):
    print("Normal Distribution Verified...proceeding to check equality of variances")

#Checking normality using the shapiro will test.

if(levene(desktop_users,mobile_users).pvalue>0.05):
    print("variance check passed....proceeding to perform t-test for dual independent samples ")
else:
    print("Variance check failed")

t_statistic= (14.3-18.5)/np.sqrt((2.7**2)/30+(3.5**2)/30)
p_value=t.cdf(t_statistic,58)

if(2*p_value<0.05):
    print("Both observations are not similar ")
else:
    print("Both observations are similar")

