# import the necessary packages
import numpy as np
import cv2
from matplotlib import pyplot as plt

# load and show the image, grey scale
image = cv2.imread("images/games.jpg")
cv2.imshow("Image", image)

# wait for a keyinput
cv2.waitKey(0)

# cv2.calcHist(images, channels, mask, histSize (bin count), ranges[, hist[, accumulate]])
# see np.bincount() 10x faster that np.histogram() for 1D array
hist = cv2.calcHist([image],[0],None,[256],[0,256])
plt.hist(image.ravel(),256,[0,256])
plt.title('Histogram for gray scale picture')
plt.show()

#img = cv2.imread('images/image1.jpg.jpg')
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()


# wait for a keyinput
cv2.waitKey(0)
# destroy window/s
cv2.destroyAllWindows()