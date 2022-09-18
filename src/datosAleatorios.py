
import os    
import random as random
from datetime import datetime


class datoAleatorio:
    listIdentificacion = []
    listNombre = []
    def __init__(self):
        cwd = os.getcwd()  # Get the current working directory (cwd)
        ruta = cwd + "/src/csv/random_names_fossbytes.csv"
        # llenamos la lista con los nombres del archivo csv
        
        with open(ruta,encoding="utf-8") as archivo:
            for linea in archivo:
                self.listNombre.append(linea.strip())

    # El metodo siempre devuelve un numero de identificacion diferente
    def getIdentificacion(self):
        # LONGITUD MÍNIMA 4
        # LONGITUD MÁXIMA 12
        ramdomIdentificacion = random.randint(10000000,999999999999)

        # Se comenta por tiempo de ejecucion
        # while ramdomIdentificacion in self.listIdentificacion:
        #     ramdomIdentificacion = random.randint(10000000,999999999999)

        # self.listIdentificacion.append(ramdomIdentificacion)
        return ramdomIdentificacion

    # Devuelve un nombre de manera aleatoria
    def getNombre(self):
        nombre = random.choice(self.listNombre) 
        return str(nombre)

    # Devuelve el estado de la cuenta
    def getEstadoCuenta(self):
        # 1. Activa - 2.Inactica - 3.Congelada - 4.Bloqueada
        return random.randint(1,4)
    
    # Devuelve el tipo de cuenta
    def getTipoCuenta(self):
        # 1. Ahorro - 2. Corriente - 3.CDT 
        return random.randint(1,3)
    
    # Devuelve fecha aleatoria
    def getFechaCreacion(self, iFechaInicial=datetime(2000,1,1)):
        # Si valida esta en cero es porque puede ser cualquier fecha aleatoria
        fechaFinal = datetime.now() 
        random_date = iFechaInicial + ( fechaFinal- iFechaInicial) * random.random()
        
        return random_date
    
    # Devuelve el tipo de movimiento
    def getTipoMovimiento(self):
        # 1.  - 2. - 3. -4.
        return random.randint(1,4)
    
    # Devuelve una ip de manera aleatoria
    def getIpCreacion(self):
        ip = str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,255))+"."+str(random.randint(1,254))
        return ip
    
    # Devuelve un valor aleatorio
    def getValor(self):
        return random.randint(10000,999999999999)

    # Devuelve un concepto aleatorio
    def getIdConcepto(self):
        return random.randint(1,9999)



