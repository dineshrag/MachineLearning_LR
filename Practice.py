import numpy as np
import matplotlib.pyplot as mat
import pandas as pd
data = pd.read_csv('C:/PythonWorkspace/LinearRegression/Data/Nations.csv')
print(data);
x=data.iloc[:,0:6]
y=data["life_expect"]

import seaborn as sb
correlations = data.corr()
sb.heatmap(correlations,square==True, cmap="seismic")
mat.yticks(rotation=0)
mat.xticks(rotation=90)
mat.show()