import speech_recognition 

import Ecuacion

class VozAEcuacion:
    def __init__(self): 
        microfono=speech_recognition.Recognizer()
        with speech_recognition.Microphone() as recurso:        
         audio=microfono.listen(recurso)
         try:
          texto=microfono.recognize_google(audio,language='es-ES')
          with open("audio.wav","wb") as fichero:
           fichero.write(audio.get_wav_data())
         except:
          print("Error")   
        print(texto)     
        texto=texto.lower() 
        texto=texto.replace('elevado al cuadrado','^2')
        texto=texto.replace('elevado a la','^')
        texto=texto.replace('uno','1')
        texto=texto.replace('dos','2')
        texto=texto.replace('tres','3')
        texto=texto.replace('cuatro','4')
        texto=texto.replace('cinco','5')
        texto=texto.replace('seis','6')
        texto=texto.replace('siete','7')
        texto=texto.replace('ocho','8')
        texto=texto.replace('nueve','9')
        texto=texto.replace('elevado','^')
        texto=texto.replace('mas','+')
        texto=texto.replace('más','+')
        texto=texto.replace('menos','-')
        texto=texto.replace('por','')
        texto=texto.replace('igual','=')
        texto=texto.replace('entre','/')
        texto=texto.replace('al cuadrado','^2')
        texto=texto.replace('x cuadrado','^2')
        texto=texto.replace('a cero','0')
        texto=texto.replace(' ','')
        self.ecuacionVoz=texto
        iniciador=Ecuacion.ResolverEcuacion(texto)
        self.ecuacion=iniciador.ecuacion
        self.resultado=iniciador.resultado

  