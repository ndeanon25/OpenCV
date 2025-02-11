import cv2

image = cv2.imread('unsplash.jpg')

#Applying the Gaussian Blur filter
blurredImage = cv2.GaussianBlur(image, (13,13), 3)

#Display the original image
cv2.imshow('Original Image', image)

#Display the blurred image
cv2.imshow('Blurred Image', blurredImage)

#wait for a key press and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()