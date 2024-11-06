from funcionesGlobales import guion

#Devuelve la 'P' de Python
def indexador(objeto, indice): 
    return objeto[indice] 
print(indexador('Python', 0)) 

print(guion())

# indice largo, da error
def indexador(objeto, indice): 
    return objeto[indice] 
#print(indexador('Python', 10)) #descomentar para ver el error

print(guion())

try:
    indexador('Python', 3)
except IndexError:
    print("El indice es muy alto")

print(guion())

print('El programa continua')

print(guion())

# errores lanzados manualmente con raise
#raise IndexError('Error lanzado con "raise"')

print(guion())

# Con assert lanzamos un error si se cumple una condicion

a = 15
b = 7

assert(a > b), '"a" tiene que ser mayor que "b"'
print('Sigue el programa')


# finally permite que ejecute algun codigo incluso cuando falla try
print(guion())
try:
    indexador('Python', 10) 
finally:
    print('---------\n Esto se ejecuta incluso cuando \
salta la excepcion \n ------------------------------')