import cv2
import matplotlib.pyplot as plt
images = []
image = cv2.imread("face_noisy.png")
greyimg = cv2.cvtColor(image,cv2.COLOR_RGBA2GRAY)
sig2 = cv2.GaussianBlur(greyimg,(0,0),2)
sig5 = cv2.GaussianBlur(greyimg,(0,0),5)
sig10 = cv2.GaussianBlur(greyimg,(0,0),10)
images.append(greyimg)
images.append(sig2)
images.append(sig5)
images.append(sig10)


for i in range(4):
    plt.subplot(2,2,1+i)
    plt.imshow(images[i],cmap="Greys_r")

plt.show()