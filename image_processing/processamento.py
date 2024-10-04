import cv2 as cv
import numpy as np

def convert_2_Gray(img):
    return cv.cvtColor(img, cv.COLOR_BGR2GRAY)

def Gaussian_Blur(img, sigma=1, ksize=(5,5)):
    return cv.GaussianBlur(src=img, ksize=ksize, sigmaX=sigma)

def Median_Blur(img, ksize=5):
    return cv.medianBlur(img, ksize)

def binariza(img):
    X = img.shape[0]
    Y = img.shape[1]
    img1= img.copy()
    for j in range(Y):
        for i in range(X):
            if img1[i][j] > 145:
                img1[i][j] = 255
            else:
                img1[i][j] = 0
    return img1

def Abertura(img):
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
    opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
    return opening

def Erosao(img):
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5,5))
    erode = cv.erode(img,kernel)
    contorno = img - erode
    return contorno

def identifica(img, contorno):
    X = img.shape[0]
    Y = img.shape[1]
    img2 = img.copy()
    for j in range(Y):
        for i in range(X):
            if contorno[i][j] == 255:
                img2[i][j] = 255
            else:
                continue
    return img2
