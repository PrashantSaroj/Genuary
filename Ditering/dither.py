import cv2
import numpy as np


def minmax(v):
    if v > 255:
        v = 255
    elif v < 0:
        v = 0
    return v


def atkinson_dithering(inMat):
    # grab the image dimensions
    h = inMat.shape[0]
    w = inMat.shape[1]
    
    # loop over the image
    for y in range(1, h-3):
        for x in range(1, w-3):
            # threshold the pixel
            new_p = inMat[y, x]
            if (new_p > 128):
                new_p = 255
            else:
                new_p = 0
            quant_error = (inMat[y, x] - new_p)/8.0
            inMat[y, x] = new_p
            
            # error diffusion
            inMat[y, x+1] = minmax(inMat[y, x+1] + quant_error)
            inMat[y, x+2] = minmax(inMat[y, x+2] + quant_error)
            inMat[y+1, x] = minmax(inMat[y+1, x] + quant_error)
            inMat[y+2, x] = minmax(inMat[y+2, x] + quant_error)
            inMat[y+1, x+1] = minmax(inMat[y+1, x+1] + quant_error)
            inMat[y-1, x-1] = minmax(inMat[y-1, x-1] + quant_error)


    # return the thresholded image
    return inMat



# #read image
inMat = cv2.imread('input.png', 0)
outMat_gray = atkinson_dithering(inMat)
cv2.imshow('Result', outMat_gray)
cv2.waitKey(0)
