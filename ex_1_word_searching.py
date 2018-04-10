
#Busqueda y orden de palabras dentro de un archivo para posterior arreglo de manera alfabetica empleando sort

#Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method.
#The program should build a list of words. For each word on each line check to see if the word is already in the list and if not
#append it to the list. When the program completes, sort and print the resulting words in alphabetical order.


fname= input("Enter file name: ")#se le solicita al usuiario ingresar un nombre de archivo, se tiene que recordar que termine con extension ".txt"
if len(fname)<1: fname='romeo.txt'#condicional en caso de que no se ingrese un valor y se presione enter, se carga el nombre del archivo por default
try:#verifica que el archivo se pueda abrir
    fh=open(fname)#comando para realizar la apertura del archivo
except (FileNotFoundError): #en el caso de que no se pueda realizar la apertura del archivo, devuelve un error de archivo no encontrado, para tomarlo e informar
                            #al usuario la situacion, se pone entre parentesis el nombre del error y se envia a impresion la nota al usuario
    print("Oops! no fue un nombre de archivo valido, intente nuevamente por favor")#Nota al usuario sobre el error
    quit()#indicacion de terminacion del programa

lst = list()#se genera una lista para agregar todas las palabras
ouplst=list()#se genera otra lista para procesamiento de la primera ouput list, se tiene que crear una nueva lista de comparacion y en base a esta
             #filtrar y agregar en caso de que no se encuentre en la misma

for line in fh:#se recorren todos los renglones del archivo con for recorriendo al apuntador "fh"
    line=line.rstrip()#se eliminan los saltos de renglon al final de cada  renglones
    words=line.split()#se toman todos los datos en la cadena y se vuelven valores independientes en cada una de las posiciones de una lista
    lst=lst+words#se suma a una lista general las nuevas palabras de cada renglon analizado de manera secuencial

for sword in lst:#se revisa cada una de las palabras para evaluar si se encuentran en la lista anterior
    if sword not in ouplst:#si la palabra no se encuentra en la lista de salida, se agrega
        ouplst.append(sword)#comando para agregar un nuevo dato a la ultima posicion de la lista

#print ouplst
ouplst.sort() #comando para organizar automaticamente una lista de manera alfabetica
print (ouplst) #se envia a impresion el resultado
