
#========llamamos a la libreria de "urllib" y "JSON" para realizar conexiones a internet y organizar los datos de JSON proporcionados por google =======
#this program was developed for chalres serverance and modified to make it run by Miguel Laguna to run properly as a homework activitie.

import urllib.request, urllib.parse, urllib.error  #realiza las conexiones con las paginas, automatiza los "sockets"
import json #Biblioteca que realiza el procesamiento de los datos en json y retorna un "arbol" de los mismos, en bibliotecas de python

# Note that Google is increasingly requiring keys
#mas informacion de como funciona el api de google en la siguiente liga.
#  https://developers.google.com/maps/documentation/geocoding/start
# for this API
serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?' #pagina de servicio de google

while True: #ciclo de repeticion para busqueda de informacion
    address = input('Enter location: ') #solicita al usuario ingresar la direccion y la almacena en forma de cadena
    if len(address) < 1: break #en caso de que no se proporcione una direccion, termina el ciclo con "break"

    url = serviceurl + urllib.parse.urlencode({'address': address}) #une la pagina "API", con la cadena que le propociono el usuario
     #se genera una cadena con una biblioteca donde la llave es "addess" y el valor es lo contenido en la variable es la url asinganda, urllib.parse.ulencode separa estos valores y pone entre ambos un signo de igual "=", este valor puede ser enviado a impresion, saldra todo junto. ademas, se genera la codificacion del mismo para proporcinar este mismo en utf-8 hacia Internet.

    print('Retrieving', url) #se envia a impresion la variable url, notese como aparece la "adress" + "=" + "la url por default o la ingresada
                             #por el usuario"
    uh = urllib.request.urlopen(url)  #puntero para leer la pagina regresa una cadena de valores
    data = uh.read().decode() #lectura de datos proporcionados por la "API" + "parametros de busqueda ingresados" notese el .read() al final, tambien es psosible  uh = urllib.request.urlopen(url).read()
    print('Retrieved', len(data), 'characters')  #se envia a impresion "Retrieved"+"longitud de la cadena", empleando len() + "characters"

    try: #dos casos posibles
        js = json.loads(data) #intenta cargar al informacion, si es posible salta al ciclo if posterior a except, caso contrario salta directamente a "except",
    except:
        js = None #al entrar a la excepcion se declara js como valor nulo

    if not js or 'status' not in js or js['status'] != 'OK': #esto dice: si js==false, o el valor "status" no esta en js, o si el valor dentro de ["status"] es diferente de OK, ejecuta los siguiente
        print('==== Failure To Retrieve ====') #envia a imprimir, falla en la recuperacion
        print(data) #imprime lo proporcionado por la "API"
        continue #regresa al inicio del ciclo while

    print(json.dumps(js, indent=4)) #envia a impresion las secciones recuparadas en js, dandoles sangria de cuatro espacios para mayor claridad

    lat = js["results"][0]["geometry"]["location"]["lat"] #entra a buscar la key "results", la latitud en la posicion cero de la lista con la biblioteca que contiene geometry/location/lat
    lng = js["results"][0]["geometry"]["location"]["lng"] #entra a buscar la key "results", la longitud en la posicion cero de la lista con la biblioteca que contiene geometry/location/lng
    print('lat', lat, 'lng', lng) #imprimer los resultados sustraidos de longitud y latitud
    location = js['results'][0]['formatted_address'] ##entra a buscar la key "results", la "formatted_address" en la posicion cero de la lista con la biblioteca que contiene formatted_address
    print(location) #imprimer los resultados sustraidos de la direccion con formato
