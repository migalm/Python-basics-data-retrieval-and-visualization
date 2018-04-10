#Ejericios del capitulo 12 se obtiene informacion de una pagina web, solo se solicta que se cargue la informacion obtenida,
#pero se busco la forma de mandarla a guardar a un archivo de texto
#=======================================================Descripcion del ejercicio=========================================================================
#Exploring the HyperText Transport Protocol
#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

#http://data.pr4e.org/intro-short.txt
#There are three ways that you might retrieve this web page and look at the response headers:
#Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data. Make sure to change the code to retrieve the above URL - the
#values are different for each URL.
#Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
#Use the telnet program as shown in lecture to retrieve the headers and content.
#Enter the header values in each of the fields below and press "Submit".

#==================================llamamos a la libreria de "socket" para realizar conexiones a internet==================================================

import socket #importamos la libreria socket

#==================================================conexion con el servidor de internet empleando socket====================================================

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #le decimos al programa que queremos conectarnos a internet y que vamos a enviar y recivir informacion
mysock.connect(('data.pr4e.org', 80))       #le indicamos a donde queremos conectarnos y que puerto vamos a usar, se emplea el 80 normalmente para http
cmd=cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() #ahora si, le indicamos a donde queremos que extienda la conexionm notese el "\r\n\r\n" al final
mysock.send(cmd)

#carga en una lista de la infomracion enviada por el servidor ==============================

numlist=list()      #numlist es una lsita de carga de informacion

while True:                             #mientras se cumpla la validez del ciclo
    data = mysock.recv(512)             #la inforomacion que se reciva de mysoc, en bloques de 512 caracteres
    if ( len(data) < 1 ) :              #si no se recibe informacion, salir del ciclo, este es importante, para poder salir del ciclo
        break                           #salida del ciclo
    numlist.append(data.decode())       #agrega a la lista lo que se lea de la pagina asignada una vez terminada la lectura de los 512 caracteres
    print (data.decode())               #imprime la informacion obtenida
mysock.close()                          #termina la conexion

#carga de la informacion obtenida en un archivo de texto====================================

fname = "docescritura.txt"  #estring con el nombre del archivo donde queremos que se guarde la informacion recuperada
hand= open(fname,"w")       #comando open (str.,(argumento)),  str. es la cadena del nombre del archivo y el argumento puede ser r,w o a, por read (que solo lee)
                            #write(borra lo existente y escribe los datos nuevos proporcionados) y append (escribe agrega la nueva informacion al final del archivo).

for w in numlist:           #para cada uno de los valores de cadenas en la lista numlist
    hand.write(w)           #escribe en el archivo declarado como hand lo que leas
    #print (w)              #imprime en el simbolo del sistema para confirmar la realizacion del ciclo
hand.close()                #cierra el archivo





#import urllib
#fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
#for line in fhand:
# print (line.strip())
