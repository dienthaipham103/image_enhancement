from image_enhacement import *
import os

if __name__ == "__main__":
    # Reading the input image
    path = os.path.join('images', '07.png')
    saved_path = os.path.join('images', '07_.png')
    n = 15

    img = cv2.imread(path, 0)
    enhanced_img = final_image_enhance(img, n)
    cv2.imwrite(saved_path, enhanced_img)