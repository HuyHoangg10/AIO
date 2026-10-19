import cv2
import numpy as np


def l1_distance(x, y):
    return np.abs(x - y)


def l2_distance(x, y):
    return np.square(x - y)

left_img = cv2.imread("./data/Aloe/Aloe_left_1.png",0)
right_img = cv2.imread("./data/Aloe/Aloe_right_1.png",0)

left_img = left_img.astype(np.float32)
right_img = right_img.astype(np.float32)

height,width = left_img.shape

depth = np.zeros([height,width],dtype=np.uint8)


kernel_size = 3
kernel_half = kernel_size // 2

disparity_range = 32
scale = 4
max_value = 255


for y in range(kernel_half,height-kernel_half):
    for x in range(kernel_half,width-kernel_half):
        cost_min = (kernel_size * kernel_size) * max_value
        disparity = 0
        for j in range(disparity_range):
            cost = 0
            for v in range(-kernel_half,kernel_half+1):
                for u in range(-kernel_half,kernel_half+1):
                    value = max_value
                    if x + u - j >= 0 :
                        value = l1_distance(left_img[y+v,x+u],right_img[y+v,x+u-j])
                    cost += value
            if cost < cost_min:
                disparity = j
                cost_min = cost
        depth[y,x] = disparity

cv2.imshow("depth",depth*scale)
cv2.waitKey(0)
cv2.destroyAllWindows()       