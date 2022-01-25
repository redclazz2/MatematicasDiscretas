import math
listaResultado = [n for n in range(2,51) if all(n % u != 0 for u in range(2,math.isqrt(n)+1))]
print("Se encontraron",len(listaResultado),"números primos:",", ".join(map(str,listaResultado)))
#Recursos Utilizados: https://www.programiz.com/python-programming/list-comprehension
#https://stackoverflow.com/questions/18551458/how-to-frame-two-for-loops-in-list-comprehension-python