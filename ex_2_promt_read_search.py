
#7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use
#the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.
#=========================================Solicitud y manipulacion de datos proporcionados por el usuario=======================================

fname=input("Enter file name: ") #solicitud al usuiario de un nombre de archivo en la carpeta del programa
if len(fname) < 1: # en caso de que el usuario no ingrese algun valor se le asigna un archivo por default
    fname='mbox-short.txt'#nombre del archivo por default a leer en la carpeta del programa, notese como este de carga como una cadena
                          #validada esta condicion se prosigue con la manipulacion de la infomracion proporcionada con un nombre de archivo valido
try: #se intenta realizar la apertura del archivo, par esto, el mismo debe estar en la carpeta asignada al programa
    fh=open(fname) #con str.open(), se busca la posicion del archivo y se genera el enlace dee la memoria ram a la memoria fija (disco duro, memoria de estado solido,
                   #etc...)
except (FileNotFoundError): #en el caso de que no se pueda realizar la apertura del archivo, devuelve un error de archivo no encontrado, para tomarlo e informar
                            #al usuario la situacion, se pone entre parentesis el nombre del error y se envia a impresion la nota al usuario
    print("Oops! no fue un nombre de archivo valido, intente nuevamente por favor")#Nota al usuario sobre el error
    quit()#indicacion de terminacion del programa

count=0 #inicializacion de variable de conteo
sno=0   #inicializacion de variable de suma de numeros "sno"
for sline in fh: #indicacion para realizar rastreo dentro del archivo con ciclo for, y variable de iteracion sline
    if not sline.startswith('X-DSPAM-Confidence:'): #para cada seccion entro del archivo, con el puntero, se revisa si esta inicializa o no con las palabras deseadas
        continue #en caso de que no inicie con las palabras deseadas se descarta la linea a leer
    else: #analisis de caso contrario, la informacion que se obtuvo es la deseada
        count=count+1 #se suma un 1 al valor de conteo
        indgno=sline.find(':') #se busca en el renglon de iteracion la poscion dentro de la cadena donde se encuentra (:)
        gno=sline[indgno+1:] #con slicing, se secciona la informacion deseada dentro de la cadena, que es, desde una posicion posterior a ":" hasta el final de la cadena.
        pgno =float(gno) # se convierte la seccion de cadena obtenida a numero flotante
        sno=sno+pgno #se actualiza el valor de sumatoria, sno, sumando el valor original + el recien obtenido de la conversion de la seccion de cadena a numero

av = sno/count #se obtiene un promedio mediante  
print ("Average spam confidence:",av )     #se envia a impresion el resultado ya en letras mayusuculas
