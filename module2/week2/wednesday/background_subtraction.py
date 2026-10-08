import cv2
import numpy as np

# 1. Load and resize the original background image
bg = cv2.imread('background.png', 1)
bg = cv2.resize(bg, (640, 480))

# 2. Load and resize the target image containing the subject
img = cv2.imread('StillImage.png', 1)
img = cv2.resize(img, (640, 480))

# 3. Compute the absolute difference between background and subject image
difference = cv2.absdiff(bg, img)

# 4. Apply binary thresholding to create a mask (threshold = 15, max value = 255)
_, difference_binary = cv2.threshold(difference, 15, 255, cv2.THRESH_BINARY)

# 5. Load and resize the replacement background image
new_bg = cv2.imread('FakeBackground.png')
new_bg = cv2.resize(new_bg, (640, 480))

# 6. Replace background: keep subject pixels where mask is 255, otherwise use new background
output = np.where(difference_binary == 255, img, new_bg)

# 7. Save the composited result image to disk
cv2.imwrite('output_111.png', output)