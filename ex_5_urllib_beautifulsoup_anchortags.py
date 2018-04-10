#========llamamos a la libreria de "urllib" y "BeautifulSoup" para realizar conexiones a internet y organizar los datos en HTML==================

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#==================================================conexion con el servidor de internet empleando urllib==========================================

url = input('Enter - ') #se solicita al usuario ingreso de pagina a analizar
html = urllib.request.urlopen(url).read() #enlace "apuntador" y lectura con la pagina desedada, notese el .read() al final de la sentencia
soup = BeautifulSoup(html, 'html.parser') #se llama a BeautifulSoup para segmentar y organizar las instrucciones en HTML

# Retrieve a list of the anchor tags
# Each tag is like a dictionary of HTML attributes

numlist=list() #generamos una lista donde cargaremos los valores, posteriormente los sumaremos y los contaremos con ayuda de los comandos len('list') y sum('list')

tags = soup('span') #se obtienen con soup las etiquetas 'span', tags es un elemento de soup que "indica" donde se encuentra el elemento buscado, se puede solicitar impresion: print (type(tags)

for tag in tags: #ciclo para busqueda en cada renglon de la variable deseada
    #print (tag.get('href', None)) #si hay una pagina de internet, devuelve el resultado, caso contrario, regresa el valor None
    #print ('TAG:',tag) #TAG, se refiere a toda el tema que comprende el ancla que en este caso es "span"
    #print ('URL:',tag.get('href', None)) #envía a impresion la pagina en caso de que exista, con el comando tag.get, precedido de la cadena 'URL' en la pantalla de comandos
    #print ('Contents:',tag.contents[0]) #se imprime el valro extraido cargado en la ancla, ya que este toma la posicion '0' de la lista
    chv=int(tag.contents[0])  #comando para convertir a entero la cadena obtenida en la posicion cero de la lista
    numlist.append(chv) #cargamos el nuevo valor a la lista numlist

print (len(numlist)) #se envia a imprimir la longitud de la lista con la funcion len
print (sum(numlist)) #se envia a imprimir la suma de la lista con la funcion sum
