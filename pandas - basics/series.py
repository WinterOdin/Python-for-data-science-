
import numpy as np
import pandas as pd 

labels = ["a","b","c"]
my_data = [10,20,30]
np_arr = np.array(my_data)
dic = {"a":10,"b":20,"c":30}

pd_series = pd.Series(data=my_data, index=labels)
#or 
pd_series = pd.Series(my_data, labels)
#or 
pd_series = pd.Series(dic)
print(pd_series)
pd_series = pd.Series(["Poland","USA","Germany","UK"],[1,2,3,4])
print(pd_series)

