'''
Created on Jan 28, 2017

@author: angelddaz
'''
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
from IPython.core.display import HTML, display
import matplotlib.pyplot as plt
import numpy as np 

df_adv = pd.read_csv(r'http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
X = df_adv[['TV', 'Radio']]
y = df_adv['Sales']
#print(df_adv.head())   #make sure everything's all there

#method1:
X = sm.add_constant(X)
est = sm.OLS(y, X).fit()
#print est.summary()

#method2: formula= response ~ predictor + predictor
est = smf.ols(formula='Sales ~ TV + Radio', data=df_adv).fit()
#print est.summary()

'''
handling categorical variables
e.g. geographic region
'''
df = pd.read_csv(r'http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data', index_col=0)
X = df.copy()
y = X.pop('chd')

y.groupby(X.famhist).mean()

#changing categories into numeric variables
df['famhist_ord'] = pd.Categorical(df.famhist).codes
est = smf.ols(formula="chd ~ famhist_ord", data=df).fit()

#statsmodels used to create a k-level categorical variable into k-1 binary variables

#coeff summary
def short_summary(est):
    return display(HTML(est.summary().tables[1].as_html()))

#fit OLS on categorical variables
est = smf.ols(formula='chd ~ C(famhist)', data=df).fit()
#couldn't figure out how to display HTML in eclipse
#not yet at least
#short_summary(est)

'''
Polynomial regression:
Boston housing dataset

We’ll look into the task to predict median house values in the Boston area 
using the predictor lstat, defined as the “proportion of the adults without 
some high school education and proportion of male workes classified as laborers.
'''

df = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/MASS/Boston.csv')
#plot lstat (lower status of the pop) against median value
plt.figure(figsize=(6 * 1.618, 6))
plt.scatter(df.lstat, df.medv, s=10, alpha=0.3)
plt.xlabel('lstat')
plt.ylabel('medv')

#points linearly space on lstats
x = pd.DataFrame({'lstat': np.linspace(df.lstat.min(), df.lstat.max(), 100)})

#1st order polynomial
poly_1 = smf.ols(formula='medv ~ 1 + lstat', data=df).fit()
plt.plot(x.lstat, poly_1.predict(x), 'b-', label='Poly n=1 $R^2$=%.2f' % poly_1.rsquared, alpha=0.9)

#2nd order polynomial
poly_2 = smf.ols(formula='medv ~ 1 + lstat + I(lstat ** 2.0)', data=df).fit()
plt.plot(x.lstat, poly_2.predict(x), 'g-', label='Poly n=2 $R^2$=%.2f' % poly_2.rsquared, alpha=0.9)

#3rd order polynomial
poly_3 = smf.ols(formula='medv ~ 1 + lstat + I(lstat ** 2.0) + I(lstat ** 3.0)', data=df).fit()
plt.plot(x.lstat, poly_3.predict(x), 'r-', alpha=0.9, label='Poly n=3 $R^2$=%.2f' % poly_3.rsquared)

plt.legend()

plt.show()
