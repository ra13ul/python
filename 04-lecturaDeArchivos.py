print(' - - - - - - - - - - ')
texto = '''\
Bello es mejor que feo. 
Explicito es mejor que implicito. 
Simple es mejor que complejo. 
Complejo es mejor que complicado. 
'''
print(texto)
print(' - - - - - - - - - - ')

#Creo el fichero con permiso de escritura
f = open('short.zen.txt', 'w')

#Escribe en el fichero
f.writelines(texto)

#Se cierra fichero
f.close()

f = open('short.zen.txt', 'r')
linea=f.readline()
print(linea)

lineaSiguiente=f.__next__()
print('lineaSiguiente',lineaSiguiente)
print(next(f))

print(' - - - - - - - - - - ')
#Leer un archivo de texto completo
for linea in open('short.zen.txt'):
    print(linea)