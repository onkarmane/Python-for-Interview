
import cv2
import numpy as np

# Load the YOLO model
model = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3.cfg")

# Create a blob from the input image
image = cv2.imread("people.jpg")
blob = cv2.dnn.blobFromImage(
    image, 1/255.0, (416, 416), (0, 0, 0), True, crop=False)

# Feed the blob into the model
model.setInput(blob)

# Get the output layers of the model
output_layers = model.getUnconnectedOutLayersNames()

# Forward pass through the model
outputs = model.forward(output_layers)

# Print the output

# print(outputs[0][0, 0, :, :, :4])
# # Get the bounding boxes and confidence scores
boxes = outputs[0:4]
print(boxes)
scores = outputs[5:]
print(scores)
# confidences = output[0, 0, :, :, 2]

# # Filter out the bounding boxes with low confidence
# indices = np.where(confidences > 0.5)[0]
# boxes = boxes[indices]
# confidences = confidences[indices]

# # Draw the bounding boxes on the image
# for i in range(len(boxes)):
#     x, y, w, h = boxes[i]
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     cv2.putText(image, str(confidences[i]), (x, y - 10),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# # Display the image
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
