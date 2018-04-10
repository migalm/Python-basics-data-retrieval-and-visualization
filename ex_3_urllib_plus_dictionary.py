#==================================llamamos a la libreria de "urllib" para realizar conexiones a internet==================================================
import urllib.request, urllib.parse, urllib.error #urllib es una manera abreviada de emplear socket

#==================================================conexion con el servidor de internet empleando urllib===================================================

counts = dict() #se genera el diccionario counts
fhand = urllib.request.urlopen('http://www.py4inf.com/code/romeo.txt') #Puntero hacia la dirección de internet.


for line in fhand: #por cada valor encontrado en la pagina del puntero fhand
    words = line.split() #Genera una lista de cadenas separando cada linea "line" perteneciente a los valores de fhand
    for word in words:   #por cada cadena encontrada en cada linea perteneciente a los valores del puntero fhand
        counts[word] = counts.get(word,0) + 1 #comando para agregar y contar en caso de que no se encuentre en el diccionario 'counts' el valor leeido en la lista words
print (counts) #impresion del diccionario
