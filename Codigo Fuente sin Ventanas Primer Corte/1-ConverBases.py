from operator import neg
from os import remove

#Esta función permite convertir un número de base 10 a cualquier otra base
def funcionPartidaBaseDiezAOtraBase(numero,base):
    negativo = False
    cociente = 1
    if("-" in str(numero)):
        negativo = True
        tempListConvertir = list(str(numero))
        tempListConvertir.remove("-")
        numero = "".join(map(str,tempListConvertir))
    dividiendo = int(numero)
    storeResultado = []
    while(cociente != 0):
        resto = dividiendo % int(base)
        cociente = dividiendo // int(base)
        dividiendo = cociente
        storeResultado.append(resto)
    if(negativo):
        print("El resultado es: -", "".join(map(str,reversed(storeResultado))))
    else:
        print("El resultado es:", "".join(map(str,reversed(storeResultado))))

#Esta función permite convertir un número de cualquier base a 10
def partidaBaseDistintaDiezADiez(numero,base):
    negativo = False
    almacenTemp = 0
    arrayNumero = list(numero)
    if(arrayNumero[0]=="-"):
            negativo = True
            arrayNumero.remove("-")
    longitudBucle = len(arrayNumero)
    for n in range(0,longitudBucle):
        almacenTemp += int(arrayNumero[n]) * (pow(int(base),longitudBucle-(n+1)))
    if(negativo):
        return - almacenTemp
    else:
        return almacenTemp

#Menú de opciones --// Hecho por Sebastian Zárate 448669 //--
slc = input("Ingrese el número de la opción que quiere ejecutar (cualquier otro valor para finalizar): \n1) Base 2-9 a base 10 \n2) Base 10 a base 2-9 \n3) Base 1-9 a Base 1-9\n")
if(slc == "1"):
    i = partidaBaseDistintaDiezADiez(input("Ingrese el número a convertir: "), input("Ingrese la base en que está escrito: "))
    print("El resultado en base 10 es: ", i)
if(slc == "2"):
    funcionPartidaBaseDiezAOtraBase(input("Ingrese el número de base 10: "), input("Ingrese la base a la que se desea convertir: "))
if(slc == "3"):
    w = partidaBaseDistintaDiezADiez(input("Ingrese el número a convertir: "),input("Ingrese la base en que está escrito: "))
    funcionPartidaBaseDiezAOtraBase(w,input("Ingrese la base a la que se quiere convertir: "))