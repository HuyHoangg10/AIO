import cv2
import numpy as np


def cosine_similarity(x1, x2):
    numerator = x1 @ x2
    denominator = np.linalg.norm(x1) * np.linalg.norm(x2)
    return numerator / denominator


left_img = cv2.imread("./data/Aloe/Aloe_left_1.png", 0)
right_img = cv2.imread("./data/Aloe/Aloe_right_3.png", 0)

left_img = left_img.astype(np.float32)
right_img = right_img.astype(np.float32)

height, width = left_img.shape
depth = np.zeros([height, width], dtype=np.uint8)

kernel_size = 5
kernel_half = kernel_size // 2

disparity_range = 48
scale = 4

for y in range(kernel_half,height-kernel_half):
    for x in range(kernel_half,width-kernel_half):
        disparity = 0
        cost_min = -1
        for j in range(disparity_range):
            d = x - j
            if d-kernel_half >= 0:
                wp = left_img[y-kernel_half:y+kernel_half+1,x-kernel_half:x+kernel_half+1]
                wqd = right_img[y-kernel_half:y+kernel_half+1,d-kernel_half:d+kernel_half+1]
                wp = wp.flatten()
                wqd = wqd.flatten()
                cost = cosine_similarity(wp,wqd)
                if cost > cost_min:
                    cost_min = cost
                    disparity = j
        depth[y,x] = disparity
        
cv2.imshow("depth", depth * scale)
cv2.waitKey(0)
cv2.destroyAllWindows()
