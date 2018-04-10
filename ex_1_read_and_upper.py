
#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file
#words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt
#=========================================Solicitud y manipulacion de datos proporcionados por el usuario=======================================

fname=input("Enter file name: ") #solicitud al usuiario de un nombre de archivo en la carpeta del programa
if len(fname) < 1: # en caso de que el usuario no ingrese algun valor se le asigna un archivo por default
    fname='words.txt'#nombre del arvhivo por default a leer en la carpeta del programa, notese como este de carga como una cadena

#validadas alguna de las condiciones anteriores se prosigue con la manipulacion de la infomracion proporcionada con un nombre de archivo valido

try:
    fh=open(fname)#con str.open(), se busca la posicion del archivo y se genera el enlace de la memoria ram a la memoria fija (disco duro, memoria de estado solido, etc...)
except (FileNotFoundError): #en el caso de que no se pueda realizar la apertura del archivo, devuelve un error de archivo no encontrado, para tomarlo e informar
#al usuario la situacion, se pone entre parentesis el nombre del error y se envia a impresion la nota al usuario
    print("Oops! no fue un nombre de archivo valido, intente nuevamente por favor")
    quit()


inp=fh.read()#con str.read(), se carga toda la cadena en la memoria flotante.
minp=inp.rstrip()#con rstrip, se eliminan las indiciaciones de salto de renglon al final de cada uno de estos "\n" ya que la funcion los elimina
upinp=minp.upper()#con str.upper(), se almacena una copia de la cadena procesada en la nueva variable asignada
print (upinp)#se envia a impresion el resultado ya en letras mayusuculas
