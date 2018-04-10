fruit="banana" # se declara a banana como string (cadena)
x=len(fruit) #con la funcion incorporada (built in) se determina la longitud de la cadena asignada, que en este caso es de 6
print (x) #se imprime el resultado obtenido, 6
#===========================================ejemplo de ciclo while para recorrer cadenas (strings)=============================================================
index=0 #se declara la variable index igual a cero
while index<len(fruit):#este es un lazo definido que se ejecuta mientras se tenga un valor menor que la longitud de la cadena "fruit" en la variable index
    letter=fruit[index]#esta seccion asigna a la variable cambiante letter el valor de la cadena en la posicion index (index inicia en cero)
    print (index, letter)#se envia a impresion la variable index y la letra de la cadena que ha sido asignada a la variable letter
    index=index+1# se incrementa el valor de index en uno, de manera que se recorra toda la longitud de la cadena almacenada en la variable fruit.

#===========================================ejemplo de ciclo while para recorrer cadenas (strings)=============================================================

for letb in 'banana': #ciclo for que resume lo realizado en el aterior ciclo while
    print (letb) # solo se emplea una sentencia de impresion de variable de iteracion, ya que al emplear in dentro de for con una cadena, recorre toda esta "[:]"

count=0 #este emplea un contador de coincidencias, aunque me parece que se puede emplear una funcion
for letc in fruit: #se emplea la variable de iteracion letc para recorrer la cadena en la variable fruit
    if letc=='n': #condicional que compara el valor dentro de la cadena con la letra "n"
        count=count+1 #incrementa la cantidad de la variable desde cero hasta el valor total de coincidencias encontradas
print (count)# imprime el resultado almacenado en la variable count

#===========================================ejemplo de ralizacion de slicing==================================================================================

namech='Monty python'#almacena la cadena en la variable namech
print (namech[0:4])#imprime la palabra Monty, hay que recordar que las cadenas inician su valor de iterancion desde cero
print (namech[6:7])#imprime la letra p, ejemplifica que lo marcado entre corchetes incluye el valor al lado izquierdo y todos aquellos valores dentro de la cadena hasta
#llegar al valor de la cadena marcado al lado derecho del corchete, sin incluir el valor de este mismo, en este ejemplo, como el 7 precede directamente al 6, solo se
#imprime la p
print (namech[6:20])#en el parentesis se incluye donde iniciar y donde terminar, pero, python termina de iterar donde termina la cadena, aunque el programador se
#equivoque y ponga un numero mayor a la longitud de la cadena del lado derecho del ":" dentro de los corchetes.
print (namech[:2])#indica, inicia en 0 y termina en 2 sin incluirlo
print (namech[8:])#esta instruccion significa, inicia en la posicion 8 y termina hasta la ultima posicion
print (namech[:])#si se dejan en blanco, significa ya sea, el inicio, del lado izquierdo, y el final, del lado derecho.

#====================================================concatenacion de cadenas==================================================================================

pal1='hello' #almacena la cadena en la variable pal1
pal2=pal1+'there' #suma la cadena 'there' a la variable pal1
print (pal2) #el resultado del mismo une las dos cadenas, aunque, sin un espacio entre ambas
pal3=pal1+' '+'there' # en esta ocacion se almacena en pal3, la concatenacion de la variable pal1 se le agrega un espacio y despues se le agrega la cadena 'there'
print (pal3)#el resultado es 'hello there', aqui si se incluye el espacio

#============================================operadores logicos con la expresion "in" aplicados a cadenas=========================================================

'n' in fruit #consulta la existencia de la letra "n" en la variable "fruit"
'm' in fruit #consulta la existencia de la letra "m" en la variable "fruit"
'nan' in fruit #consulta la existencia de la cadena0 "nan" en la variable "fruit"
if 'a' in fruit: #condiconal de busqueda
    print ('found it') #consulta la existencia de la letra "a" en la variable "fruit" y envia a impresion en caso de cumplirse esta condicion

#===========================================operaciones matematicas, modificaciones y consulta de fuciones incorporadas a las cadenas============================

print (len(fruit)*7)  #len retorna la longitud de la cadena como un numero entero y se multiplica esta longitud por el numero deseado, en este caso es 7
print (fruit.upper()) #se envia a impresion una copia de la cadena en la variable "fruit", con upper, toda la cadena se copia con la version en mayusculas de la misma
print (dir(fruit)) #se solicita el directorio disponible para las caracteristicas de la cadena almacenada en la variable "fruit", este arroja las variables locales
#y las fuciones incorporadas

#===========================================busqueda y extraccion de informacion dentro de las cadenas==========================================================

text = "X-DSPAM-Confidence:    0.8475"; #texto proporcionado
indgno= text.find(":")#con la funcion ya incorporada dentro de python str.find(), se encuentra la seccion de la cadena que tiene ":"
gno= text[indgno+1:] #con este slicing, o corte, se secciona la parte que se desea de informacion dentro de la cadena, que es, desde una posicion posterior a ":" hasta el final de la cadena.
pgno =float(gno) #se convierte la seccion obtenida de la cadena a un numero flotante
print (pgno) #se imprime el resultado obtenido de la conversion a flotante
