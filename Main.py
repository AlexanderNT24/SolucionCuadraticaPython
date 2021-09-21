import tkinter 
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

#Modulos
import IAImagenes
import IAVoz
import Ecuacion
import TextoAVoz

#GUI
#Interfaz
ventana=tkinter.Tk()
ventana.geometry("800x500")
ventana.title("Equations")
ventana['bg'] = '#e8e8e8'
ventana.tk.call('wm', 'iconphoto', ventana._w, tkinter.PhotoImage(file=".\iconos\iconoPrincipal.png"))
def abrirArchivo():
   direccionImagen=filedialog.askopenfilename(title="Abrir archivo")
   iniciadorArchivo=IAImagenes.ImagenAEcuacion(direccionImagen) 
   ecuacion = ''.join(iniciadorArchivo.ecuacion)
   resultado= ''.join(iniciadorArchivo.resultado)
   mensaje=ecuacion+"\n"+resultado.replace('X2',' X2')
   cajaTextoResultado.configure(state='normal')
   cajaTextoResultado.delete("1.0","end")
   cajaTextoResultado.insert(1.0,mensaje)
   cajaTextoResultado.configure(state='disabled')
   botonHablar=tkinter.Button(ventana,image=imagenHablar,command=lambda:decirRespuesta(iniciadorArchivo.resultado),relief="flat", bg="white",activebackground="red").place(x=550, y=200)

def grabarAudio():
   iniciador=IAVoz.VozAEcuacion() 
   ecuacion = ''.join(iniciador.ecuacion)
   resultado= ''.join(iniciador.resultado)
   mensaje=ecuacion+"\n"+resultado.replace('X2',' X2')
   cajaTextoResultado.configure(state='normal')
   cajaTextoResultado.delete("1.0","end")
   cajaTextoResultado.insert(1.0,mensaje)
   cajaTextoResultado.configure(state='disabled')
   botonHablar=tkinter.Button(ventana,image=imagenHablar,command=lambda:decirRespuesta(iniciador.resultado),relief="flat", bg="white",activebackground="red").place(x=550, y=200)

def insertarEcuacion():   
   ecuacion=cajaTextoEcuacion.get(1.0, tkinter.END+"-1c")
   ecuacion=ecuacion.replace(' ','')
   if not ecuacion:
    messagebox.showinfo("Error", "Cuadro de texto vacio")
   else:
    iniciadorArchivo=Ecuacion.ResolverEcuacion(ecuacion) 
   ecuacion = ''.join(iniciadorArchivo.ecuacion)
   resultado= ''.join(iniciadorArchivo.resultado)
   mensaje=ecuacion+"\n"+resultado.replace('X2',' X2')
   cajaTextoResultado.configure(state='normal')
   cajaTextoResultado.delete("1.0","end")
   cajaTextoResultado.insert(1.0,mensaje)
   cajaTextoResultado.configure(state='disabled')
   botonHablar=tkinter.Button(ventana,image=imagenHablar,command=lambda:decirRespuesta(iniciadorArchivo.resultado),relief="flat", bg="white",activebackground="red").place(x=550, y=200)

def decirRespuesta(resultado):
   inciador=TextoAVoz.TextoaVoz(resultado)

#Imagenes
imagenTexto=PhotoImage(file=".\iconos\iconoEnviar.png")
imagenSubirArchivo=PhotoImage(file=".\iconos\iconoSubirArchivo.png")
imagenGrabarAudio=PhotoImage(file=".\iconos\iconoGrabar.png")
imagenHablar=PhotoImage(file=".\iconos\iconoParlante.png")

#Etiquetas
#Etiqueta Titulo/Cabecera (x=0,y=0)-(x=fill,y=24)   
etiquetaTitulo = Label(ventana, text="Equations")
etiquetaTitulo.pack(fill="x",side="top")
etiquetaTitulo.config(fg="#e8e8e8",  bg="#810000", font=("Roboto",30),anchor="nw") 
#Etiqueta Servicios (x=50,y=60)-(x=50,y=80)  
etiquetaServicios = Label(ventana, text="Servicios:")
etiquetaServicios.place(x=0, y=60)
etiquetaServicios.config(fg="#1b1717",  bg="#e8e8e8",font=("Verdana",20)) 

#Etiqueta Agregar Texto (x=150,y=130)-(x=200,y=240) 
etiquetaAgregarTexto = Label(ventana, text="Ecuación")
etiquetaAgregarTexto.place(x=150, y=130)
etiquetaAgregarTexto.config(fg="#1b1717",  bg="#e8e8e8",font=("Verdana",10)) 

#Etiqueta Agregar Achivo (x=350,y=230)-(x=400,y=240) 
etiquetaAgregarAchivo = Label(ventana, text="Archivo Ecuación")
etiquetaAgregarAchivo.place(x=350, y=130)
etiquetaAgregarAchivo.config(fg="#1b1717",  bg="#e8e8e8",font=("Verdana",10)) 

#Etiqueta Grabar Audio (x=150,y=230)-(x=200,y=240) 
etiquetaGrabarAudio = Label(ventana, text="Grabar Ecuación")
etiquetaGrabarAudio.place(x=550, y=130)
etiquetaGrabarAudio.config(fg="#1b1717",  bg="#e8e8e8",font=("Verdana",10)) 

#Botones
#Boton Agregar Texto (x=150,y=100)-(x=175,y=125) 
botonAgregarTexto=tkinter.Button(ventana,image=imagenTexto,command=insertarEcuacion,relief="flat", bg="#e8e8e8").place(x=150, y=100)

#Boton Agregar Archivo (x=350,y=100)-(x=375,y=125) 
botonAgregarArchivo=tkinter.Button(ventana,image=imagenSubirArchivo,command=abrirArchivo,relief="flat", bg="#e8e8e8").place(x=350, y=100)

#Boton Grabar Audio (x=550,y=100)-(x=575,y=125) 
botonGrabarAudio=tkinter.Button(ventana,image=imagenGrabarAudio,command=grabarAudio,relief="flat", bg="#e8e8e8",activebackground="red").place(x=550, y=100)


#Cajas de Texto
#Caja de Texto (x=150,y=150)-(x=170,y=151)  
cajaTextoEcuacion = tkinter.Text(ventana,width=20,height=1)
cajaTextoEcuacion.place(x=150, y=150)

#Caja de texto Solucionario (x=0,y=300)-(x=fill,y=320) 
cajaTextoResultado = tkinter.Text(ventana)

cajaTextoResultado.place(x=100, y=200)
 
ventana.mainloop()