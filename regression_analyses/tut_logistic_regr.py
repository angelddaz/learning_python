'''
Created on Feb 4, 2017

@author: angelddaz
logistic regression bitches.
http://nbviewer.jupyter.org/github/justmarkham/DAT8/blob/master/notebooks/12_logistic_regression.ipynb
'''
import pandas as pd
#from Cython.Shadow import inline

url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data'
#reminder to self: check out this url later for possible databases to mess with
col_names = ['id', 'ri', 'na', 'mg', 'al', 'si', 'k', 'ca', 'ba', 'fe', 'glass_type']
glass = pd.read_csv(url, names=col_names, index_col='id')
glass.sort_values(by='al', inplace=True)
#print glass.head()

'''
#linear regression using seaborn
import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
sns.set(font_scale=1.5)
sns.lmplot(x='al', y='ri', data=glass, ci=None)
plt.show()
'''
import matplotlib.pyplot as plt
#scatter plot using pandas
glass.plot(kind='scatter', x='al', y='ri', marker='o')
#plt.show()

#scatter plot using Matplotlib
#plt.scatter(glass.al, glass.ri)
#plt.xlabel('al')
#plt.ylabel('ri')
#plt.show()

#fit a linear regression model
from sklearn.linear_model import LinearRegression
linreg = LinearRegression()
feature_cols = ['al']
X = glass[feature_cols]
y = glass.ri
linreg.fit(X, y)
#make predictions for all values of X
glass['ri_pred'] = linreg.predict(X)
plt.plot(glass.al, glass.ri_pred, color='red')
plt.xlabel('al')
plt.ylabel('Predicted ri')
plt.title('FIRST ONE')
plt.show()

#print linreg.coef_   
#print linreg.intercept_

#Now that the linear regression tutorial is over.
#Predicting a categorical response
glass.glass_type.value_counts().sort_index()
#This creates a new column with the dummy variable to classify 
#1: household, 0:not household
glass['household'] = glass.glass_type.map({1:0, 2:0, 3:0, 5:1, 6:1, 7:1})
#print glass.head()

plt.scatter(glass.al, glass.household)
plt.xlabel('al')
plt.ylabel('household')
plt.grid()
#a linear regression model to store the predictions
feature_cols = ['al']
X = glass[feature_cols]
y = glass.household
linreg.fit(X, y)
glass['household_pred'] = linreg.predict(X)
#scatter plot that includes the regression line
plt.plot(glass.al, glass.household_pred, color='red')
plt.title('SECOND ONE')

plt.show()

# np.where returns the first value if the condition is True
# and the second value if the condition is False
import numpy as np
#adding a column of classifying predictions 

glass['household_pred_class'] = np.where(glass.household_pred >= 0.5, 1, 0)
plt.scatter(glass.al, glass.household)
plt.plot(glass.al, glass.household_pred_class, color='red')
plt.xlabel('al')
plt.ylabel('household')
plt.grid()
plt.title('THIRD ONE')

plt.show()

#PART 3: Using logistic regression instead
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(C=1e9)
feature_cols = ['al']
X = glass[feature_cols]
y = glass.household
logreg.fit(X,y)
glass['household_pred_class'] = logreg.predict(X)

#plot the class predictions
plt.scatter(glass.al, glass.household)
plt.plot(glass.al, glass.household_pred_class, color='red')
plt.xlabel('al')
plt.ylabel('household')
plt.grid()
plt.title('FOURTH ONE')

plt.show()

#store the predicted probability of class 1
glass['household_pred_prob'] = logreg.predict_proba(X)[:,1]

#plotting predicted probabilities
plt.scatter(glass.al, glass.household)
plt.plot(glass.al, glass.household_pred_prob, color='red')
plt.xlabel('al')
plt.ylabel('household')
plt.grid()
plt.title('FIFTH ONE')

plt.show()


#PART 4: Probability, odds, e, log, log-odds
# create a table of probability versus odds
table = pd.DataFrame({'probability':[0.1, 0.2, 0.25, 0.5, 0.6, 0.8, 0.9]})
table['odds'] = table.probability/(1 - table.probability)
# add log-odds to the table
table['logodds'] = np.log(table.odds)
print table

# compute predicted log-odds for al=2 using the equation
logodds = logreg.intercept_ + logreg.coef_[0] * 2
print logodds

'''
Bottom line: Positive coefficients increase the log-odds of 
the response (and thus increase the probability), and negative 
coefficients decrease the log-odds of the response (and thus 
decrease the probability).
'''
# examine the intercept
print logreg.intercept_
#Interpretation: For an 'al' value of 0, the log-odds of 'household' is -7.71.

'''
Logistic regression can still be used with categorical features. 
Let's see what that looks like:
'''
glass['high_ba'] = np.where(glass.ba > 0.5, 1, 0)
# original (continuous) feature
import seaborn as sns
sns.lmplot(x='ba', y='household', data=glass, ci=None, logistic=True)
sns.plt.show()
sns.lmplot(x='high_ba', y='household', data=glass, ci=None, logistic=True)
sns.plt.show()
#categorical feature, with jitter added
sns.lmplot(x='high_ba', y='household', data=glass, ci=None, logistic=True,
           x_jitter=0.05, y_jitter=0.05)
sns.plt.show()
#fit a logistic regression model
feature_cols = ['high_ba']
X = glass[feature_cols]
y = glass.household
print logreg.fit(X, y)

print zip(feature_cols, logreg.coef_[0])