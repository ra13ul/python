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
    print(a, end=' ')
    if a==2:
        break
    a-=1
print('\nFuera del bucle')
print('valor de "a": {}'.format(a))

print(' - - - -  - - - - - ')