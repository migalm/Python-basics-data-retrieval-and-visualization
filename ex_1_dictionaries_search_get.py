# Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

#==================================================Solicitud de ingreso de datos al usuario===============================================
#explicacion detallada sobre esta seccion disponible en los progrmas generados de los capitulos anteriores
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except (FileNotFoundError):
    print('Opss! el archivo no esta dentro de la carpeta, por favor ingrese un nombre de archivo valido')
    quit()

#==================================================proceso de informacion ==================================================================
#seleccion de informacion deseada, si la linea inicia con from se leera la misma===================
mbl=list() #se genera una lista para almacenar la informacion con todas las palabras
for line in fh: #por cada linea en el archivo proporcionado realizar:
    line=line.rstrip() #se cortan los saltos de renglon,  con rstrip(), ya que estos se ubican del lado derecho.
    if not line.startswith('From '): continue #se omiten todas las lineas que no inicien con 'From '
    words =line.split()#se separan todos los segmentos separados por espacios para ser considerados como cadenas independientes a cargar en la lista
    mbl.append(words[1])#se agregan todas las palabras ya separadas a la lista

#ciclo para agregar palabras nuevas al diccionario y realizar su conteo==============================
dnsend=dict()#se genera un diccionario bacio para almacenar y contar todas las palabras sin que estas se repitan
for sname in mbl:#ciclo para recorrer los valores en la cadena con las palabras
        dnsend[sname]=dnsend.get(sname,0)+1 #sentencia abreviada para de ciclo "if", evita el traceback realiza dos acciones al mismo tiempo, busca la "key (llave)""
                                            #con la palabra o la agrega, y suma un uno al valor cargada en la misma.

#print (dnsend)


#busqueda de la palabra con mayor conteo empleando doble variable de iteracion (tuole)===============

mname=None    #declaracion de variables en valor vacio
mcounter=None #declaracion de variables en valor vacio
for word,count in dnsend.items():   #se emplean dos variables de iteracion word y count para busqueda en cada uno de los items, es decir key y value, de el diccionario
    if (mcounter is None) or (count > mcounter): #ciclo que agrega a la cuenta de la variable mcounter o cambia el nombre de la variable mname si esta posee un mayor numero de conteo, basicamente modifica por el que tenga mas cuentas
        mname=word
        mcounter=count

print (mname,mcounter) #impresion de salidas requeridas

#ejemplos adicionales....=======
#stuff=dict()
#print stuff.get('candy',-1) # esta seccion hace que si la key no está, se coloque -1
