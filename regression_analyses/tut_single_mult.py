'''
Created on Jan 28, 2017

@author: angelddaz
'''

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)

#scatter plots
fig, axs = plt.subplots(1, 3, sharey=True)
data.plot(kind='scatter', x='TV', y='Sales', ax=axs[0], figsize=(16, 8))
data.plot(kind='scatter', x='Radio', y='Sales', ax=axs[1])
data.plot(kind='scatter', x='Newspaper', y='Sales', ax=axs[2])
#plt.show()

#creating a fitted model in one line
lm = smf.ols(formula='Sales ~ TV', data=data).fit()
#print(lm.params) #printing coefficients

#manual sales prediction:
#print(7.032594+0.047537*50) #50,000 TV ad spend
#statsmodels formula prediction with a new dataframe
#x_new = pd.DataFrame({'TV': [50]})
#print(lm.predict(x_new))

#plotting the least squares line
#step1: create a df with min and max values of dependent value
x_new = pd.DataFrame({'TV': [data.TV.min(), data.TV.max()]})

#step2: make preds for these two x values
preds = lm.predict(x_new)

#step3: plot observed data
data.plot(kind='scatter', x='TV', y='Sales')

#step4: plot the ols line
plt.plot(x_new, preds, c='red',linewidth=2)
plt.show()

#print(str(lm.conf_int()) + "\n") #same can be done with rsquared, pvalues.

'''
Multiple Linear Regression
y = Beta0 + Beta_1*x_1 + ... + Beta_n*x_n
'''

#a fitted model with all three coefficients
lm = smf.ols(formula='Sales ~ TV + Radio + Newspaper', data=data).fit()
'''
print(lm.params)
print(lm.summary())
'''

#removing Newspaper, which has a high pvalue and is statistically irrelevant to sales
lm = smf.ols(formula='Sales ~ TV + Radio', data=data).fit()
#print(lm.summary())

'''models in scikit-learn'''
#step1: create x and y
feature_cols = ['TV', 'Radio', 'Newspaper']
X = data[feature_cols]
y = data.Sales

#step2: create the regression. print intercept and coeffs
lm = LinearRegression()
lm.fit(X, y)

#print lm.intercept_
#print lm.coef_

#step3: pair the names with the coeffs
zip(feature_cols, lm.coef_)

#predicting for x1, x2, x3
#lm.predict([100, 25, 25])

#step4: calculate the R-squared
lm.score(X, y)

#NOTE: pvals and conf intervals are not easily accessible through scikitlearn

'''
Handling Categorical Predictors with Two categories i.e. Small, Large
'''
#step1: set a seed for reproducibility
np.random.seed(12345)

#step2: create a series of booleans in which roughly half are True
nums = np.random.rand(len(data))
mask_large = nums > 0.5

#step3: set Size to small and then change roughly half to be large
data['Size'] = 'small'
data.loc[mask_large, 'Size'] = 'large'

#step4: because data needs to be represented numerically, two categories can be
#changed into a dummy variable as a binary value

data['IsLarge'] = data.Size.map({'small':0, 'large':1})

#step5: Redo mult linear regression including dummy variable

#step5a: create X and y
feature_cols = ['TV', 'Radio', 'Newspaper', 'IsLarge']
X = data[feature_cols]
y = data.Sales

#step5b: instantiate linear regression and fit
lm = LinearRegression()
lm.fit(X, y)

#step5c: merge coeffs labels and data. PRINT results:
#print(feature_cols, lm.coef_)

'''
More than Two Categories for a variable
EX: rural, suburban, urban
'''

np.random.seed(123456)

#assigning roughly one third of observations to each group
nums = np.random.rand(len(data))
mask_suburban = (nums > 0.33) & (nums < 0.66)
mask_urban = nums > 0.66
data['Area'] = 'rural'
data.loc[mask_suburban, 'Area'] = 'suburban'
data.loc[mask_urban, 'Area'] = 'urban'

#check if its right
#print data.head()

#step1: create 3 dummy variables using get_dummies and then exclude the first dummy col
area_dummies = pd.get_dummies(data.Area, prefix='Area').iloc[:, 1:]

#step2: concat the dummy variable cols onto the original df (axis=0 means rows)
#in general you need k-1 dummy variables for k categories. 2 categories means 1 dummy variable.
data = pd.concat([data, area_dummies], axis=1)
#check your work
#print data.head()

#step3a: create X and y
feature_cols = ['TV', 'Radio', 'Newspaper', 'IsLarge', 'Area_suburban', 'Area_urban']
X = data[feature_cols]
y = data.Sales

#step3b: instantiate, fit
lm = LinearRegression()
lm.fit(X, y)

#step3c: merge and print coeffs
print(zip(feature_cols, lm.coef_))