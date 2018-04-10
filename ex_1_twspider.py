
#========llamamos a la libreria de "urllib","json", "twurl" de charles serverance y "ssl" para conectar a internet, organizar los datos de JSON proporcionados por twitter=======
#========manejar las autorizaciones de twitter con "twurl" y los errores con "ssl"===============================================================================================
from urllib.request import urlopen
import urllib.error
import twurl  #biblioteca generada por charles serverance para manejar los codigos de autorizacion con twitter
import json  #Biblioteca que realiza el procesamiento de los datos en json y retorna un "arbol" de los mismos, en bibliotecas de python
import sqlite3  #Biblioteca que realiza el procesamiento de los datos en sqlite3
import ssl  # biblioteca para manejo de errores de certificacion

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'   #pagina para obtener listas de amigos con api de twitter

conn = sqlite3.connect('spider.sqlite') #le solcita a sqlite3 generar la base de datos con este nombre 'spider.sqlite', la crea en caso de no existir
cur = conn.cursor() #solicitamos un cursor para ingresar datos y ejecutar comandos hacia la base de datos

#la triple comilla " ''' " indica una cadena multilinea
cur.execute('''
            CREATE TABLE IF NOT EXISTS Twitter
            (name TEXT, retrieved INTEGER, friends INTEGER)''')
#el texto dentro de la cadena multilinea indica: si, no existe una tabla con el nombre twitter, creala,con el "contrato" donde incluya las tres columnas siguientes, 'name', 'retrieved' y 'friends'
#siendo los anteriores limitados a ser texto, numero entero y numero entero, respectivamente.

# Ignore SSL certificate errors
#====Instrucciones para ingorar errores de certificado SSL===========================================
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#====extraccion de informacion de twitter y carga a la base de datos, requiere token y secrets en el archivo hidden dentro de una carpeta donde este corriendo el programa=========================
while True: #mientras la condicion sea verdadera
    acct = input('Enter a Twitter account, or quit: ')  #solicita al usuiario la entrada de una cuenta de twitter e informa al usuario puede salir del ciclo ingresando quit
    if (acct == 'quit'): break #en caso de que la variable sea igual a la cadena 'quit': 'break' (salir del ciclo).
    if (len(acct) < 1): #en caso de que solo se presione Enter, sin valor alguno
        cur.execute('SELECT name FROM Twitter WHERE retrieved = 0 LIMIT 1') #ejecutar dentro de sqlite3 el codigo de sql que indica: extrae un 'name' dentro de la tabla twitter donde el valor en la
        #columna retrived sea igual a cero, 'retrieved=0' y limita esta seleccion a solo obtener un renglon, posteriormente esta informacion se va emplear para buscar.
        try:
            acct = cur.fetchone()[0] # . fetchone obtiene un renglon de la base de datos, [0] declara a acct como el valor de la primera columna en el renglon obtenido,
        except:
            print('No unretrieved Twitter accounts found') #en caso de que la recuperacion de informacion falle, envia el mensaje 'No unretrieved Twitter accounts found'
            continue #regresa al inicio del ciclo

    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '5'}) #biblioteca con tuplas de key:value, en "screen_name" se carga la pagina con la cuenta y en "acct" se carga un valor
    #predetermiado de "5" esta relacionada con la bibloteca twurl, ya que es un campo de ingreso a la misma
    print('Retrieving', url) #envia a impresion la cadena "Retrieving" + la "url"
    connection = urlopen(url, context=ctx)# puntero para leer la pagina regresa una cadena de valores, "calla" revisiones de seguridad en errores de certificado con 'context=ctx' para ssl
    data = connection.read().decode() #orden de lectura, es la representacion en cadena del "json", viene de internet, se tiene que codificar para cambiar de utf-8 al formato general de pyton: "unicode"
    headers = dict(connection.getheaders()) #declara "headers" como el diccionario donde se almacenan todos los headers con el comando getheaders() de "urllib", aplicado al puntero de la pagina solicitada

    print('Remaining', headers['x-rate-limit-remaining'])  #envia a impresion el valor de la key con nombre 'x-rate-limit-remaining', el limite para twitter es muy corto, cerca de 15 unicamente
    js = json.loads(data)  #carga la informacion recuperada en la variable js ya en formato "unicode" y genera un "arbol" de la misma en notacion json
    # Debugging
    # print json.dumps(js, indent=4)

    cur.execute('UPDATE Twitter SET retrieved=1 WHERE name = ?', (acct, )) #ejectua en sqlite3: ingresa en la tabla twitter, cambia el valor en la columna retrieved a 1 donde el nombre sea igual a 'acct'

    countnew = 0 #variables de conteo
    countold = 0
    #extraccion de la informacion para el usuario seleccionado.
    for u in js['users']: # para cada 'u', abreviatura para usuario, en la informacion que contiene js, ya ordenada, buca lo contenido en la key 'users'
        friend = u['screen_name']  #declara el valor de la key dentro de 'users' con el nombre 'screen_name'
        print(friend) #envia a impresion el valor en la variable 'friend'
        cur.execute('SELECT friends FROM Twitter WHERE name = ? LIMIT 1',
                    (friend, )) #ejectua en sqlite3: lee de la columna friends en la tabla twitter el valor de 'name' igual a 'friend'(puesto al final de la sentencia) y limitalo a 1
        try: #intenta
            count = cur.fetchone()[0] # . fetchone obtiene un renglon de la base de datos, [0] declara a 'count' como el valor de la primera columna en el renglon obtenido,
            cur.execute('UPDATE Twitter SET friends = ? WHERE name = ?',
                        (count+1, friend)) #ejectua en sqlite3: ingresa en la tabla twitter, actualiza el valor de 'friends' = count+1, donde el nombre del amigo ='friend'
            countold = countold + 1 #adiciona 1 a countold al termninar este ciclo.
        except:#en caso de falla
            cur.execute('''INSERT INTO Twitter (name, retrieved, friends)
                        VALUES (?, 0, 1)''', (friend, )) ##ejectua en sqlite3: ingresa en la tabla de twitter, los valores para  'name, retrieved, friends' los valores de: 'name' igual a 'friend'(puesto
                        #al final de la sentencia), 0 para retrieved y 1 para friends.
            countnew = countnew + 1 #adiciona 1 a countnew al termninar este ciclo.
    print('New accounts=', countnew, ' revisited=', countold) #envia a impresion el valor de las nuevas cuentas y las revisitadas.
    conn.commit() # genera la transaccion en sqlite3

cur.close()#cierra la comunicacion y archivo selecionado en sqlite3
