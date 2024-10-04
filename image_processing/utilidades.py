import cv2 as cv

def histogram(img):
    return cv.calcHist([img], [0], mask=None, histSize=[256], ranges=[0, 256])

def try_sigma_Gauss(img):
    for i in range(1,10):
        show(Gaussian_Blur(img, sigma=i), 'imagem Bluring')
