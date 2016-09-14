from scipy import misc
from scipy import ndimage
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
imgBW = misc.imread("face-resize.png",True,mode="L")
print(imgBW.dtype)
#open_img = ndimage.binary_opening(imgBW)
#imgBW = ndimage.binary_closing(open_img)
#misc.toimage(imgBW).convert("1");
misc.imsave("faceBW.png",imgBW)

plt.subplot(221)
plt.title("Original")
plt.imshow(imgBW,cmap='gray')
plt.subplot(222)
plt.title("Threshhold 0.1")
image_threshold = .1
label_array, n_features = ndimage.label(imgBW>image_threshold*255)
plt.imshow(label_array,cmap='gray')
print(label_array)
plt.subplot(223)
plt.title("Threshhold 0.25")
image_threshold = .25
label_array, n_features = ndimage.label(imgBW>image_threshold*255)
plt.imshow(label_array,cmap='gray')
print(label_array)

plt.subplot(224)
plt.title("Threshhold 0.5")
image_threshold = .5
label_array, n_features = ndimage.label(imgBW>image_threshold*255)
plt.imshow(label_array,cmap='gray')
misc.imsave("threshold0-5.png",label_array)
print(label_array)


print(imgBW)
plt.tight_layout()
plt.show()

