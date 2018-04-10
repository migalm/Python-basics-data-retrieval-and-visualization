#========llamamos a la libreria de "sqlite3" para poder cargar los datos recopilados a una base de datos========================================================================

import sqlite3 #Biblioteca que realiza el procesamiento de los datos en sqlite3
import re

conn = sqlite3.connect('orgdb.sqlite') #le solcita a sqlite3 generar la base de datos con este nombre 'emaildb.sqlite', la crea en caso de no existir
cur = conn.cursor() #solicitamos un cursor para ingresar datos y ejecutar comandos hacia la base de datos

 #la triple comilla " ''' " indica una cadena multilinea
cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
#el texto dentro de la cadena multilinea indica: si, no existe una tabla con el nombre counts, creala,con el "contrato" donde incluya las dos columnas siguientes, 'email', y 'count'
#siendo los anteriores limitados a ser texto, o numero entero respectivamente.
fname = input('Enter file name: ')  #solicita al usuiario la entrada de el nombre de un archivo para procesamiento
if (len(fname) < 1): fname = 'mbox.txt' #en caso de que solo se presione Enter, sin valor alguno, el archivo que se cargara por default sera 'mbox-short.txt'
fh = open(fname) #con str.open(), se busca la posicion del archivo y se genera el enlace de la memoria ram a la memoria fija (disco duro, memoria de estado solido, etc...)
for line in fh: #para cada renglon almacenada en cada una de las posiciones de la cadena proporcionada por fh realizar:
#=====El objetivo se puede conseguir empleando dos metodos, con "regular expresions" o separando dos veces el conetenido recolectado con el metodo .split para cadenas=============
#=====primer metodo con 'regular expresions'==================================
    #line = line.rstrip() #se recortan los espacios los saltos de renglon \n antes y despues
    #org0 =re.findall('^From: .*@(\S+)', line) #encuentra con 'regular expresions' donde inicia 'From: ' seguido de cualquier cosa hasta llegar a @, ahi inicia la extraccion hasta el espacio en blanco
    #if not org0: continue#si no cumple con la condicion de tener los solicitado por la expresion regular reinicia el ciclo
    #org=str(org0)#se convierte la lista a cadena para poder ingresarla en la base de datos y procesarla, resta saber como extraer la informacion sin las comillas y los corchetes

#=====segundo metodo con separacion doble empleando metodo .slit para cadenas ==================================
    if not line.startswith('From: '): continue #si la linea no empieza con la cadena 'From: ', continuar y reiniciar el ciclo
    pieces = line.split() #declara pieces igual a la segmentacion de la cadena en pequeñas cadenas individuales (palabras), se genera en base a los espacios existentes en el renglon
    email = pieces[1] #el correo es equivalente a la informacion contenida en la primera posicion de 'pieces'
    pieces2=email.split('@') #se separa nuevamente la cadena en base al signo de arroba
    org=pieces2[1] #se toma la segunda posicion de la nueva cadena creada, correspondiente a la seccion posterior al signo arroba


    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,)) #ejecutar dentro de sqlite3 el codigo de sql que indica: extrae el numero de 'count' en la tabla  Counts donde 'email'
    #sea igual al valor recuperado y colocado en la variable 'email'
    row = cur.fetchone()   # . fetchone obtiene un renglon de la base de datos, puede usarse para generar tuplas
    if row is None: #en caso de que no exista la columna
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,)) #ingresar los valores de (email,count) en la talba Counts, donde los valores son, el obtenido en la variable 'email' y 1 para 'count', notese aqui hay dos
                #'email' que se refieren a cosas distintas, uno es la variable y otro es el renglon dentro de la vase de datos.
    else: #en caso de que si exista en la base de datos
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,)) #ejectua en sqlite3: ingresa en la tabla 'Counts', actualiza el valor de count = count+1, donde email ='email'

conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10' #lee de la talba Counts los valores en las tablas email,count y ordenalas en orden descendente, con un limite de 10 valores

for row in cur.execute(sqlstr):  #para cada 'row' en la lista que se almaceno en la variable sqlstr
    print(str(row[0]), row[1]) #imprime el valor de 'row' en la posicion [0] y [1] de la cadena, correspondientes a 'email'y 'count'

cur.close() #cierra la comunicacion y archivo selecionado en sqlite3
