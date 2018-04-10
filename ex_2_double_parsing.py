#8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
#Hint: make sure not to include the lines that start with 'From:'.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt


fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt" #condicional en caso de que no se ingrese un valor y se presione enter, se carga el nombre del archivo por default

try:#verifica que el archivo se pueda abrir
    fh=open(fname)#comando para realizar la apertura del archivo
except (FileNotFoundError): #en el caso de que no se pueda realizar la apertura del archivo, devuelve un error de archivo no encontrado, para tomarlo e informar
                            #al usuario la situacion, se pone entre parentesis el nombre del error y se envia a impresion la nota al usuario
    print("Oops! no fue un nombre de archivo valido, intente nuevamente por favor")#Nota al usuario sobre el error
    quit()#indicacion de terminacion del programa

fh = open(fname)#generacion de marcador para lectura de documento
count = 0#inicializacion de variable "count" a cero
mbl=list()#se declara mbl como lista
for line in fh:#ciclo a ejecutar para las lineas en el archivo fh
    line=line.rstrip()#a cada linea en el archivo se le remueve el salto de linea
    if not line.startswith('From '): continue#en caso de que la linea no inicie con "From" se descarta
    words =line.split() #se separa la cadena y se almacena en una lista con el comando split
    print (words[1])#se envia a imprimir la palabra almacenada en la posicion 1, que es la segunda de izquierda a derecha
    count=count+1#se agrega uno al contador
print ("There were", count, "lines in the file with From as the first word")
