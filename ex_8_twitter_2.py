#========llamamos a la libreria de "urllib","json", "twurl" de charles serverance y "ssl" para conectar a internet, organizar los datos de JSON proporcionados por twitter=======
#========manejar las autorizaciones de twitter con "twurl" y los errores con "ssl"===============================================================================================
import urllib.request, urllib.parse, urllib.error #realiza las conexiones con las paginas, automatiza los "sockets"
import twurl  #biblioteca generada por charles serverance para manejar los codigos de autorizacion con twitter
import json #Biblioteca que realiza el procesamiento de los datos en json y retorna un "arbol" de los mismos, en bibliotecas de python
import ssl  # biblioteca para manejo de errores de certificacion

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json' #pagina para obtener listas de amigos con api de twitter

# Ignore SSL certificate errors
#====instrucciones para ingorar errores de certificado SSL===========================================
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#====codigo para extraccion de informacion de twitter, requiere token y secrets en el archivo hidden dentro de una carpeta donde este corriendo el programa=========================
while True: #mientras la condicion sea verdadera
    print('')  #imprime un renglon en blanco
    acct = input('Enter Twitter Account:') #solicita al usuiario la entrada de una cuenta de twitter
    if (len(acct) < 1): break #en caso de no ingresarse una cuenta de twitter, con break, el programa sale del lazo
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'}) #biblioteca con tuplas de key:value, en "screen_name" se carga la pagina con la cuenta y en "count" se carga un valor predetermiado de "5"
                        #esta relacionada con la bibloteca twurl, ya que es un campo de ingreso a la misma
    print('Retrieving', url) #envia a impresion la cadena "Retrieving" + la "url"
    connection = urllib.request.urlopen(url, context=ctx) # puntero para leer la pagina regresa una cadena de valores, "calla" revisiones de seguridad en errores de certificado con 'context=ctx' para ssl
    data = connection.read().decode() #orden de lectura, es la representacion en cadena del "json", viene de internet, se tiene que codificar para cambiar de utf-8 al formato general de pyton: "unicode"

    js = json.loads(data) #carga la informacion recuperada en la variable js ya en formato "unicode" y genera un "arbol" de la misma en notacion json
    print(json.dumps(js, indent=2)) #envia a impresion las secciones recuparadas en js, dandoles sangria de dos espacios para mayor claridad

    headers = dict(connection.getheaders())  #declara "headers" como el diccionario donde se almacenan todos los headers con el comando getheaders() de "urllib", aplicado al puntero de la pagina solicitada
    print('Remaining', headers['x-rate-limit-remaining']) #envia a impresion el valor de la key con nombre 'x-rate-limit-remaining', el limite para twitter es muy corto, cerca de 15 unicamente

    for u in js['users']: # para cada 'u', abreviatura para usuario, en la informacion que contiene js, ya ordenada, buca lo contenido en la key 'users'
        print(u['screen_name']) #envia a impresion el valor de la key dentro de 'users' con el nombre 'screen_name'
        if 'status' not in u: #si no hay una key con nombre 'status' dentro de la key 'users'
            print('   * No status found') #envia a imporesion : no se encontro un status
            continue #reinicia el ciclo
        s = u['status']['text'] #ingresa dentro de la varialbe  la sumatiora de los valores de cadena que corresponden a los valores de las key 'status' + 'text'
        print('  ', s[:50]) #imprime dos espacios en blanco y adiciona los primeros 50 valores enontrados en la cadena de la variable s
