import cv2
import numpy as np
from cv2_morphology import *

def remove_text(grayscale_img, color_threshold, blur_size):
    h, w = grayscale_img.shape
    _, thresh = cv2.threshold(grayscale_img, color_threshold, 255, cv2.THRESH_BINARY)
    tophat_img = tophat(thresh, 3)

    result = img.copy()
    (rows, cols) = np.nonzero(tophat_img)
    for (r, c) in zip(rows, cols):
        r1 = max(0, r-blur_size)
        r2 = min(h-1, r+blur_size)
        c1 = max(0, c-blur_size)
        c2 = min(w-1, c+blur_size)
        kernel_img = img[r1:r2, c1:c2]
        result[r1:r2, c1:c2] = np.average(kernel_img)
    
    return result

if __name__ == "__main__":
    img = cv2.imread('images/07.png', 0)
    # img = cv2.imread('test.png', 0)
    removed_img = remove_text(img, 200, 5)
    cv2.imwrite('07.png', removed_img)