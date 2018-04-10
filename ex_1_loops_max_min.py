#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.




print ("Enter a series of numbers to look for maximum or minimum or type -done- to exit de aplication")
largest = None #ingreso de variables base en valor vacio
smallest = None #ingreso de variables base en valor vacio
while True: #lazo a ejecutar mientras la condicion sea verdadera
    value = input("give a number: ") #toma de valores al usuario y los almacena en la variable value
    if value == "done": break #en caso de que el valor ingresado sea igual a done el progrma indica salir del lazo while

    try:    #condicion a evaluar verdadera o falsa para continuar con el programa o realizar excepcion
        value=float(value) #en caso de que sea posible convertir el valor ingresado a flotante, es decir, que no es una cadena con numeros
    except: #si la accion en try no se puede realizar se procede a generar la exepciona,qui nos damos cuenta de que el valor ingresado es diferente a un numero
        print ("Error, please ener a numeric value or done")#se le notifica al usuiario el error
        continue#esta parte es importante, ya que no queremos que se ejecuten condiciones  que sean verdaderas para el codigo, con continue, regresamos a la cima del lazo

    if largest is None: #se modifica el valor vacio al ingresado por el usuario, esta condicion puede ser cierta si no se pone continue en el except
        largest= value #se cambia el valor de largest al valor ingresado, se debe tener cuidado al ingresar cada variable, ya que puede haber herrores de tipografia
        #print ('larguest cambio a valor de ingreso')#marcadores para saber que seccion del programa se esta ejecutando
    elif smallest is None: #se modifica el valor vacio al ingresado por el usuario, esta condicion puede ser cierta si no se pone continue en el except
        smallest=value #se cambia el valor de smallest al valor ingresado
        #print ('smallest cambio a valor de ingreso')#marcadores para saber que seccion del programa se esta ejecutando
    elif value > largest:#en caso de que el valor sea mayor al ya almacenado inicialmente la variable modifica su valor por el ingresado
        #print ('cambio de valor a larguest')#marcadores para saber que seccion del programa se esta ejecutando
        largest= value#se cambia el valor de largest al valor ingresado
    elif value < smallest:#en caso de que el valor sea menor al ya almacenado inicialmente la variable modifica su valor por el ingresado
        #print ('cambio de smallest')#marcadores para saber que seccion del programa se esta ejecutando
        smallest=value#se cambia el valor de smallest al valor ingresado

print ("Maximum is: " ,largest) #impresion final de resultado maximo
print ("Minimum is: " ,smallest)#impresion final de resultado minimo
