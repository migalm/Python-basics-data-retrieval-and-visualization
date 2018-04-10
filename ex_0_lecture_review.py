

import re

b = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
c = re.findall('\S+@\S+', b)
print (c)
#print y

hand=str()

fname = input("Enter file name: ")

if len(fname) < 1 : fname = "mbox-short.txt"
try:
    fh = open(fname)
except (FileNotFoundError):
    print('Opss! el archivo no esta dentro de la carpeta, por favor ingrese un nombre de archivo valido')
    quit()




#metodo neuvo
for line2 in hand:
    line2=line2.rstrip()
    if re.search('From: ', line2) :
        print (line2)

print ('marcador de separacion')

#hand= open(fname)
#metodo anterior
for line in hand:
    line =line.rstrip()
    if line.find('From: ')>=0:
        print (line)

#anadir inteligencia a las sentencias mediante el empleo de la re

print ('segundo marcador de separacion')
hand= open(fname)
for exline in hand:
    exline= exline.rstrip()
    if re.search('^From: ', exline): #la flecha hacia arriba
        print (exline)

#empleando re.findall
x='My 2 favoritenumbers are 19 and 42'
y=re.findall('[0-9]+',x)
print (type(y))
print (y)
y=re.findall('[AEIOU]+',x)
print (y)
y=re.findall('[M]+',x)
print (y)

x='From: Using the: character'
y=re.findall('^F.+:',x)#esto significa, encuentre la seccion que inicia con F, seguida de al menos un valor, el que sea, hasta llegar a ":", en este caso, al haber dos coincidencias, se regresara la cadena mas larga
print (y)

y=re.findall('^F.+?:',x) #esto significa, encuentre la seccion que inicia con F, seguida de al menos un valor, el que sea, hasta llegar a ":", pero regresando la cadena mas corta.
print (y)

z=None
t=None
hand=open(fname)
for line3 in hand:
    line3=line3.rstrip()
    if re.search('From: ',line3):
        z=re.findall('\S+@\S+',line3)
        t=re.findall('@(\S+)', line3)  # Obtiene los dominios de los correos seguidos precedidos pro el signo @, lo que esta en parentesis es lo que se extrae, recordar que debe estar entre comillas
        #print z
        print (t)
w=None
print ('inicio de ciclo final')
hand=open(fname)
numlist=list()

for line4 in hand:
    line4=line4.rstrip()
    w=re.findall('^From: .*@([^ ]*)',line4)
    if len(w) != 1: continue #esta es la resticcion que se tiene que poner para saltar todos los espacios en blanco, aunque al parecer ocupa mas memoria
    print (w)
    numlist.append(w)
print (type(w))
print (numlist)
#    if re.search('From: ', line4):
#        w=re.findall('(\S+@\S+)', line4)# Obtiene los dominios de los correos seguidos precedidos pro el signo @, lo que esta en parentesis es lo que se extrae, recordar que debe estar entre comillas
#        print w
