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