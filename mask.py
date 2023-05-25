# import cv2

# # Load the image
# image = cv2.imread('card.png', 0)  # Read as grayscale

# # Apply thresholding with cv2.THRESH_BINARY
# _, binary_threshold = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)

# # Apply thresholding with cv2.THRESH_BINARY_INV
# _, binary_inv_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY_INV)

# # Display the results
# cv2.imshow('Binary Threshold', binary_threshold)
# cv2.imshow('Binary Inverted Threshold', binary_inv_threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the image
image = cv2.imread('card.png')

# Create a mask (assuming it has been obtained using appropriate techniques)
mask = np.zeros(image.shape[:2], dtype=np.uint8)
mask[100:300, 200:400] = 255  # Example mask region

# Apply the mask to the image
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Display the results
cv2.imshow('Original Image', image)
cv2.imshow('Mask', mask)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
