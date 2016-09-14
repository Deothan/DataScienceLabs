from scipy import misc
from scipy import ndimage as Image
from scipy.stats import threshold
import matplotlib.pyplot as plt

import numpy as np

#TODO figure out threshholding + rest

img = misc.imread("face.png")
#Resize image
img = misc.imresize(img,(100,100))
misc.imsave("face-resize.png",img)

#Load and save as grayscale
imgGrey = misc.imread("face-resize.png",True)
misc.imsave("faceGrey.png",imgGrey)

#Load and save as binary
imgBW = misc.imread("face-resize.png",True,"1")

misc.imsave("faceBW.png",imgBW)


#Trying to threshold
pilImg01 = misc.toimage(imgGrey)
pilImg01 = pilImg01.point(lambda i:i*0.1,mode="1")
pilImg01.save("pilImg01.png")

pillimg025 = misc.toimage(imgGrey)
pillimg025 = pillimg025.point(lambda i:i*0.25,mode="1")
pillimg025.save("pillimg025.png")

pillimg05 = misc.toimage(imgGrey)
pillimg05 = pillimg05.point(lambda i:i*0.5,mode="1")
pillimg05.save("pillimg05.png")

misc.imsave("faceBW.png",imgBW)



plt.subplot(311)
plt.imshow(pilImg01)
plt.subplot(312)
plt.imshow(pillimg025)
plt.subplot(313)
plt.imshow(pillimg05)


plt.show()