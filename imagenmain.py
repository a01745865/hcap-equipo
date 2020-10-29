import cv2
import numpy as np
import black_white 
import grayescale 
import padding
import convolucion
imagen =cv2.imread("imagen.jpg")
imagen_gray=grayescale.escala(imagen)
valor = 127
cv2.imwrite("grayScale.jpg", imagen_gray)
imagen_black_white = black_white.black_white(imagen_gray, valor)
cv2.imwrite("BlackWhite.jpg", imagen_black_white)
filtro = [[3,4,2],[1,0,1],[2,3,1]]
B = np.array(filtro)
imagen_convolucion = convolucion.convolucion(imagen_gray,B)
cv2.imwrite("ImagenConvolucion.jpg",imagen_convolucion)
imagen_padd = padding.padding(imagen_gray)
imagen_convolucion_padding = convolucion.convolucion(imagen_padd,B)
cv2.imwrite("ImagenConvolucionPadding.jpg",imagen_convolucion_padding)


