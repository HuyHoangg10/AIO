import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("./image1.png", 1)
print(img.shape)

#slicing
# plt.imshow(img[:, :, ::-1])

#fancy indexing
# plt.imshow(img[:, :, [2, 1, 0]])

# cv2.cvtColor()
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

#change the RGB image to gray image
img = np.apply_along_axis(np.mean,axis = 2,arr = img)
print(img.shape)
img = img.astype(np.uint8)
plt.imshow(img, cmap='gray')
plt.show()



#save the image :
# cv2.imwrite("new_image.png",img)