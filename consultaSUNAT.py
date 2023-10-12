#se importan las librerias que vamos a utilizar
#ESTOS SE TIENEN QUE DESCARGAR ANTES CON PIP POR CONSOLA SI NO NO SE PRODRÁ IMPORTAR
from bs4 import BeautifulSoup as BS #libreria para hacer el scrapping
from selenium import webdriver #controlar el navegador de forma remota y automatica
from selenium.webdriver.common.by import By #encontrar elementos de DOM
from selenium.webdriver.support import expected_conditions as EC #esperar a eventos para que siga el codgigo
from selenium.webdriver.chrome.options import Options as opt
from selenium.webdriver.support.ui import WebDriverWait


#!!!!!!AUTOMATIZACIÓN!!!!!

#codigo para que el navegador se NO cierre automaticamente
#ESTO ES PARA VERIFICAR INFORMACION O CONTROL DE ERRORES NO ES NECESARIO
#EN EL CASO DE QUE QUIERAS ELIMINARLO O PROBAR ELIMINARLO, BORRAS LAS DOS LINEAS Y QUITAS EN PARAMETRO DE driver
#YO lo voy a comentar porque no lo necesito
"""
chrome_options=opt()
chrome_options.add_experimental_option("detach", True)
"""
#llamo al driver
driver = webdriver.Chrome() #aqui se le pasa el parametro chrome_options para hacerlo valido

"""
en esta parte se le pide al driver que abra la pagina del enlace con el metodo get
y despues se le pide que busque el elemento por el XPATH (By.XPATH) '//*[@id="txtRuc"]'
con el metodo find_element. se busca con el por el xpath para ser más preciso
y se le envie la clave que esta dentro del metodo send_keys
"""
driver.get('https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp')

numeroRUC = driver.find_element(By.XPATH,'//*[@id="txtRuc"]')

numeroRUC.send_keys(input('digita el RUC:'))

"""
en este pedaso de codigo creo un metodo para clickear el boton "manualmente" en lugar de 
utilizar el metodo submit(). esto con el fin de evitar ser detectado como bot por el reCAPTCHA

"""
#se localiza el boton al que le quiero dar click
botonEnviar = driver.find_element(By.XPATH,'//*[@id="btnAceptar"]')
#se le indica al programa que lo precione con el metodo click()
botonEnviar.click()

"""
aqui se utiliza la libreria webdriverwait para detener el codigo hasta que aparezca
los elementos que me interesan
"""
WebDriverWait(driver, 30).until(EC.presence_of_all_elements_located((By.CLASS_NAME,'list-group-item-text')))

#!!!!!!WEBSCRAPING!!!!!!

"""
aqui se utiliza la libreria BeautifulSoup pasandole el parametro'.page_source'(selenium)
para poder realizar acciones con el codigo fuente html de la pagina
tambien se le pasa el parametro'html.parser' para poder analizar el codigo html
"""
soup = BS(driver.page_source, 'html.parser')

#aqui se utiliza el metodo find_all para buscar todos los elementos que se encuentran dentro de la clase
datos = soup.find_all(class_="row")

#recorremos cada elemento encontrado para imprimirlo
#PERO se especifica que solo muestre los elementos que no contengan un button dentro de ellas
for dato in datos:
    if not dato.find('button'):
        print(dato.text)