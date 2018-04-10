#===============Indicaciones del profesor Charles Serverance, se puede colocar el archivo de BeautifulSoup en la carpeta y correrlo============
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#========llamamos a la libreria de "urllib" y "BeautifulSoup" para realizar conexiones a internet y organizar los datos en HTML==================

from urllib.request import Request, urlopen
import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup
import ssl


#====instrucciones para ingorar errores de certificado SSL===========================================
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#====Codigo para busqueda y retorno de información de "tags" tipo "a"(paginas de internet)============
url = input('Enter - ') #solicitud de ingreso de pagina de busqueda al usuario
req = urllib.request.Request(url,data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }) #=========this part is important not to be confused with a bott, user agent eliminates the error 403 = urllib.error.HTTPError: HTTP Error 403: Forbidden==========
html = urllib.request.urlopen(req).read() #enlace y lectura con la pagina desedada, notese el .read() al final de la sentencia

soup = BeautifulSoup(html, 'html.parser') #se llama a BeautifulSoup para segmentar y organizar las instrucciones en HTML

# Recuperacion de todos los "tags" ancla, en este caso "a"
tags = soup('a') #se recurre a la funcion soup para recuperar los "tags" tipo "a", lo cual regresa una lista
for tag in tags:  #para cada una de las cadenas en tags
    print(tag.get('href', None)) #solicita obtener las referencias(paginas) dentro de cada una de las cadenas dentro de la lista
