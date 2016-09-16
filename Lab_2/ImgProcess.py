from scipy import misc
from scipy import ndimage
import matplotlib.pyplot as plt



img = misc.imread("face.png")
#Resize image
img = misc.imresize(img,(100,100))
misc.imsave("face-resize.png",img)

#Load and save as grayscale
imgGrey = misc.imread("face.png",True,mode="LA")
misc.imsave("faceGrey.png",imgGrey)

#Load and save as binary
imgBW = misc.imread("faceGrey.png",mode="1")
misc.imsave("faceBW.png",imgBW)

#Histogram for Threshhold 0.1
plt.subplot(231)
plt.title("Threshhold 0.1")
image_threshold = .1
label_array1, n_features1 = ndimage.label(imgGrey<image_threshold*255)
plt.imshow(label_array1,cmap="Greys")
print(n_features1)
misc.imsave("threshold0-1.png",label_array1)

#Histogram for Threshhold 0.25
plt.subplot(232)
plt.title("Threshhold 0.25")
image_threshold = .25
label_array2, n_features2 = ndimage.label(imgGrey<image_threshold*255)
plt.imshow(label_array2,cmap="Greys")
print(n_features2)
misc.imsave("threshold0-25.png",label_array2)


#Histogram for Threshhold 0.5
plt.subplot(233)
plt.title("Threshhold 0.5")
image_threshold = .5
label_array3, n_features3 = ndimage.label(imgGrey<image_threshold*255)
plt.imshow(label_array3,cmap="Greys")
misc.imsave("threshold0-5.png",label_array3)
print("labelsarray: "+str(label_array3))

slices = ndimage.find_objects(label_array3)

plt.subplot(234)
plt.title("threshold 0.1")
plt.hist(label_array1,weights=imgGrey)
plt.subplot(235)
plt.title("threshold 0.25")
plt.hist(label_array2,weights=imgGrey)
plt.subplot(236)
plt.title("threshold 0.5")
plt.hist(label_array3,weights=imgGrey)
print(len(label_array3))

print(len(label_array1))

plt.tight_layout()
plt.show()

