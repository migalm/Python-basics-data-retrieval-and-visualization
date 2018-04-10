
#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

try: #condicion a evaluar, el valor ingresado por el usuario debe ser un numero
    grade = float(input("enter grade : ")) #se toma el numero ingresado por el usuario y se convierte en flotante
    if grade <0 or grade > 1:
        quit()
except:#se corre la excepcion en caso de no ser un numero
    print ('Error, please enter a number in the range between 0.0 and 1.0') # se envia al usuiario la notificacion de las restricciones de programa
    quit() #se sale del programa

if grade >= 0.9:  #condicion mayor o igual a 0.9
    print ("A") #imprime la letra A
elif grade >= 0.8:#condicion mayor o igual a 0.8
    print ("B") #imprime la letra B
elif grade >= 0.7: #condicion mayor o igual a 0.7
    print ("C") #imprime la letra C
elif grade >= 0.6: #condicion mayor o igual a 0.6
    print ("D")#imprime la letra D
#elif grade <  0.6 and grade >= 0: #condicion igual o menor a 0.6
else:
    print ("F") #imprime la letra F
