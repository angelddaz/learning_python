'''
Created on Feb 28, 2017

@author: angelddaz
'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.io.stata.read_stata(r"C:\Users\angelddaz\OneDrive\School\17sp\ECON342\group_project\bwght2.dta")
data.to_csv(r"C:\Users\angelddaz\OneDrive\School\17sp\ECON342\group_project\bwght2.csv")
df = pd.read_csv(r"C:\Users\angelddaz\OneDrive\School\17sp\ECON342\group_project\bwght2.csv")
#yay now a stata file is a pandas dataframe

print df.columns
plt.scatter(df.mage, df.fage)
plt.xlabel("mothers age")
plt.ylabel("fathers age")
plt.show()

plt.scatter(df.meduc, df.bwght)
plt.xlabel("mothers educ")
plt.ylabel("baby weight")
plt.show()

plt.scatter(df.meduc, df.omaps)
plt.xlabel("mothers educ")
plt.ylabel("baby 1minScore")
plt.show()

plt.scatter(df.meduc, df.fmaps)
plt.xlabel("mothers educ")
plt.ylabel("baby 5minScore")
plt.show()