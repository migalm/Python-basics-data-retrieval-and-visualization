
#================================llamamos a la libreria de "ElementTree" para realizar el arbol a partir dl XML============================================
import xml.etree.ElementTree as ET  #genera "arboles" a partir de el xml con el que trabaje

#=======================================================Datos en forma de XML==============================================================================
#la triple comilla " ''' " indica una cadena multilinea
input = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>''' #XML de ejemplo

#=======================================Busqueda con "ElementTree" dentro del XML=========================================================================

stuff = ET.fromstring(input)  #En este caso la varibale se llama stuff, devuelve un elemento de "arbol" de la variable input
lst = stuff.findall('users/user') #tree.findall encuentra todos los valores con nombre'user' dentro de 'users'
print('User count:', len(lst)) #como ya es una lista se pueden emplear los metodos disponibles para este tipo de datos como len('lista') que regresa la longitud de la misma

for item in lst: #recorre todos los valores dentro de la lista para impresion de los datos deseados de cada 'mini' arbol
    print('Name', item.find('name').text) #tree.find solo encuentra uno de los valores con 'name', al poner .text se le indica que regrese el valor del texto en name
    print('Id', item.find('id').text) #tree.find solo encuentra uno de los valores con 'id', al poner .text se le indica que regrese el valor del texto en name
    print('Attribute', item.get("x")) #tree.find solo encuentra uno de los valores con 'Attribute', al poner .get('x') se le indica que regrese el valor del atributo indicado : '2 o 7'
