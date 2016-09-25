import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats as st
import Lab_2


self = np.asarray(np.loadtxt("heights_self_processed.txt",skiprows=1))
tomas = np.asarray(np.loadtxt("heights_processed.txt"))
#print(self)
bins = 28


males = self[np.where(self[:,0]==1)]
females = self[np.where(self[:,0]==0)]

print(st.describe(self[:,1]))

meanMales = np.mean(males[:,1])
meanFemales = np.mean(females[:,1])
print("Males")
print(meanMales)
print(st.normaltest(males[:,1]))
print(st.describe(males[:,1]))

print("Females")
print(meanFemales)
print(st.normaltest(females[:,1]))
print(st.describe(females[:,1]))

print("Compare male female")
print(st.ttest_ind(males[:,1],females[:,1]))

#Two tailed test

difmean = meanMales-meanFemales
sp2 = ((79-1)*9.8096658729730617+(67-1)*8.6214285201628211)/(79+67-2)

SE = np.sqrt(sp2/79+sp2/67)

zCrit  =st.t.ppf(0.975,144)
std = self.std()
CI = (difmean-zCrit*SE,difmean+zCrit*SE)
print("CI: ",CI)

critMale = st.t.ppf(0.975,78)
critFemale = st.t.ppf(0.975,66)

CIMale = (meanMales-critMale * np.sqrt(males[:,1].var()),(meanMales+critMale * np.sqrt(males[:,1].var())))
CIFemale = (meanFemales-critFemale * np.sqrt(females[:,1].var()),(meanFemales+critFemale* np.sqrt(females[:,1].var())))
print(CIMale,CIFemale)
##CIFemale


means = [meanMales,meanFemales]

counts, binedges = np.histogram(means,2)
bin_centres = (binedges[:-1] + binedges[1:])/2.

CIs = [(CIMale[1]-CIMale[0])/2,(CIFemale[1]-CIFemale[0])/2]

ind = np.arange(2)
width=1;

plt.figure(1)
plt.subplot(221)
plt.hist(self[:,1],bins=bins)
plt.subplot(222)
plt.hist(self[:,0],bins=2)
plt.subplot(223)
plt.hist(tomas[:,1],bins=bins)
plt.subplot(224)
plt.hist(tomas[:,0],bins=2)


plt.figure(2)
plt.title("males vs females")
plt.subplot(211)
plt.title("males")
plt.hist(males[:,1])
plt.subplot(212)
plt.title("females")
plt.hist(females[:,1])

plt.figure(3)


plt.bar(0,meanMales,width,color ="Blue",yerr=CIs[0],error_kw=dict(elinewidth=2, ecolor="red"))
plt.bar(1,meanFemales,width,color ="Green",yerr=CIs[1],error_kw=dict(elinewidth=2, ecolor="red"))
xticklabels=["Men","Women"]
plt.xticks(ind+width/2,xticklabels)
#plt.errorbar((1,0),means,yerr=CIs,fmt="o")

plt.show()
