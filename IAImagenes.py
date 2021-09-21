from PIL import Image
from pytesseract import *
import Ecuacion

class ImagenAEcuacion:
    def __init__(self,direccionImagen): 
        pytesseract.tesseract_cmd=r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

        img=Image.open(direccionImagen)
        resultado=pytesseract.image_to_string(img,lang='eng+equ+osd')
        print("IA:  "+resultado)
        resultado=resultado.replace('%','^')
        resultado=resultado.replace('*','^',1)
        resultado=resultado.replace('','')
        print("Casteo:  "+resultado)
        iniciador=Ecuacion.ResolverEcuacion(resultado)
        self.ecuacion=iniciador.ecuacion
        self.resultado=iniciador.resultado