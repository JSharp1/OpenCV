# capture and crop a video frame
import cv2
print(cv2.__version__)
vidcap = cv2.VideoCapture('video/SampleVideo_360x240_1mb.mp4')
success,image = vidcap.read()
roi = image[60:180, 120:240]

cv2.imshow('roi_image', roi)
cv2.imshow('image', image)


print 'Read a new frame: ', success
cv2.imwrite("frame_ROI.jpg", roi)     # save frame as JPEG file
cv2.imwrite("frame_NO_ROI.jpg", image)     # save frame as JPEG file
