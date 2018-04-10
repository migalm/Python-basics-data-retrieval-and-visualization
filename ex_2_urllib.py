#==================================llamamos a la libreria de "urllib" para realizar conexiones a internet==================================================
import urllib.request, urllib.parse, urllib.error #urllib es una manera abreviada de emplear socket

#==================================================conexion con el servidor de internet empleando urllib===================================================

fhand=urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt') #Este comando enlaza al archivo sin leerlo, es como el open empleado en el capitulo 11,
                                                                     #es un puntero, pero en vez de ser a un archivo es a una dirección de internet.

#procesa la infomracion enviada por el servidor, convirtiendola a Unicode y recortandola para enviarla a impresion ==============================

for line in fhand: #ejecutar el siguiente codigo para cada una de las lineas en la pagina que indica el puntero fhand
    print (line.decode().strip()) # para la linea "line" convertirla de utf-8  a Unicode, posterior eliminar extremos vacíos, o, con indicación de salto de pagina (en
                                  # ambos lados)
