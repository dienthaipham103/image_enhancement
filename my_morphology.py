import numpy as np
import cv2
from maxpooling2d import *

'''
Implementation of basic morphological processing by numpy 
'''
def operator(grayscale_img, k, operation):
    h, w = grayscale_img.shape
    result = np.zeros((h, w))
    for j in range(w):
        for i in range(h):
            i1 = max(0, i - k//2)
            i2 = min(h, i + k//2 + 1)
            j1 = max(0, j - k//2)
            j2 = min(w, j + k//2 + 1)
            kernel_region = grayscale_img[i1:i2, j1:j2]

            # do operation on the kernel region
            output_element = np.max(kernel_region) if operation == "dilation" else np.min(kernel_region)

            # change the result matrix
            result[i][j] = output_element
    
    return result

def dilation_slow(grayscale_img, k, iterations=1):
    result = grayscale_img.copy()
    for _ in range(iterations):
        result = operator(result, k, "dilation")
    return result

def erosion_slow(grayscale_img, k, iterations=1):
    result = grayscale_img.copy()
    for _ in range(iterations):
        result = operator(result, k, "erosion")
    return result

def dilation(grayscale_img, k, iterations=1):
    result = grayscale_img.copy()
    for _ in range(iterations):
        result =  pool2d(result, kernel_size=k, stride=1, padding=(k//2, k//2), padding_value=(0, 0), pool_mode='max')
    return result.astype(float)

def erosion(grayscale_img, k, iterations=1):
    result = grayscale_img.copy()
    for _ in range(iterations):
        result =  pool2d(result, kernel_size=k, stride=1, padding=(k//2, k//2), padding_value=(255, 255), pool_mode='min')
    return result.astype(float)

def open(grayscale_img, k):
    return dilation(erosion(grayscale_img, k), k)

def close(grayscale_img, k):
    return erosion(dilation(grayscale_img, k), k)

def tophat(grayscale_img, k):
    return grayscale_img - open(grayscale_img, k)

def blackhat(grayscale_img, k):
    return close(grayscale_img, k) - grayscale_img



if __name__ == "__main__":
    print("Welcome to my implementation")

    ###################################################################
