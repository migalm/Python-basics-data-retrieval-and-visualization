#========llamamos a la libreria de "urllib" y "BeautifulSoup" para realizar conexiones a internet y organizar los datos en HTML===========================

import urllib.request, urllib.parse, urllib.error #realiza las conexiones con las paginas, automatiza los "sockets"
from bs4 import BeautifulSoup #organiza el HTML que contenga la pagina solicitada y facilita la obtencion de datos

#======================================solicitud de informacion al usuario===============================================================================

url = input('Enter URL: ')
if len(url) < 1: url="http://python-data.dr-chuck.net/known_by_Fikret.html"


pos= input('Enter position: ')
if len(pos)>1: pos=pos
elif len(pos)<1: pos=3

count = input('Enter count: ')
if len(count)>1: count= count
elif len(count)<1:
        count=4

#===========================================Puntero para lectura de informacion de la pagina============================================================

html = urllib.request.urlopen(url).read() #enlace "apuntador" y lectura con la pagina desedada, notese el .read() al final de la sentencia
soup = BeautifulSoup(html, 'html.parser') #se llama a BeautifulSoup para segmentar y organizar las instrucciones en HTML
tags = soup('a') #se carga las secciones que se desean obtener de la url provista por el usuario.
print ('Retrieving:',url) #impresion al usuario donde se indica de donde se esta obteniendo la primera informacion


#=========================================procesamiento de informacion para solucion del problema========================================================

#conversion de valores iniciales recividos o por default para manipulacion de los mismos
pos=int(pos)  #conversion a entero para la poscion deseada de busqueda
count=int(count) #conversion a entero para el conteo de la cantidad de veces requeridas para repeticion de busqueda


while count > 0: #ciclo a repetir mientras la variable count sea mayor a cero
    impsal2=tags[pos-1]#se convierte en la tercera posicion de la cadena que se nos provee, ya que las posiciones de la lista comienzan a contar desde cero
    url2=impsal2.get('href', None) #se decalra a url2 igual al valor del enlace "link" en la posicion ingresada por el usuario o por default
    print ('Retrieving:',url2) #se envia a imprimir el "link" al que se le esta dando seguimiento
    #print impsal2
    html2 = urllib.request.urlopen(url2).read() #enlace "apuntador" y lectura con la pagina desedada, notese el .read() al final de la sentencia
    soup2 = BeautifulSoup(html2, 'html.parser') #se llama a BeautifulSoup para segmentar y organizar las instrucciones en el HTML de la pagina
    tags = soup2('a') #aqui, tags cambia sus valores por el de la nueva pagina, al iniciarse el nuevo ciclo, los valores de busqueda seran estos
    count=count-1 #se disminuye en uno el conteo ingresado o por default, una vez que llega a cero, se para la busqueda
