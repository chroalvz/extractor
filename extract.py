from datetime import datetime
import time, os

def extractor():
    with open('material/tablas.csv','r') as file:
        linea = file.readline()
        linea_split = linea.split(';')
        for i in range(len(linea_split)):
            print(f'{i}\t{linea_split[i]}')

def listados_filtrado():
    c_linea = 0
    with open('material/tablas.csv','r') as file:
        linea = file.readlines()
        # linea_f = linea.split(';')
        # for linea in lineas:
        #     print(linea[0])
        for linea_f in range(len(linea)):
            linea_split = linea[linea_f].split(';')
            if linea_split[19] == 'Y':
                print(f'{linea_split[0]}\t{linea_split[21]}\t{linea_split[8]}\t{linea_split[19]}')
                c_linea += 1
        print(f'cantidad de registros {c_linea}')


# extractor()
listados_filtrado()