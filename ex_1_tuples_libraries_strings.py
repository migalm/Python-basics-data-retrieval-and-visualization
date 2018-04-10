#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the
#'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

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
#count=None
mbl=list() #creacion de lista en blanco
for line in fh: #para cada una de las lineas en el archivo a procesar:
    line=line.rstrip() #remocion de salto de renglon colocado al lado derecho, con el comando 'str.rstrip()'
    if line ==[]: continue#se agrega un "guardian" debido a la condicion existente donde puede existir un renglon en blanco y causa un error en el programa, si existe, se omite y se continua
    if not line.startswith('From '): continue
    words =line.split() #toma cada linea de lectura que nos interesa
#    count=count+1#contador de repeticiones del ciclo, 27 en este caso
#    print (words[5]#impresion para debuging de el resultado obtenido)
    cohour=words[5]
    sihour=cohour.find(":")# Da la posicion en la que se encuentra por primera vez el simbolo ":" ( de dos puntos) con el comando str.find('str')
    chhour=cohour[:sihour] #asinga el valor desde que inicia la cadena cohours (que ya solo contine la hora, hasta la posicion donde de encuentran los dos puntos.
    mbl.append(chhour)#obtengo la seccion de horas que se encuentra en la 5 posicion contando desde cero
#print (count)

#conteo de horas repetidas agregando la informacion que se tiene en la varible mbl a un diccionario
dnsend=dict()
for sname in mbl:#por cada valor en la lista mbl:
        dnsend[sname]=dnsend.get(sname,0)+1 #comando para agregar y contar en caso de que no se encuentre en el diccionario 'dnsend' el valor leeido en la lista mbl
#print (dnsend)

#impresion ordenada de los valores agregados al diccionario
for word,count in sorted(dnsend.items()):   #se emplean dos variables de iteracion word y count para busqueda en cada uno de los items, es decir key y value, de el diccionario y se agrego el comando sorted para ordenarlos
    print (word,count)                        #de menor a mayor antes de aplicarles el ciclo for, este comando es muy util porque evita mayor escritura de codigo, posterior se envian a impresion.
