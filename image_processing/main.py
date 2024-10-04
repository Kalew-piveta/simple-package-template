from processamento import convert_2_Gray, Gaussian_Blur, Median_Blur, binariza, Abertura, Erosao, identifica
from plotagem import show, show_pyplot
from utilidades import histogram
import cv2 as cv
import os

def start_quest_1(path):
    img = cv.imread(path)
    img = convert_2_Gray(img)
    Gauss = Gaussian_Blur(img, 2)
    Med = Median_Blur(img)
    Med_Gauss = Median_Blur(Gaussian_Blur(img, 3))

    show(Med_Gauss, "Mediana da Gaussiana")

    hist_med_gauss = histogram(Med_Gauss)
    show_pyplot(hist_med_gauss, xlabel='Intensidade de Iluminação', ylabel='Quantidade de Pixeis', titulo='Hist Median Gauss')

    img_binarizada = binariza(Med_Gauss)
    show(img_binarizada, titulo="Imagem Binarizada")

    abertura = Abertura(img_binarizada)
    show(abertura, titulo="Abertura")

    erosao = Erosao(abertura)
    show(erosao, titulo='Contorno')

    img_identificada = identifica(img, erosao)
    show(img_identificada, titulo='Imagem final')

if __name__ == '__main__':
    
    #    A variavel path_1 é o caminho da imagem que é usada para a start_quest_1, na qual é um exemplo de um problema de segmentação
    #    Toda a função "start_quest_1 é um exemplo do uso do pacote, de forma encadeada a resolver o problema. Faça bom uso!"
    
    basedir = os.path.abspath(os.path.dirname(__file__))
    path_1 = os.path.join(basedir, r'images\brain.png')
    start_quest_1(path_1)
