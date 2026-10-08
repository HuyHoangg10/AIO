import numpy as np
from PIL import Image

# open image
image1 = Image.open("data/image1.jpg")
image2 = Image.open("data/image2.jpg")
query_image = Image.open("data/query_image.jpg")

# convert to np array
image1_data = np.array(image1)
image2_data = np.array(image2)
query_data = np.array(query_image)

# convert to gray image
image1_gray = np.mean(image1_data, axis=-1)
image2_gray = np.mean(image2_data, axis=-1)
query_gray = np.mean(query_data, axis=-1)

# flatten for compare
img1_flatten = image1_gray.flatten()
img2_flatten = image2_gray.flatten()
query_flatten = query_gray.flatten()


def compute_cosine(A, B):
    cosine = A @ B / (np.linalg.norm(A) * np.linalg.norm(B))
    return cosine


cosine1 = compute_cosine(query_flatten, img1_flatten)
cosine2 = compute_cosine(query_flatten, img2_flatten)
