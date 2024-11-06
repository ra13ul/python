

#Devuelve la 'P' de Python
def indexador(objeto, indice): 
    return objeto[indice] 
print(indexador('Python', 0)) 



# indice largo, da error
def indexador(objeto, indice): 
    return objeto[indice] 
#print(indexador('Python', 10))

try:
    indexador('Python', 10)
except IndexError:
    print("El indice es muy alto")
