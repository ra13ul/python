# FUNCIONES EN PYTHON
def unaFuncion():
    print('dentro de la funcion')

unaFuncion()

a=5
b=3

def sumar(a,b):
    return a+b

print("Suma de las variables a y b")
print(sumar(a,b))

print("Suma de las variables a y b y suma 100 a lo que devuelve")
print(sumar(a,b)+100)
print('\n')

print("Suma de las variables a y b pasando valores\
      nuevos de a y b como argumentos")
print(sumar(3,25))

print('\n')
print('Guardamos el resultado en una variable')
def resta(c, d):
    return c - d

resultado=resta(5,3)
print(resultado)

c = resultado
d= 10

print(resta(c, d))

def guion():
    return ' - - - - - - S E P A R A D O R - - - - - - -'

#el factorial de x es igual a x * (x-1) * (x-2) * … * 1
def factorial(x): 
    if x > 1: 
        return x*factorial(x-1)
    else:
        return 1
x=3
print(factorial(x))
print(guion())

#contador
def contador(cont):
    while cont <= 10:
        if(cont%2==0):
            print(cont, 'es par')
        else:
            print(cont, 'es impar')
        cont=cont+1

contador(1)

print(guion())

#AMBITO DE FUNCIONES
a = 'FUERA de la funcion'


def funcion1():
    a='DENTRO de la funcion'
    return a

print(a)
print(funcion1())


print(guion())
#pruebas de parametros
def funcion2(*args):
    a='LOG'
    print(b, a, args)
    
b='los LOGS:'
funcion2('EMPIEZA',1,3,8,65,21,'ACABA')

print(guion())
print(type(funcion1))
print(type(b))

print(guion())
texto=''' Este es UN TEXTO en Varias \
    lineas para USAR algunas variables'''
print(texto)
print(texto.upper())
print(texto.lower())

print(guion())
print(texto.capitalize())
print(texto.count('s'), 'veces aparece en el texto la "s"')
print(texto.find('y'))

print(guion())
print(texto.split())
print(texto.split('para'))
print(texto.replace('a', 'AAA'))

print(guion())
nombre=input("Escribe tu nombre ")
print("Hola", nombre)

a = 65
print(id(a))