from genericpath import exists



vocales:str="aeiouAEIOU"
print("a" in vocales)
# tarea
#averiguar que son y cuales son los operadores unarios, binario,ternario 



#metdos para convertir un texto en mayuscula
texto:str="hola"
print(texto.upper())
# metodo para convertir un texto en minuscula 
texto:str="HOLA"
print(texto.lower())
# metodo para convertir solo la primera letra en mayuscula
texto:str="buenos dias"
print(texto.capitalize())
# metodo para conertir la primera letra de cada palabra en mayuscula como un titulo
texto:str="buenos dias"
print(texto.title())
# metodo para quitar espacios
texto_espacio:str="     osos      " 
print(texto_espacio)
# este metodo quita los espacios que estan en la izquierda y derecha , si deseamos quitar solo los espacios solo de la izquierda usamos el metodo lstrip()y si deseamos quitar solo de la derecha usamos rstrip()
print(texto_espacio.strip())

# metodo para buscar un caracterer o conjunto de caracteres 
parrafo:str="mi mama me ama yo amo a mi mama gianfranco"
print(parrafo.find("gianfranco"))
print(parrafo[35:])

# metodo para remplazar una parte de texto
texto_incorrecto:str="gianfranco es malo"
print(texto_incorrecto.replace("malo","bueno"))
# (metodo) operador binario de existencia 
## este operador verifica si ci
