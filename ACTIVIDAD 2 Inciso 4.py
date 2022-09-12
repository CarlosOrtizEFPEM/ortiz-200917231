import time
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.2  ")
print ("I N C I S O  4  ")

print ("\n1-: Almacenar 12 Elementos")
#{} []

diccionario_productos={}

for inicio in range(1,3):
    productos={
        "codigo":inicio,
        "nombre":input("Ingrese un nombre: "),
        "precio":str(input("Ingrese un precio:"))
        }
    diccionario_productos.update({inicio:productos})
print ("\nLos datos almacenados son: ")
for nombre, precio in diccionario_productos.items(): 
    print ("ID %s es %s" % (nombre, precio))
    
   
print ("\nEl aumento de precio al precio es: ")
diccionario_productos.update({"Aumento":10})
print(diccionario_productos)

print ("\nModificar dato: ")
diccionario_productos.update({"nombre":"CARLOS"})
print (diccionario_productos)
diccionario_productos["nombre"]="Ortiz"
print (diccionario_productos)







#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()
