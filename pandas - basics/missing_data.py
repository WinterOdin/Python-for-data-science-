from statistics import mean
import numpy as np
import pandas as pd 

data = {'A':[1,2,np.nan], 'B':[5, np.nan, np.nan], 'C':[1, 2, 3]}
df = pd.DataFrame(data)
#droping NaN, if you want to drop columns set axis=1, to make permament changes set inplace=true
df.dropna()
#if you want to drop Nan with some threshold use thresh=1<-amount of acceptable Nan values in row
df.dropna(thresh=2)
#filling NaN 
df.fillna(value="filled")
#or fill NaN with mean 
df.fillna(value=df['A'].mean())
#check different statistical methods for filling NaN