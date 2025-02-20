import numpy as np
import cv2
import matplotlib.pyplot as plt

# Creating a image with black and white lines
height, width = 256, 256
image = np.zeros((height,width), dtype=np.uint8)
image[::10,:] = 255

# Applying Gaussian filter with different kernel sizes
gaussian1 = cv2.GaussianBlur(image, (3,3),0)
gaussian2 = cv2.GaussianBlur(image, (5,5),0)
gaussian3 = cv2.GaussianBlur(image, (7,7),0)

#Display it
plt.figure(figsize=(10,7))
plt.subplot(1,4,1),plt.imshow(image, cmap='grey'), plt.title('Original Image')
plt.subplot(1,4,2),plt.imshow(gaussian1, cmap='grey'), plt.title('Gaussian1')
plt.subplot(1,4,3),plt.imshow(gaussian2, cmap='grey'), plt.title('Gaussian2')
plt.subplot(1,4,4),plt.imshow(gaussian3, cmap='grey'), plt.title('Gaussian3')
plt.show()

