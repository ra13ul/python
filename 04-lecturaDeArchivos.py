import pickle
import csv
from pathlib import Path
#LEER ARCHIVOS
pkl_file = open('myfile.pkl', 'rb')
diccionario = pickle.load(pkl_file)
print(pkl_file)
pkl_file.close()


#escribir diccionario
diccionario2 = {'a':1, 'b':2, 'c':3}
salida = open('myfile.pkl', 'wb')
pickle.dump(diccionario, salida)
salida.close()
