# import the necessary packages
import numpy as np
import cv2

# load the image1, grey scale
image = cv2.imread("images/image1.jpg", 0)
cv2.imshow("Image", image)

# wait for a keyinput
cv2.waitKey(0) & 0xFF
# destroy window/s
cv2.destroyAllWindows()