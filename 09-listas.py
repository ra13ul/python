from funcionesGlobales import sep

print(sep)

miLista=["Angel", 43, 667767250]  
miLista2 = [22, True, "una lista", [1, 2]] 
print(type(miLista))

print(miLista)

for i in miLista:
    print(i)

print(miLista[1])
print(miLista2[3][1])

miLista3 = [1, False, "cadena", "de", "texto"]
print(miLista3)

miLista3[1] = True 
print(miLista3)

print(len(miLista3))

print(sep)

i=0
while i < len(miLista3):
    print(miLista3[i])
    i+=1

print(miLista[-1])

print(sep)
miLista4 = ["Angel", "Maria", "Manolo", "Antonio", "Pepe"] 
miLista5 = ["Maria", 2, 5.56, True]
print(miLista4)
print(miLista5)
print(sep)

print('Uno las listas')
miLista6 = miLista4 + miLista5
print(miLista6)
print(miLista6[2:4])