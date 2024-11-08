from funcionesGlobales import sep
print(sep)

#crear diccionario

dic={
    'nombre':'Andres',
    'apellido':'Fernandez',
    'edad':15,
    'peso':82.8
}

dic2 = dict(
    nombre='Andres',
    apellido='Fernandez',
    edad=15,
    peso=82.8
)
print(dic.keys())
print(dic.values())

dic2.update(direccion='alcala')
print(dic2)

print(dic2)