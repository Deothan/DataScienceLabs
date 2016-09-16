import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import cv2


#Create black and white image, using custon threshold
def createBW(img, thresh):
    threshold = 255*thresh
    newImg = cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)[1]
    return newImg


#Read and resize image
img = cv2.imread("face.png")
resImg = cv2.resize(img,(100,100))
cv2.imwrite("face-resized.png",resImg)
#Set image to grayscale
greyImg = cv2.cvtColor(resImg,cv2.COLOR_RGBA2GRAY)


#Degfine thresholds
thresholds = [0.1,0.25,0.5]
images=[]
slices = []
labels = []


def printimages():
    plt.figure(1)
    for i in range(len(thresholds)):
        images.append(createBW(greyImg,thresholds[i]))

        plt.subplot(331+i)
        plt.imshow(images[i],cmap="Greys_r")
        plt.subplot(334+i)
        plt.hist(images[i])

def getLabelsAndSlices():

    for i in range(len(images)):
        label, nf = np.asarray(ndimage.label(images[i]))
        labels.append(label)
        slice = ndimage.find_objects(label)
        slices.append(slice)

def showSlices():

    for i in range(len(images)):
        count = 0
        plt.figure(i+2)
        rows = round(len(slices[i])/4)+1

        print(len(slices[i]))
        for sli in slices[i]:
            plt.subplot(rows,5,1+count)
            plt.imshow(labels[i][sli],cmap="Greys")
            count+=1


printimages()
getLabelsAndSlices()
showSlices()

plt.tight_layout()
plt.show()
