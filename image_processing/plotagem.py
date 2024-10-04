import cv2 as cv
from matplotlib import pyplot as plt

def show(img, titulo='Imagem resultado', write=False):
    if write:
        cv.imwrite(r'C:\Users\kalew\Desktop\---UNB---\INTRO-PROSS-IMAGEM\projeto 2\imagesT2png\binarizado.jpg', img)
    else:
        cv.imshow(titulo, img)
        cv.waitKey(0)
        cv.destroyAllWindows()

def show_pyplot(img, color='gray', xlabel='Eixo X', ylabel='Eixo Y', titulo = "Histograma"):
    plt.plot(img, color=color)
    plt.title(titulo, loc='center')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
