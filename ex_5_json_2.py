#================================llamamos a la libreria de "json" para realizar el "arbol" a partir de lenguaje JSON ============================================
#this program was developed for chalres serverance and modified to make it run by Miguel Laguna to run properly as a homework activitie.

import json #Biblioteca que realiza el procesamiento de los datos en json y retorna un "arbol" de los mismos, en bibliotecas de python

#=======================================================Datos en forma de JSON ==================================================================================
#la triple comilla " ''' " indica una cadena multilinea

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]'''#JSON de ejemplo

#=======================================Busqueda con "json" dentro de la cadea en lenguaje JSON ===================================================================

info = json.loads(data) #con el comando json.loads("informacionaprocesar") se genera un diccionario separando cada uno de los elementos y se le asigna su valor,
                        #semejante a un "arbol".
print('User count:', len(info)) #como es un diccionario se puede solicitar el tamaño del mismo con el comando len()

for item in info: #ciclo para impresion de secciones de los diccionarios generados por la funcion json.loads()
    print('Name', item['name']) #impresion de cadena 'Name' seguido de la cadena en el diccionario con el valor de key igual a 'name', notese, son dos cosas distitntas
    print('Id', item['id'])  #impresion de cadena 'Id' seguido de la cadena en el diccionario con el valor de key igual a 'id', notese, son dos cosas distitntas
    print('Attribute', item['x']) #impresion de cadena 'Attribute' seguido de la cadena en el diccionario con el valor de key igual a 'x', notese, son dos cosas distitntas
