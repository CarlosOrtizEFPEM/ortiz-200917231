import time

print ("---------------------")
print (" Carlos Ortiz Serrano")
print (" Carnet 200917231")
print (" Lic. en Informatica")
print (" ---------------------" )
print ("ACTIVIDAD No.2  ")
print ("I N C I S O  1  ")
print ("Agregar en una TUPLA 8 Elementos\n")

tupla=("Ortiz","Carlos","USAC","Informatica",1988,34,2022,50)

print ("Los Elementos de la Tupla Original son:\n",tupla)

print ("\nA >> Los Elementos de la Tupla por linea:")
for inicio in range(len(tupla)):
   print (tupla[inicio])

print ("\nB >> Mostar texto que esten  en mayusculas")
for mayus in tupla:
    if (type(mayus) is str):        
        if (mayus.isupper()==True):
            print ("Texto en Mayuscilas son:", mayus)

print ("\nC >> Mostar texto que en Minisculas")
for mayus in tupla:
    if (type(mayus) is str):        
        if (mayus.isupper()==False):
            print ("Texto con Minusculas son:", mayus)

print ("\nD >> Mostar texto que terminen con letra s")
for elemento in tupla:   
   if (type(elemento) is str):
         #print (elemento[-1])
         if (elemento[-1]=="s"):
            print (elemento)  
                  
print ("\nE >> Contar Vocales")
def recore_tupla():
    global txt
    txt=("Ortiz""Carlos""USAC""Informatica")
def busca_vocales():
    busca_a=["a","A",]
    busca_e=["e","E",]
    busca_i=["i","I",]
    busca_o=["o","O",]
    busca_u=["u","U",]
    cont_a=0
    cont_e=0
    cont_i=0
    cont_o=0
    cont_u=0

    for i in busca_a:
        for j in txt:
            if(i==j):
                cont_a+=1
    for r in busca_e:
        for y in txt:
            if(r==y):
                cont_e+=1
    for h in busca_i:
        for ñ in txt:
            if(h==ñ):
                cont_i+=1
    for l in busca_o:
        for k in txt:
            if(l==k):
                cont_o+=1
    for s in busca_u:
        for n in txt:
            if(s==n):
                cont_u+=1
                
    cont=cont_a+cont_e+cont_i+cont_o+cont_u
    print("El numero total de vocales es: " ,cont)
    print("""El numero por vocal son: 
    Vocal a: {cont_a}
    Vocal e: {cont_e}
    Vocal i: {cont_i}    
    Vocal o: {cont_o}
    Vocal u: {cont_u}
    """)
recore_tupla()
busca_vocales()





     


     
   
   
                  
      #print (texto,"vocal",(vocal), {texto.count(vocal)})
    
#generar pausa en ejecucion
duracion = 2
time.sleep(duracion)
exit()



