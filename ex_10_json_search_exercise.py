
#-----------------------------------------------importacion de librerias necesarias para el programa-----------------------------------------------------------
import urllib
import urllib.request, urllib.parse, urllib.error
import json
#-----------------------------------------------solicitud de informacion al usuario----------------------------------------------------------------------------

serviceurl = 'http://python-data.dr-chuck.net/geojson?'#se asgna una pagina por default para completarla con la universidad que proveea el usuario

while True:
    address = input('Enter location: ') #solicitud de ingreso por el usuario en python 3 solo se pone input, en vez de raw_input
    if len(address) < 1 : break #si no se ingresa un valor, el programa se sale del while y termina
    url = serviceurl + urllib.parse.urlencode({'sensor':'false', 'address': address})# se toma la pagina de base serviceurl1 y se le agrega al codigo, la condicion de falso +  lo que
                                                                                      #ingrese el usuario separado por signos&
    print ('Retrieving', url)#se muestra al usuario la pagina de donde se obtiene la informacion
    uh = urllib.request.urlopen(url)#con la libreria urllib se genera el puntero para saber de donde se puede leer la pagina
    data = uh.read() #se lee la informacion en la pagina regresa una cadena de valores
#    print (data) #se puede enviar a impresion para observar la cadena completa
    print ('Retrieved',len(data),'characters') #como ya es una cadena se puede pedir que nos de la longitud de la misma
    try: info = json.loads(data) #info es un diccionario con una cadena que contiene otro diccionario, el observar esto perimite hacer la siguietne declaración que es qinfo=info['results'][0]['place_id']
    #esto en el cso de que se pueda obtener la carga, se envia al renglon 27, qinfo=info['results'][0]['place_id'] #en caso de haber informacion  en caso contrario el programa salta al except:
    except: info = None # en csao de que no se reciba informacion se procede a realizar el ciclo condicional if
    if 'status' not in info or info['status'] != 'OK': # en caso de que la condicion de estatus no este en info o la seccion de status no sea igual a ok, se envia a imprimir Failure
       print ('==== Failure To Retrieve ====')
       continue #se envia la ejecucion a la parte superior del while
#    print (json.dumps(info, indent=4))
    qinfo=info['results'][0]['place_id'] #en caso de haber informacion se obtiene el dato requerido colocando entre corchetes las secciones a donde se desea que 'descienda' nuestro 'buscador
    print (qinfo)#se imprime el resultado
