#This program executes a function capable to evaluate if the user enters a wrong number or value, it promts the error and only executes when the values are correct

#computepay function calculates the payrol based on the parameter 'h' and 'r', where 'h' are the worked hours and 'r' is the hourly rate. In the case of overtime, the function will calculate the respective amount of such overtime.
def computepay(h,r):
    try: #it evaluates if the imput is a string or a number
        h=float (h) #if the input is not a string it will be converted to float
        r=float (r) #same case as the line before
        if r<0 or h<0: #in the case the input is less than cero
            Print ('Error, inmput must be numbers above 0')
            quit() #end of the program
        if h>=0 and h<=40: #normal pay rol evaluation
    	    pay= h*r
        elif h>40: #when overtime have to be evaluated
            pay= (40*r) + (h-40)*(r*1.5)
        return pay #what the function returns as a numeric value or as none
    except: #in the case the input can not be converted to float it returns an error
        print ('Error, inmput must be numbers above 0')



hrs = input('Enter Hours:') #ask the user forthe hours
rate= input('Enter rate:') # ask the user for the hourlyrate
p = computepay(hrs,rate) #calls the fuction
if p==None: #this part eliminates the None result as an output
    quit()
elif p>=0: #this part prints the result of the function
    print (p)
