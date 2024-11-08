from funcionesGlobales import sep

print(sep)
num = int(input('Introduce un número: '))

def tablaMultiplicar(num):
    for i in range(1, 11):
        print(i, ' x ', num, ' = ', i*num)
            
tablaMultiplicar(num)