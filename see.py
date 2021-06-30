import cv2 
cap = cv2.VideoCapture(0)
ret,frame = cap.read()

while True:
	cv2.imshow("0_*", frame)
	ret,frame = cap.read()
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

                                                                                                                                                                                                                                                                                                     