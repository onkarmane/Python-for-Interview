import cv2
import numpy as np

# Read the input image
image = cv2.imread('card.png')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to obtain a binary image
_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# Apply morphological operations to remove noise and fill holes
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel, iterations=2)

# Perform the distance transform
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
_, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

# Convert the sure foreground to 8-bit image
sure_fg = np.uint8(sure_fg)

# Perform the watershed algorithm
_, markers = cv2.connectedComponents(sure_fg)
markers += 1
markers[opening == 255] = 0
cv2.watershed(image, markers)

# Color the segmented regions
image[markers == -1] = [0, 0, 255]

# Display the result
cv2.imshow('Segmented Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
