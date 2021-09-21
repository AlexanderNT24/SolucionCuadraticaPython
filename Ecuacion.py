import os


class ResolverEcuacion:
    def __init__(self,ecuacion): 
        directorio = "./archivos"
        try:
         os.mkdir(directorio)
        except OSError:  
             print("La creación del directorio %s falló" % directorio)
        else: 
           print("Se ha creado el directorio: %s " % directorio)
        file = open("./archivos/archivo.txt", "w")
        file.write(ecuacion)
        self.ecuacion=ecuacion
        file.close()
        print("En C++:")

        os.system(r"D:\SolucionCuadraticaPython\Solucionador.exe")

        print("En Python:")

        file = open("./archivos/respuesta.txt", "r")
        lineas=file.readlines()
        file.close()
        lineas=[file.rstrip('\n') for file in lineas]

        print("Respuesta:" )
        print(lineas)

        self.resultado=lineas


