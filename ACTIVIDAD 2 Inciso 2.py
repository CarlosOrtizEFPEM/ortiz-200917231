import time
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.2  ")
print ("I N C I S O  2  ")

lista=[]
print ("\n1-: Solicitar 15 Elementos")
for inicio in range(3):
    texto=input("Ingrese un texto:")
    lista.append(texto)
print("\n2-:Los elementos ingresados son:", lista)

print ("\n3-: Listar en forma Alfebiticamente")
lista.sort()
print("Orden alfabetico",lista)

print ("\n4-: Mostrar nombres con finalizen con VOCAL")
for ultimo in lista:   
    #print("muestra todoslos elementos",ultimo)
    #print("muestra ultima letra",ultimo[-1])
    if ultimo[-1]=="a" or ultimo[-1]=="e" or ultimo[-1]=="i" or ultimo[-1]=="o" or ultimo[-1]=="u":
        print(ultimo)
    

print ("\n5-: Mostrar longitud de los textos")
contador=0
promedio=0
for lista in lista:
    print ("No.de letras del texo:",lista,"es",len(lista))
    for lista in lista:
        contador+=1
print ("La suma de textos es:",contador)
promedio=contador/15
print ("El promedio es:",promedio)
 

#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()
