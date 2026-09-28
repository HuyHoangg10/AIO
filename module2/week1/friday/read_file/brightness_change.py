import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Read input image (defaults to uint8 and BGR color space)
img = cv2.imread('image1.png', 1)

# 2. Cast data type to float to prevent integer overflow and underflow
img = img.astype(float)
print(f"Current data type: {img.dtype}")

# 3. Process: Adjust brightness by adding an offset
# Positive value increases brightness; negative value decreases it (e.g., -50)
img = img + 20

# 4. Clip pixel values to the valid dynamic range [0, 255]
img = np.clip(img, 0, 255)

# 5. Cast back to uint8 for memory efficiency and proper rendering
img = img.astype(np.uint8)

# 6. Show: Convert BGR to RGB via channel slicing and display with Matplotlib
img = img[:, :, ::-1]
plt.imshow(img)
plt.axis('off')
plt.show()