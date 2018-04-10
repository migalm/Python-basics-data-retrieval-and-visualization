#================================llamamos a la libreria de "json" para realizar el "arbol" a partir de lenguaje JSON ============================================
import json #Biblioteca que realiza el procesamiento de los datos en json y retorna un "arbol" de los mismos, en bibliotecas de python
#=======================================================Datos en forma de JSON ==================================================================================
#la triple comilla " ''' " indica una cadena multilinea

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}''' #JSON de ejemplo

#=======================================Busqueda con "json" dentro de la cadea en lenguaje JSON ===================================================================

info = json.loads(data) #con el comando json.loads("informacionaprocesar") se genera un diccionario separando cada uno de los elementos y se le asigna su valor,
                        #semejante a un "arbol".
#print (type(info))     #comprueba que el valor retornado es un diccionario

print('Name:', info["name"])    #impresion de cadena 'Name' seguido de la cadena en el diccionario con el valor de key igual a 'name', notese, son dos cosas distitntas
print('Hide:', info["email"]["hide"]) #impresion de cadena 'Hide' seguido de la cadena en el diccionario con el valor de key igual a 'hide', que pertenece a la key igual a "email"
