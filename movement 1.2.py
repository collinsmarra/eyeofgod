"""
-test for threshed video output.
-idea is good. worked
- implement drone strike class,
"""
import cv2
import numpy as np
cap = cv2.VideoCapture(0)

ret,frame1 = cap.read()
ret,frame2 = cap.read()

while True:
	diff = cv2.absdiff(frame1, frame2) #difference between the first and second frames
	gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # conversion to gray
	blur = cv2.GaussianBlur(gray, (5,5), 0) 
	_, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
	dilated = cv2.dilate(thresh, None, iterations=3)
	contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.imshow("Prove, reality's a simulation", thresh)
	frame1 = frame2
	ret, frame2 = cap.read()

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
print(type(diff))
	
                                                                                                                                                                                                                                                                                                     