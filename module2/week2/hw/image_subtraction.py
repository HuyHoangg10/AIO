import cv2
import numpy as np

bg1_image = cv2.imread('./data/GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('./data/Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('./data/NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    difference_single_channel = cv2.absdiff(bg_img,input_img)
    difference_single_channel = np.mean(difference_single_channel,axis=2).astype(np.uint8)
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    _, difference_binary = cv2.threshold(difference_single_channel,15,255,cv2.THRESH_BINARY)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)

    binary_mask = compute_binary_mask(difference_single_channel)

    output = np.where(binary_mask[:,:,None] == 255, ob_image, bg2_image)

    return output

output = replace_background(bg1_image, bg2_image, ob_image)
if output is not None:
    cv2.imshow('Output', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()