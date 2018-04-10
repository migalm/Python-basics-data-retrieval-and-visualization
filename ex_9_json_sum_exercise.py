
#-----------------------------------------------importacion de librerias necesarias para el programa-----------------------------------------------------------
import json
import urllib.request, urllib.parse, urllib.error
#-----------------------------------------------solicitud de informacion al usuario----------------------------------------------------------------------------
adress = input('Enter URL: ')
if len(adress) < 1: adress="http://py4e-data.dr-chuck.net/comments_2579.json"

#-----------------------------------------------Puntero para lectura de informacion de la pagina------------------------------------------------------------------

url = urllib.parse.urlencode({'address': adress})  #une la pagina "API", con la cadena que le propociono el usuario
 #se genera una cadena con una biblioteca donde la llave es "addess" y el valor es lo contenido en la variable es la url asinganda, urllib.parse.ulencode separa estos valores y pone entre ambos un signo de igual "=", este valor puede ser enviado a impresion, saldra todo junto. ademas, se genera la codificacion del mismo para proporcinar este mismo en utf-8 hacia Internet.
print('Retrieving', url)

uh = urllib.request.urlopen(adress)#se genera el puntero para saber de donde se puede leer la pagina
data = uh.read()#se lee la informacion en la pagina regresa una cadena de valores
print('Retrieved', len(data), 'characters')#como ya es una cadena se puede pedir que nos de la longitud de la misma

info = json.loads(data)  #info es un diccionario con una cadena que contiene otro diccionario, el observar esto perimite hacer la siguietne declaración que es requinfo = info['comments']
#print (info) #se puede activar para ver lo que esta pasando en el programa, el dicionario tiene un tuple que contiene la cadena con varios diccionarios en ella en la seccion de comments
#print (type(info))#comando para verificar que esta variable es un diccionario
reqinfo = info['comments'] #se declara la variable solicitando se cargue con la informacion que viene asignada a comments
#print(reqinfo) se puede enviar a imprimir para ver la separacion que ha tenido el diccionario inicial
vsum=int() #variables de conteo declaradas como enteros
vsum=0     #inicializacion de valor para suma a cero
count=int
count=0
for item in reqinfo:
    #print('name', item['name'])#obtiene el valor de name en cada biblioteca en los argumentos de la cadena en que estos se encuentran inmersos y lo envia a imprimir
    #print('count', item['count'])#obtiene el valor de count en cada biblioteca en los argumentos de la cadena en que estos se encuentran inmersos y lo envia a imprimir
    tval=int(item['count'])
    count=count +1
    vsum=vsum+tval
print ('Count: ',count)
print ('sum:', vsum) #impresion del resultado
