import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as st

#Loads the CSV file and changes the names of the rows
iris = pd.read_csv('iris.csv', index_col = False)
iris.columns = ['Id', 'SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species']

#Make DataFrames for each species
setosa = iris.loc[iris['Species'] == 'Iris-setosa'].copy()
plt.subplot(311)
plt.hist(setosa.iloc[:,1], 50)

versicolor = iris.loc[iris['Species'] == 'Iris-versicolor'].copy()
plt.subplot(312)
plt.hist(versicolor.iloc[:,1], 50)

virginica = iris.loc[iris['Species'] == 'Iris-virginica'].copy()
plt.subplot(313)
plt.hist(virginica.iloc[:,1], 50)

#Change the Species to 0, 1 and 2
iris['Species'] = iris['Species'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})

plt.show()