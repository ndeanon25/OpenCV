import cv2
import numpy as np


#Create a blank image
image = np.zeros((512,512,3), dtype = np.uint8)

#Draw a rectangle
cv2.rectangle(image, (100,100), (300,250), (0,255,0), thickness = 2)

#Draw a circle
cv2.circle(image, (350,350), 100, (255,0,0), thickness = 2)

#Display the image
cv2.imshow('OpenCV example', image)

#wait for a key press and close window
cv2.waitKey(0)
cv2.destroyAllWindows()
