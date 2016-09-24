import numpy as np
import matplotlib.pyplot as plt
import MinMax
import ZScore


mean = 5
std = 1
size = 1000
dimensions = 2
#Generate 1000 2D samples with mean = 1 and std = 1
sample = np.random.normal(mean,std,size=[size,dimensions])

#adds [20, 20] to sample size
sample = np.vstack((sample,[20,20]))

print("mean: " + str(mean))
print("std: " + str(std))


#find min and max of given sample
def findMinMax(sample):
    max = np.ndarray.max(sample)
    min = np.ndarray.min(sample)
    print("max: " + str(max))
    print("min: " + str(min))

    return [min,max]

print("sample1: ")
findMinMax(sample)
#normalize and standardize sample
def normAndStand(oldArray):
    minmax = findMinMax(oldArray)
    mean = np.mean(oldArray)
    std = np.std(oldArray)
    print(mean)
    print(std)
    newArray = np.empty([len(oldArray),2])
    for i in range(1001):
        x = sample[i][0]
        y = sample[i][1]
        x2 = ZScore.zScore(x,mean,std)
        y2 = ZScore.zScore(y,mean,std)
        x3 = MinMax.minmax(x2,minmax[0],minmax[1])
        y3 = MinMax.minmax(y2,minmax[0],minmax[1])

        newArray[i]=[x3,y3]
    return newArray

#normalized and standardized sample
print("sample2")
sample2 = normAndStand(sample)

sample = np.vstack((sample,[30,30]))

sample3 = normAndStand(sample)

#define x and y for first sample
x1=sample[:,0]
y1 = sample[:,1]

#define x and y for second sample
x2 = sample2[:,0]
y2 = sample2[:,1]

#define x and y for third sample
x3 = sample3[:,0]
y3 = sample3[:,1]


#create subplot for first sample
plt.subplot(311)
plt.title("first sample")
plt.scatter(x1,y1)

#create subplot for second sample
plt.subplot(312)
plt.title("second sample")
plt.scatter(x2,y2)

#create subplot for third sample
plt.subplot(313)
plt.title("third sample")
plt.scatter(x3,y3)

#define layout and show plots
plt.tight_layout()
plt.show()


