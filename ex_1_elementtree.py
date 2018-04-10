
#================================llamamos a la libreria de "ElementTree" para realizar el arbol a partir dl XML============================================
import xml.etree.ElementTree as ET #genera "arboles" a partir de el xml con el que trabaje

#=======================================================Datos en forma de XML==============================================================================
#la triple comilla " ''' " indica una cadena multilinea
data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
     +1 734 303 4456
   </phone>
   <email hide="yes"/>
</person>''' #XML de ejemplo

#=======================================Busqueda con "ElementTree" dentro del XML=========================================================================

tree = ET.fromstring(data) #En este caso la varibale se llama tree, pero puede tomar el nombre que desee el programador, devuelve un elemento de "arbol"
print('Name:', tree.find('name').text) #tree.find solo encuentra uno de los valores con 'name', al poner .text se le indica que regrese el valor del texto en name
print('Attr:', tree.find('email').get('hide')) #tree.find solo encuentra uno de los valores con 'email', al poner .get('hide') se le indica que regrese el valor del atributo indicado : 'yes'
