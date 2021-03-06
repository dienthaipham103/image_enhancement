from os import name
import numpy as np
from numpy.lib.stride_tricks import as_strided
import cv2

def pool2d(A, kernel_size, stride, padding, padding_value, pool_mode='max'):
    '''
    2D Pooling

    Parameters:
        A: input 2D array
        kernel_size: int, the size of the window
        stride: int, the stride of the window
        padding: int, implicit zero paddings on both sides of the input
        pool_mode: string, 'max' or 'avg'
    '''
    # Padding
    A = np.pad(A, padding, 'constant', constant_values=padding_value)

    # Window view of A
    output_shape = ((A.shape[0] - kernel_size)//stride + 1,
                    (A.shape[1] - kernel_size)//stride + 1)
    kernel_size = (kernel_size, kernel_size)
    A_w = as_strided(A, shape = output_shape + kernel_size, 
                        strides = (stride*A.strides[0],
                                   stride*A.strides[1]) + A.strides)
    A_w = A_w.reshape(-1, *kernel_size)

    # Return the result of pooling
    if pool_mode == 'max':
        return A_w.max(axis=(1,2)).reshape(output_shape)
    elif pool_mode == 'min':
        return A_w.min(axis=(1,2)).reshape(output_shape)

if __name__ == "__main__":
    A = np.array([[1, 1, 2, 4],
                [5, 6, 7, 8],
                [3, 2, 1, 0],
                [1, 2, 3, 4]])
    img = cv2.imread('c.png', 0)

    x = pool2d(img, kernel_size=2, stride=1, padding=0, pool_mode='max')
    print(x)
            