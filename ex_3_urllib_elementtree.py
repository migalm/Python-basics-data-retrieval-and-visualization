
#este problema estuvo dificil por el descnocimiento del retonro de la orden item.find('nombredeelementobuscadehtml').txt, este comando regresa un tuple.

#========llamamos a la libreria de "urllib" y "ElementTree" para realizar conexiones a internet y organizar los datos en XML que estan en la pagina asgnada =======

import urllib.request, urllib.parse, urllib.error #realiza las conexiones con las paginas, automatiza los "sockets"
import xml.etree.ElementTree as ET #genera "arboles" a partir de el xml con el que trabaje

#================================================solicitud de informacion al usuario===============================================================================
adress = input('Enter URL: ')
if len(adress) < 1: adress= "http://py4e-data.dr-chuck.net/comments_2578.xml"

#-----------------------------------------------Puntero para lectura de informacion de la pagina------------------------------------------------------------------

url = urllib.parse.urlencode({'address': adress}) #se genera una cadena con una biblioteca donde la llave es "addess" y el valor es lo contenido en la variable es la url asinganda, urllib.parse.ulencode separa estos valores y pone entre ambos un signo de igual "=", este valor puede ser enviado a impresion, saldra todo junto.

#urllib.parse.urlencode(query, doseq=False, safe=”, encoding=None, errors=None, quote_via=quote_plus)
# Convierte un objeto de mapeo o una secuencia de dos elementos tupla, que pueden contener caracteres tipo cadena o objetos bytes, a una cadena  porcentaje-codificado tipo ASCII.  si la cadena resultante se va a emplear como datos para impresion.


print('Retrieving', url)                                #se envia a impresion la variable url, notese como aparece la "adress" + "=" + "la url por default o la ingresada
                                                        #por el usuario"
uh = urllib.request.urlopen(adress).read() #se genera el puntero para saber de donde se puede leer la pagina y se lee la informacion en la pagina regresa una cadena de valores, todo en el mismo comando, notese el .read() al final
print('Retrieved', len(uh), 'characters')#como ya es una cadena se puede pedir que nos de la longitud de la misma
tree = ET.fromstring(uh)                                #se solicita a la biblioteca element tree que separe como tal los elementos que se encuentran en el xml
#counts = tree.findall('comments/comment')              #esta linea y la siguiente funcionan de igual forma, hay que poner atencion en que se busca comment y no count
counts = tree.findall('.//comment')                     #se tiene que dar como referencia elemento complejo, es decir el que puede tener mas dentro de el para encontrar
                                                        #el elemento simple que se busca
                                                        #el retorno de tree.findall es una lista de valores que indican el nombre y la posicion por lo cual cada valor de
                                                        #esta lista es un tuple
print ('count:',len(counts))                            #como es una lista se le puede pedir que de la longitud de la misma
vsum=int()                                              #variables de conteo declaradas como enteros
vsum=0                                                  #inicializacion de valor para suma a cero

for item in counts:
    #print('count', item.find('count').text) #se puede enviar a imprimir, pero solo funciona asi, por eso se puede dar uno cuenta del error si lo considera como un valor independiente y no un tuple
    bval=('count', item.find('count').text)#lo tengo que trabajar forzosaente como un tuple, si no causa problemas...:(
    tval=int(bval[1])
    vsum=vsum + tval

print ('sum:', vsum) #impresion del resultado
