# from: http://www.pyimagesearch.com/2016/08/29/common-errors-using-the-raspberry-pi-camera-module/
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import io
import socket
import struct
NOT FINISHED
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(.1)

# setup a client socket to my_server:12345
client = socket.socket()
client.connect('162.168.0.11', 12345)
# make a file like object out of the connection to server
connection = client.makefile('wb')
try:
	with picamera.PiCamera() as camera:
		# Note the start time and construct a stream to hold image data
        # temporarily (we could write it directly to connection but in this
        # case we want to find out the size of each capture first to keep
        # our protocol simple)
		start = time.time()
		stream = io.BytesIO()

		# capture frames from the camera
		for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
			# grab the raw NumPy array representing the image - this array
			# will be 3D, representing the width, height, and # of channels
			image = frame.array

			# show the frame
			cv2.imshow("Frame", image)
			key = cv2.waitKey(1) & 0xFF

			# clear the stream in preparation for the next frame
			rawCapture.truncate(0)

			# if the `q` key was pressed, break from the loop
			if key == ord("q"):
				break