import cv2
import numpy as np

'''
Implementation of basic morphological processing by open cv 
'''

def dilation(grayscale_img, k, iter=1):
    kernel = np.ones((k, k), np.uint8)
    img_dilation = cv2.dilate(grayscale_img, kernel, iterations=iter)
    return img_dilation

def erosion(grayscale_img, k, iter=1):
    kernel = np.ones((k, k), np.uint8)
    img_erosion = cv2.erode(grayscale_img, kernel, iterations=iter)
    return img_erosion

def open(grayscale_img, k):
    kernel = np.ones((k, k), np.uint8)
    opening = cv2.morphologyEx(grayscale_img, cv2.MORPH_OPEN, kernel)
    return opening

def close(grayscale_img, k):
    kernel = np.ones((k, k), np.uint8)
    closing = cv2.morphologyEx(grayscale_img, cv2.MORPH_CLOSE, kernel)
    return closing

def tophat(grayscale_img, k):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, 
                                   (k, k))
    # Applying the Top-Hat operation
    tophat_img = cv2.morphologyEx(grayscale_img, 
                              cv2.MORPH_TOPHAT,
                              kernel)
    return tophat_img

def blackhat(grayscale_img, k):
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, 
                                   (k, k))
    # Applying the Top-Hat operation
    blackhat_img = cv2.morphologyEx(grayscale_img, 
                              cv2.MORPH_BLACKHAT,
                              kernel)
    return blackhat_img

if __name__ == "__main__":
    # Reading the input image
    img = cv2.imread('a.png', 0)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    erosion_img = erosion(img, 10)
    dilation_img = dilation(img, 10)
    open_img = open(img, 10)
    close_img = close(img, 10)
    tophat_img = tophat(img, 10)
    blackhat_img = blackhat(img, 10)

    # save
    cv2.imwrite('erosion.png', erosion_img)
    cv2.imwrite('dilation.png', dilation_img)
    cv2.imwrite('open.png', open_img)
    cv2.imwrite('close.png', close_img)
    cv2.imwrite('tophat.png', tophat_img)
    cv2.imwrite('blackhat.png', blackhat_img)