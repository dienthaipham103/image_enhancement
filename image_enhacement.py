import cv2
import numpy as np
from my_morphology import *

'''
Implementation of image enhancement
'''

# k is old
# do not use the detail tophat, the performance is poor compared to final_image_enhance (using detail tophat)
def image_enhance(grayscale_img, k):
    tophat_img = tophat(grayscale_img, k)
    blackhat_img = blackhat(grayscale_img, k)
    return grayscale_img + tophat_img - blackhat_img

# note: the same the tophat with kernel_size=n
def multi_tophat(grayscale_img, n, type="white"):
    multi_regions = []
    for i in range(1, n+2, 2):
        tophat_img = tophat(grayscale_img, i) if type == "white" else blackhat(grayscale_img, i)
        multi_regions.append(tophat_img)
    
    multi_regions = np.stack(multi_regions, axis=0)

    # maximum gray values of all scales
    multi_tophat_img = np.amax(multi_regions, axis=0)

    return multi_tophat_img

def detail_tophat(grayscale_img, n, type="white"):
    detail_regions = []
    for i in range(1, n, 2):
        tophat_img_1 = tophat(grayscale_img, i) if type == "white" else blackhat(grayscale_img, i)
        tophat_img_2 = tophat(grayscale_img, i+2) if type == "white" else blackhat(grayscale_img, i+2)
        detail_img = tophat_img_2 - tophat_img_1
        detail_regions.append(detail_img)
    
    detail_regions = np.stack(detail_regions, axis=0)

    # maximum gray values of all scales
    detail_tophat_img = np.amax(detail_regions, axis=0)

    return detail_tophat_img

# n >= 3, and old
def final_image_enhance(grayscale_img, n):
    tophat_img = tophat(grayscale_img, n)
    blackhat_img = blackhat(grayscale_img, n)
    detail_white_tophat_img = detail_tophat(grayscale_img, n, "white")
    detail_black_tophat_img = detail_tophat(grayscale_img, n, "black")

    result =  grayscale_img + tophat_img - blackhat_img + detail_white_tophat_img - detail_black_tophat_img
    result = np.clip(result, 0, 255)

    return result

if __name__ == "__main__":
    # Reading the input image
    img = cv2.imread('05.jpg', 0)
    enhance = final_image_enhance(img, 15)
    cv2.imwrite('05_.png', enhance)

