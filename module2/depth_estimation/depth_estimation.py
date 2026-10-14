import cv2
import numpy as np


def l1_distance(x, y):
    return np.abs(x - y)


def l2_distance(x, y):
    return np.square(x - y)


leftimg_path = "./data/tsukuba/left.png"
rightimg_path = "./data/tsukuba/right.png"
scale = 16
disparity_range = 16

left_img = cv2.imread(leftimg_path, 0)
right_img = cv2.imread(rightimg_path, 0)


left_img = left_img.astype(np.float32)
right_img = right_img.astype(np.float32)

height, width = left_img.shape
depth = np.zeros([height, width], dtype=np.uint8)

for y in range(height):
    for x in range(width):
        disparity = 0
        cost_min = 255
        for d in range(disparity_range):
            if x - d >= 0:
                cost = l1_distance(left_img[y,x],right_img[y,x-d])
                if cost < cost_min:
                    cost_min = cost
                    disparity = d
        depth[y,x] = disparity

cv2.imshow("Depth",depth * scale)
cv2.waitKey(0)
cv2.destroyAllWindows()