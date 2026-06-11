#crear una lista de 10 animales vertibrados y 5 invertibrados el orden ser aliatorios,tendreas que hacer los seguentes corecciones 
"""
1. modeficar los 3 elementos aves.
2. modeficar el 6 y el ultimo elementos por repeteles.
3. modeficar el elemento 8 por gianfranco.
4. mostrar toda la lista nueva con las modificaciones .

# 1. Definir los conjuntos de animales.
vertebrados = ["Vaca", "Oso", "Ballena", "Salamandra", "Loro", "Jirafa", "Pingüino", "Canguro", "Cocodrilo", "Tigre"]
invertebrados = ["Cangrejo", "Estrella de mar", "Mosca", "Araña", "Lombriz"]
# 2. Unir y mezclar de forma aleatoria (15 elementos en total)
lista_animales = vertebrados + invertebrados


print(list coriginal(oden aliatoria
for i, animal in enumerate(lista_animales, 1):
    print(f"{i}. {animal}")

print("\n" + "-"*40 + "\n")

# 3. Aplicar las correcciones requeridas (Python usa índice desde 0)
# Corrección 1: Modificar el elemento 3 (índice 2) por un ave
lista_animales[2] = "Canario (Ave)"

# Corrección 2: Modificar el elemento 6 (índice 5) y el último (índice 14) por reptiles
int("📋 LISTA ORIGINAL (Orden aleatorio):")
for i, animal in enumerate(lista_animales, 1lista_animales[5] = "Tortuga (Reptil)"
lista_animales[14] = "Camaleón (Reptil)"

# Corrección 3: Modificar el elemento 8 (índice 7) por gianfranco
lista_animales[7] = "gianfranco"

# 4. Mostrar toda la lista nueva con las modificaciones
print("🔄 LISTA NUEVA CON LAS MODIFICACIONES:")
for i, animal in enumerate(lista_animales, 1):
    # Resaltar visualmente los cambios en la consola
    if i in [3, 6, 8, 15]:
        print(f"{i}. {animal} <-- [MODIFICADO]")
    else:
        print(f"{i}. {animal}")

