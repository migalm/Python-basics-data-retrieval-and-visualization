#3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use raw_input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

hours = float( input("horas :"))   #recibe la cantidad de horas que ingresa el usuario
rate = float (input("tarifa :"))   #recibe la cantided de paga por hora
#exhours = 0                       #Se declara horas extras como cero, aunque puede no ser necesario declarala desde el inicio, esta parte se puede comentar u omitir
bcexhrs =40                        #la cantidad de horas base si es necesaria, ya que es la base para ralizar la suma total de la paga requerida
if hours <= bcexhrs:                    #primera de dos condiciones, en caso de que la cantidad de horas sea menor a 40, se genera una multiplicacion sencilla como resultado
    paga = (hours * rate)          #se envia el resultado a impresion
elif hours > bcexhrs:                   #en caso de que la cantidad de horas sea mayor a 40, se procede con este ciclo condicional
    exhours = hours - bcexhrs           #las horas extras son el resultado de la diferencia de horas totales ingresadas menos las horas base
#    exrate = float (rate * 1.5)         #se convierte el resultado de la paga a flotante, aunque por el hecho de poner el "." en la multiplicacion deberia ser automatico
    exrate = rate * 1.5                 #ejemplo de como en efecto, por la multiplicacion con punto se realiza la conversion a flotante automaticamente
    paga = (bcexhrs * rate )+ exhours * exrate #se realiza el calculo total de la paga sumando las horas extra
print (paga)                            #se envia a impresion el resultado obtenido
