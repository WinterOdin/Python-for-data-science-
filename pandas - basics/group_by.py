from statistics import mean
import numpy as np
import pandas as pd 


data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
        'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
        'Sales':[200,120,340,124,243,350]
}

df = pd.DataFrame(data)

group_by = df.groupby('Company')
#get mean of sales by company 
group_by.mean()
#get value of total sales for some company 
group_by.sum().loc['FB']
#getting alll the info 
df.groupby('Company').describe().transpose()


