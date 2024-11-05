a=1
b=3
if a < b:
    print('mayor')

a = 0
b = 25
while a < b:
    print(a, 'menor que ', b)
    a = a+1

print(' - - - -  - - - - - ')

a=5
while a:
    print(a, end=' - ')
    if a==2:
        break
    a-=1
print('\nFuera del bucle')
print('valor de "a": {}'.format(a))

print(' - - - -  - - - - - ')
# BUCLE FOR
for s in ['Uno', 'Dos', 'Tres']:
    print(s, end=' ')

print(' - - - - - - - - - - ')
x = 0
for y in [1, 2, 3, 4, 5]:
    print(y)
    x += y

print(x)

print(' - - - - - - - - - - ')

for c in 'Ahora mismo acabo':
    print(c, end=' - ')

print(' - - - - - - - - - - ')
keys = ['nombre', 'apellidos', 'edad']
values = ['Guido', 'van Rossum', '60']
diccionario=dict(zip(keys, values))
for k in diccionario:
    junto= '{}: {}'.format(k, diccionario[k])
    print(junto)

print(' - - - - - - - - - - ')
lista5=[2, 5, 8, 50]
lista6=[1, 15, 6, 54]
dict02=dict(zip(lista5, lista6))
for m in dict02:
    print(m, dict02[m])

for x,y in zip(lista5, lista6):
    maximo = max(x, y)
    print('valor mas alto: {}'.format(maximo))

keys1=['pais', 'ciudad']
values1=['espania', 'madrid']
diccionario3 = dict(zip(keys1, values1))
for l, m in diccionario3.items():
    print('{}: {}'.format(l, m))

print(diccionario3.keys())
print(diccionario3.values())
print(diccionario3.items())