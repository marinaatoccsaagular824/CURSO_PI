lista_vacia : list = []
print(len(lista_vacia)) 
#python regla el nombre de la vareable no debe tener el tipo de dato que se va almacenar 
amores:list¨[str]=['wicho','perce']
print(len)
frutas:lista[str]=[ 🍎,🍌,🍒,🍑]
#pocicion o indice
#acider al tercer elemento
print(frutas[2])
#acceder al 2 elementos por su indece negativo 
print(fruta[-3])
## modeficar el ultimo elemento con Naranja
frutas[-1]="🍊"
print

##acceder por rango

# aceder por rango 
El acceso por rango permite extraer un subconjunto de datos secuenciales a partir de una lista o secuencia, utilizando sus posiciones inicial y final en lugar de buscarlos uno por uno.
Para entenderlo sin utilizar tablas o listas estáticas, imagina una frutería organizada en una sola fila continua, donde cada fruta tiene una posición numérica asignada.
Ejemplo práctico:
Tienes una fila con \(8\) frutas ordenadas de la siguiente manera:
🍎
🍐
🍌
🍊
🍊
🥝
🍇
🥭
Si quieres acceder al rango desde la posición 3 hasta la 6, la regla general se estructura de la siguiente manera: Rango [Inicio : Fin]
Inicio: Posición (3) (🍌)Fin: Posición (6) (🥝).
Resultado del rango: Plátano, Naranja, Mandarina, Kiwi En programación, lenguajes como Python utilizan el índice base (0). Si la lista comienza en el número (0) (🍎), el rango se define como ([2:6]). 

##remplazo de elementos de  remplazo de eleminar por slicing
num_pares:list[int]=[1,3,5,6,10]
print(num_pares)
num_pares[0:3]=[2,4]
print (f"mi lista modeficada es:{num_pares}")



