#El programa recibe la infomracion de usuario para la paga, se evalua si los valores de entrada son numeros, en caso contrario se le notifica al usuario que
#existe un error y se le solocita ingresar valores adecuados para el calculo de la infomracion
try:    #condicion requerida para continuar con los ciclos if
    hours = float(input("horas: ")) #se recibe infomracion del usuario
    rate = float (input("tarifa: "))#se recibe infirnacuin dek usuario
    exhours = 0#se inicializan los valores (horas extra : exhours)
    bcexhrs = 40#se inicializan los valores (base de horas : bcexhrs)
except: #en caso de que no se cumpla lo arriba mencionado salir del programa
    print ("Error, please enter numeric imput") #previo a salir se imprime erro, por favor ingrese un valor numerico
    quit()#salida del programa

if hours <= 40:#condicional, si el tiempo es menor a 40 horas realizar la siguiente multiplicacion
    paga = hours * rate#multiplicacion a realizar en caso de que el numero de horas sea menor a 40 horas
else:#caso contrario, descartar el primer if y continuar con los comando que se encuentran debajo, recordar que en python la sangria si tiene significado
    exhours = hours - 40#obtiene la diferencia de horas entre las regulares y las que deben ser pagadas con tiempo extra
    exrate = float (rate * 1.5)# genera la multiplicacion en flotantes del ascenso en costo de la paga
    paga = (bcexhrs * rate )+ exhours * exrate #suma la paga nomral mas las horas extra requeridas

print (paga)#imprime el resultado de la paga
