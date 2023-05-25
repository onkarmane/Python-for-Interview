# import cv2
# import numpy as np


# def findLocalMaxima(image):
#     # Convert the image to grayscale
#     grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply the morphological gradient to the grayscale image
#     morphological_gradient = cv2.morphologyEx(
#         grayscale_image, cv2.MORPH_GRADIENT, None)

#     # Threshold the morphological gradient to create a binary image
#     thresholded_image = cv2.threshold(
#         morphological_gradient, 0.0, 1.0, cv2.THRESH_BINARY)[1]

#     # Find the connected components in the binary image
#     connected_components = cv2.connectedComponents(thresholded_image)

#     # Find the local maxima in the connected components
#     local_maxima = []
#     for i in range(1, connected_components[0] + 1):
#         if np.all(connected_components == i):
#             local_maxima.append(np.where(connected_components == i)[0])

#     return local_maxima


# def watershed(image):
#     # Convert the image to grayscale
#     grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply the distance transform to the grayscale image
#     distance_transform = cv2.distanceTransform(grayscale_image, cv2.DIST_L2, 5)

#     # Threshold the distance transform to create a binary image
#     thresholded_image = cv2.threshold(
#         distance_transform, 0.5, 1.0, cv2.THRESH_BINARY)[1]

#     # Find the local minima in the binary image
#     local_minima = findLocalMaxima(image)

#     # Create a marker image with one pixel per local minimum
#     marker_image = np.zeros_like(grayscale_image, dtype=np.uint8)
#     for point in local_minima:
#         marker_image[point[0], point[1]] = 255

#     # Apply the watershed algorithm to the marker image
#     watershed_image = cv2.watershed(image, marker_image)

#     return watershed_image


# if __name__ == "__main__":
#     # Load the image
#     image = cv2.imread("card.png")

#     # Apply the watershed algorithm
#     watershed_image = watershed('card.png')

#     # Display the results
#     cv2.imshow("Watershed Image", watershed_image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import cv2

# Load the image
image = cv2.imread('man2.jpg')

# Preprocess the image (if needed)
# ...

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive thresholding to create a binary mask
_, mask = cv2.threshold(
    blurred, 0, 128, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Perform morphological operations to enhance the mask
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=5)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=5)

# Apply the mask to the original image
result = cv2.bitwise_and(image, image, mask=mask)

# Save the result
cv2.imwrite('output_image.jpg', result)

# Display the result
cv2.imshow('Output Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
