



def nomina (hours,rate):  #def se emplea para crear funciones o subrutinas en otros lenguajes de programacion, de inicio no se corre, pero lo reliza cuando se le llama
    if hours <= 40:        #se cargan todos los comando que se deben realizar con los valores de entrada de esta funcion
        paga = hours * rate
    else:
        exhours = hours - 40
        exrate = float (rate * 1.5)
        paga = (40 * rate )+ exhours * exrate
    return paga        #esto es lo que regresa la funcion, por eso el comando de return
#hasta aqui el programa corre, pero no ejecuta, guarda todo lo que "def" le ha señalado en la memoria.
try:
    hours = float(input("horas: "))
    rate = float (input("tarifa: "))
    x=hours #puede ser incluso el mismo nombre el valor que se ponga en la funcion, pero se desea enfatizar que el nombre de la variable solo importa dentro de esta
    y=rate # "x" y "y" se cambian para ingresarlas al momento de llamar a la funcion
except:
    print ("Error, please enter numeric imput")
    quit()

z = nomina(x,y) #se llama a la funcion dando los valores de ingreso "x" y "y".
print (z)
