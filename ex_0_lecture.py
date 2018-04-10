#lists
#lists is a kind of collection.
#a collection allow us to put many values in a single "variable"
#a collection is nice because we can carry all many values around in one convenient package.
#https://docs.python.org/3/tutorial/datastructures.html

#Example
friends=['Joseph','Glenn','Sally']
print (friends)
carryon=['socks','shirt','perfume']  #no se esta poniendo : al final de esta sentencia
#simple variables are not collections, you can't put more than one thing in them
#lsit constants are surrounded by square brakets and the elements in the list are separated by commas
#a list element can be any python object, even an other list
#a list can be empty.

print ([1,24,76])
print (['red','yellow','blue'])
print (['red',25,98.6])
print ([1,[5,6],'7'])#esta se reconoce como una lista con 3 elementos
print ([])

#like in strings we can look for information inside the lists, we have to remember that count will
#start on cero.
#example

print (friends [1])
#strings are not mutable, they do not change.
lotto=([2,14,26,41,63])
print (lotto)
lotto [2]=28
print (lotto)

#how long is a list?

greet='Hello Bob'
print (len(greet))
x=[1,2,'joe',99]
print (len(x))

#range function, it produces a list and give it back to us
print (range(4))#lo que hace rango es generar una lista de secuencial iniciando en cero y posterior incrementa
#de uno en uno hasta llegar al numero, sin incluir el mismo, que se le asigne en el programa
print (len(friends))
print (range(len(friends)))
print (range(len(friends)+1))

#dos formas de generar un lazo para asignacion de datos
for friend in friends:
    print ('Happy new year: ', friend)

for i in range(len(friends)):
    friendv=friends[i]
    print ('Happy new year: ', friendv)

#concatenation
a=[1,2,3]
b=[4,5,6]
c=a+b
print (c)
print (a)

#we can ---slice--- strings
#example
t=[9,41,12,3,74,15]
print (t[1:3])
print (t[:4])
print (t[3:])
print (t[:])

#Methods - kind of built in functions

z=list()
print (type(z))
print (dir(z))

#we can increase a list by adding information to the tale
#example using append method

stuff=list()
print (type(stuff))
stuff.append('book')
stuff.append(99)
print (stuff)
stuff.append('cookie')
print (stuff)

#checking information.
some=[1,9,21,10.16]
print (some)
print (9 in some)
print (15 in some)
print (20 not in some)

#lists have order, a list can hold many items and keeps those items in the order until we do something
#to change the order
#example using ---sort--- method. indicates the list to sort itself

friends.sort()
print (friends)
print (friends[1])

#Example of aplications of built in functions to lists.

nums=[3,41,12,9,74,15]
print (nums)
print (len(nums))
print (max(nums))
print (min(nums))
print (sum(nums))
print (sum(nums)/len(nums))

#two ways of creating acumulating paterns, normal count and variable asignation vs ---sum---lenn---methods
#------------------------------------------------------------------------------------------------------
#this loop uses little memory space
total=0
count=0
#while True:
#    uinp=raw_input('Enter a number: ')
#    if uinp=='done': break
#    value=float(uinp)
#    total=total+value
#    count=count+1
#average=total/count
#print (average)



#this loop uses more memory space
numlist=list()
#while True:
#    u2inp=raw_input('Enter a number: ')
#    if u2inp=='done':break
#    value2=float(u2inp)
#    numlist.append(value2)
#average2=sum(numlist)/len(numlist)
#print (average2)
#------------------------------------------------------------------------------------------------------
#using ---split--- method
abc='with three words'
stuff2=abc.split()
print (stuff2)
print (len(stuff2))
print (stuff2[0])
for w in stuff2:
    print (w)
 #------------------------------------------------------------------------------------------------------

line='A lot             of spaces'
etc=line.split()
print (etc)
line2='first;second;third'
thing=line2.split()
print (thing)
print (len(thing))
thing=line2.split(';')
print (thing)
print (len(thing))


fhand=open('mbox-short.txt')
mbl=list()
for line in fhand:
    line=line.rstrip()
    if not line.startswith('From'): continue
    words =line.split()
    print (words[1])
    sect=words[1]
    secmbl=sect.split('@')
    mbl.append(secmbl[1])

#print mbl
for y in mbl:
    print (y)
#for ex in mbl:
#    print (ex[1])
