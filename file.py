from dataclasses import dataclass
from datetime import datetime
from time import *

def fecha():
    horario = datetime.now()
    return horario

with open(f'files/archivos{fecha():%d%m%Y_%H%M%S}.txt','w+') as file:
    for i in range(1, 11):
        file.write(f'ingreso: {fecha():%d/%m/%Y %H:%M:%S.%f}')
        sleep(0.75)
        file.write(f'\tsalida: {fecha():%d/%m/%Y %H:%M:%S.%f}\n')
    file.close()


sleep(2)
print('fin de la ejecucion')