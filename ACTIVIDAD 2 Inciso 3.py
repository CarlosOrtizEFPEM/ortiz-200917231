import time
print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.2  ")
print ("I N C I S O  3  ")

lista_numerica=[]
def pedir_numeros():
    print ("\n1-: Solicitar 10 numeros")
    for inicio in range(5):
        #valores=float(input(str("Ingrese numeros:")))
        valores=input(str("Ingrese numeros:"))
        lista_numerica.append(valores)
    print("Los numeros ingresados son:", lista_numerica)

def comprobar_valores():
    print ("\n2-: Mostrar el # Mayor y Menor")
    menor=None
    mayor=None
    for numero in lista_numerica:
        if menor==None and mayor==None:
            menor=numero
            mayor=numero
        else:
            if numero<menor:
                menor=numero
            if numero>mayor:
                mayor=numero
    print("El numero mayor es:", mayor)
    print("El numero menor es:", menor)

def orden_valores():
    print ("\n3-: Ordenarlos en forma desendente")
    lista_numerica.sort(reverse=True)
    print ("Orden desendente es:", lista_numerica)

def sumar_valores():
    cambiar_lista=[int(string) for string in lista_numerica]
    sumar=sum(cambiar_lista)
    print ("\n4-:La suma de los valores es:", sumar)
    
    numero_comparar=sumar
    inicio=1
    comparar=0
    while inicio<=numero_comparar:
        if numero_comparar % inicio ==0:
            comparar=comparar+1
        inicio=inicio+1
    if comparar==2:
        print ("\n5-:El Resultado",sumar, "SI es primo")
    else:
        print ("\n5-:El Resultado",sumar, "No es primo")   
       


#Llamar a funciones
pedir_numeros()
comprobar_valores()
orden_valores()
sumar_valores()


    

#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()





