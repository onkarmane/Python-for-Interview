# import numpy as np

# x = np.random.randint(1, 9, (3, 3))
# y = np.random.randint(1, 9, (5, 7))

# # print(y[0:3, 0:3])
# # print(np.dot(x, y[4:7, 2:5]))


# l = []
# for i in range(0, 3):
#     for j in range(0, 5):
#         print(np.dot(x, y[i:i+3, j:j+3]))


import numpy as np

# Define kernel and matrix
kernel = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
matrix = np.random.randint(0, 10, (5, 7))

# Get dimensions
kernel_height, kernel_width = kernel.shape
matrix_height, matrix_width = matrix.shape

# Perform convolution
output_height = matrix_height - kernel_height + 1
output_width = matrix_width - kernel_width + 1
output = np.zeros((output_height, output_width))

for i in range(output_height):
    for j in range(output_width):
        output[i, j] = np.sum(
            matrix[i:i+kernel_height, j:j+kernel_width] * kernel)

# Print the output
print(output)
