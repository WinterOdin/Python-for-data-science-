
import numpy as np
import pandas as pd 
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
#adding new column to df
df['Z1'] = [-0.335485,-1.166658,-0.385571,0,0]

#droping column
df.drop('W', axis=1, inplace=True)

#getting rows 
df.loc['B']
#or 
df.iloc[1]
#getting specific value from table
a = df.loc['A','X']
#getting range 
b = df.loc[['A','B'],['Y','Z']]
#removing row 
df.drop('E', axis=0 ,inplace= True)
#getting row based on condition that value in column Z is less than 0\
row_less_than = df[df['Z']<0] 
#get column X based on condition that there is a number in column W that is bigger than 0
col_X = df[df['Y']>0][['Z','Z1']]

#getting data with multiple contidions 
#get only rows where column y and x is bigger than 0
data_multiple = df[(df['Y']>0) & (df['X']>0)]
print(data_multiple)