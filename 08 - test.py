from funcionesGlobales import guion
print(guion())
print('Ejercicio 1 \n ' \
      'Dados dos números, escriba un código Python para \
      \n encontrar el mínimo de estos dos números')
def minimo(a, b):
    return min(a,b)

print(minimo(2,4))
print(minimo(-1,-4))

print(guion())

#Ejercicio 2
print(' EJERCICIO 2 \n Invertir palabras de una cadena dada.')
print('Cadena: codigo de practica de prueba geeks')

stringOriginal = "codigo de practica de prueba geeks"

def inversor(stringOriginal):
    splitFrase = stringOriginal.split(' ')
    
    reverseFrase = ' '.join(reversed(splitFrase))

    return reverseFrase

print(inversor(stringOriginal))

print(guion())

# Ejercicio 3
print('3. Realizar una suma de los elementos de una tupla')

laTupla = (7, 8, 9, 1, 10, 7)

#Convertimos la tupla a lista para poder operar con ella
resultado = sum(list(laTupla))
print(resultado)


print(guion())
#4. Escriba un código que calcule una lista de números proporcionados.
laLista = [3,5,8,9,9]
def sumaLista(laLista):
    if len(laLista) == 1:
        return laLista[0]
    else:
        return laLista[0] + sumaLista(laLista[1:])

print(sumaLista(laLista))

print(guion())
print('5. Escriba un código que desordene al azar una lista.')
from random import shuffle
laLista2 = [3,5,8,9,9]
print(laLista2)
shuffle(laLista2)
print(laLista2)

print(guion())
print('6. Escriba un código que pueda contar todas las palabras mayúsculas de un archivo.')

archivo = 'short.zen.txt'

with open(archivo) as fh:
    contador=0
    texto = fh.read()

for i in texto:
    if i.isupper():
        contador += 1
print(contador)

print(guion())
print('7. ¿Si la lista 1 es [4, 6, 8, 1, 0, 3], que sería la lista 1 [-1]?')

#Solución:"-1" siempre se refiere al último índice de la lista, por lo tanto, la respuesta seria 3.

print(guion())

#8. Escriba un programa para producir la serie Fibonacci en Python.
print('8. Escriba un programa para producir la serie Fibonacci en Python.')

n = 5

primero = 0
segundo = 1
suma = 0
count= 1

while(count <= n):
    print(suma)
    count+=1
    primero = segundo
    segundo = suma
    suma = primero + segundo

print(guion())

print('9. Escriba un programa en Python para comprobar si un número es primo.')

def numPrimo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True


print(numPrimo(6))

print(guion())
print('10. Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.')

a = str(515)
b = a[::-1]
if a==b:
    print('es capicula')
else:
    print('No es capicua')

print(guion())
print('11. Escribir un algoritmo de ordenación para un conjunto de datos numéricos en Python.')

laLista3 = ['10', '3', '7', '25', '1']
laLista3=[int(i) for i in laLista3]

laLista3.sort()
print(laLista3)

print(guion())

"""
12. ¿Cuál de las siguientes declaraciones es inválida?
a) abc = 1.000.000

b) a b b c = 1000 2000 3000

c) a,b,c = 1,000,000

d) a_b_c = 1,000,000

Solución: b) a b b c = 1000 2000 3000
"""

