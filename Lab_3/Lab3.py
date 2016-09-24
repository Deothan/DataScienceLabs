import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as st


self = np.asanyarray(np.loadtxt("heights_self_processed.txt",skiprows=1))
tomas = np.asanyarray(np.loadtxt("heights_processed.txt"))
bins = 50

plt.subplot(221)
plt.hist(self[:,1],bins=bins)
plt.subplot(222)
plt.hist(self[:,0],bins=2)
plt.subplot(223)
plt.hist(tomas[:,1],bins=bins)
plt.subplot(224)
plt.hist(tomas[:,0],bins=2)

plt.show()