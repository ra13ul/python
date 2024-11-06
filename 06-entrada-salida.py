from funcionesGlobales import guion

print(guion())
'''
nombre=input('Tu nombre: ')
edad=int(input("tu edad: "))
print(nombre, edad)

#varios numeros de una vez, se usa map
a, b, c, = map(int, input('Tres numeros: ').split())
print(a, b, c)
'''
guion()
#FORMATO DE CADENAS
name = 'john'

print(f'hola {name}')

a = 5
b = 6
c = a + b
print('La suma de {} mas {} es {}'.format(a,b, c))
print()
print('{2} es la suma de {0} + {1}'.format(a, b, c))
print()
print('{valor1} sumado a {valor2} es igual a {valor3}'.format(valor1=a, valor2=b, valor3=c))

#EL OPERADOR %
# %d -> entero
# %f -> flotante
# %s -> cadena
# hay mas valores %x -> hexadecimal, %o -> octal ...
num=(int(input("tu numero: ")))
suma = num*2
print('El doble es: %d' %suma)
