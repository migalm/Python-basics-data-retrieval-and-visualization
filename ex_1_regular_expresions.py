
#finding Numbers in a Haystack
#In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers.
#Data Files
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt (There are 90 values with a sum=445833)
#Actual data: http://py4e-data.dr-chuck.net/regex_sum_2574.txt (There are 97 values and the sum ends with 342)
#These links open in a new window. Make sure to save the file into the same folder as you will be writing your Python program. Note: Each student will have a distinct data file for the assignment - so only use your own data file for analysis.
#Data Format
#The file contains much of the text from the introduction of the textbook except that random numbers are inserted throughout the text. Here is a sample of the output you might see:
#Why should you learn to write programs? 7746
#12 1929 8827
#Writing programs (or programming) is a very creative
#7 and rewarding activity.  You can write programs for
#many reasons, ranging from making your living to solving
#8837 a difficult data analysis problem to having fun to helping 128
#someone else solve a problem.  This book assumes that
#everyone needs to know how to program ...
#The sum for the sample text above is 27486. The numbers can appear anywhere in the line. There can be any number of numbers in each line (including none).
#Handling The Data
#The basic outline of this problem is to read the file, look for integers using the re.findall(), looking for a regular expression of '[0-9]+' and then converting the #extracted strings to integers and summing up the integers.

#Turn in Assignent

#Enter the sum from the actual data and your Python code below:
#Sum:
# (ends with 342) Submit Assignment
#Python code:


#==================================llamamos a la libreria de "regular expresions - re"==================================================
import re

#==================================================Solicitud de ingreso de datos al usuario===============================================
#explicacion detallada sobre esta seccion disponible en los progrmas generados de los capitulos anteriores
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex_sum_2574.txt"
try:
    fh = open(fname)
except (FileNotFoundError):
    print('Opss! el archivo no esta dentro de la carpeta, por favor ingrese un nombre de archivo valido')
    quit()

#lectura de archivo y generacion de lista con comando re.findall()==============================
arch=open(fname)  #teniendo el archivo el programa se solicta su nombre para abrirlo, es solo un puntero a su posicion en la memoria
imp=arch.read() #se carga todo en la variable imp,aqui si lo lee y lo carga en la memoria
w=re.findall('[0-9]+',imp) # se recurre a la libreria re.findall para separar las secciones que deseamos tener, mencionando que queremos todos aquellos datos que
                           # contengan uno o mas datos de manera secuencial

#conversion de valores de lista a numeros y suma en lazo for ===================================

numlist=list() #generamos una lista donde cargaremos los valores,
for value in w:  #para cada valor de la lista en w
     numlist.append(int(value))
print (sum(numlist))

#sum(numlist)
#len(numlist)

#==============================opciones alternativas===========================================

#print sum
#print count

#w=None
#numlist=list()
#for line in arch:
    #line=line.rstrip()
#    w=re.findall('[0-9]+',line)
#    if len(w) != 1: continue #esta es la resticcion que se tiene que poner para saltar todos los espacios en blanco, aunque al parecer ocupa mas memoria
#    print w
    #w=float(w)
#    numlist.append(w)

#print type(w)
#print numlist
#a=sum(w)
#b=len(w)
#print a
#print b

#============================================================================================
#sum=int()  #declaramos tener variables para suma y conteo en los lazos,
#count=int() #
#numlist=list()#generamos una lista donde cargaremos los valores, aunque no la ocupe, no recuerdo como sumar dentro de la lista XD debo revisar esto
#chv=None # se inicializa cvh, el programa corrio, pero pudo haberse declarado mejor como entero, int()
#for value in w: #para cada valor de la lista en w
    #chv=int(value) #el valor de la variable de iteracion debe ser el valor de la lista en la posicion secuencial que le corresponda
    #numlist.append(chv) #cargamos a la nueva lista, no se recordaba como ocuparlo inicialmente, pero posterior se quedo la version corta con sum y len para cadenas
    #sum=sum+chv #suma de manera continua cada dato tan pronto entra al lazo
    #count=count+1# suma la cantidad de datos que son ingresados al lazo
