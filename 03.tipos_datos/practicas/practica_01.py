una freriteria tiene separada em dos litas los siguentes
1. listas de pruductos de limpieza (10)productos
productos_limpieza = ( Lejía,Detergente,jabón líquido,Desinfectante,Alcohol,Quita grasa,Ambientador,Esponjas,Trapo industrial)

 2. Lista de materiales de construcción
materiales_construccion = (Cemento,Arena fina, Fierro 1/2,Yeso,Tubos PVC)
--------------------------------------------------------------
el dueño desea realizar las siguientes  las siguientes accio0nes:
1.en su lista de pruduccion de liempeza exixte un material de construcioon , deves eliminarlo y eliminar al lista que corrwespomde.
if in productos_limpieza:
    productos_limpieza.remove("producto_lempieza")
    print("productos_limpieza")

2. indicar si en la lista de M.C esxixten cemento.
if "Cemento" in materiales_construccion:
    print( "materiales_construccion")
else:
    print(" materiales_construccion")

3. en la lista de P.L buscar elpruducto lejia y cambiar su valor por la lejia sapolio.
if "Lejía" in productos_limpieza:
    indice = productos_limpieza.index("Lejía")
    productos_limpieza[indice] = "Lejía Sapolio"
    print( "Lejía Sapolio")
4. mostrar un mensaje donde su detalle cual la lista de M.C y la lista de P.L formatiando.
buscar:int=M.C.indix("honda")
vihiculo[buscar] ("honda")