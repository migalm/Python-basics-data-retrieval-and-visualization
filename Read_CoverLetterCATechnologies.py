
#7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. Use the file
#words.txt to produce the output below.
#You can download the sample data at http://www.pythonlearn.com/code/words.txt
#=========================================Solicitud y manipulacion de datos proporcionados por el usuario=======================================

fname=input("Enter file name: ")
if len(fname) < 1:
    fname='CA_CoverLetter_MiguelLaguna.txt'
try:
    fh=open(fname)
except (FileNotFoundError):
    print("Oops!, the file wasn´t found, please try again")
    quit()
inp=fh.read()
minp=inp.rstrip()
print (minp)
