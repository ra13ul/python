#LEER ARCHIVOS
pkl_file = open('2024-10-29_crypto.csv', 'rb')
diccionario = pickle.load(pkl_file)
pkl_file.close()

#escribir diccionario
diccionario2 = {'a':1, 'b':2, 'c':3}
salida = open('diccionario.pkl', 'wb')
pickle.dump(diccionario2, salida)
salida.close()