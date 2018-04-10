
#programa de Busqueda
#6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.


text = "X-DSPAM-Confidence:    0.8475"; #texto proporcionado
indgno= text.find(":")#con la funcion ya incorporada dentro de python str.find(), se encuentra la seccion de la cadena que tiene ":"
gno= text[indgno+1:] #con este slicing, o corte, se secciona la parte que se desea de informacion dentro de la cadena, que es, desde una posicion posterior a ":" hasta el final de la cadena.
pgno =float(gno) #se convierte la seccion obtenida de la cadena a un numero flotante
print (pgno) #se imprime el resultado obtenido de la conversion a flotante
