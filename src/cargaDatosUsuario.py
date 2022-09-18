#from random import random
from datetime import datetime
import random as random
import conexionPostgres
import clasesBD

def run():
    # Instancio las clases
    pg = conexionPostgres.conexionPostgres()
    cuenta = clasesBD.cuenta()
    detacuenta = clasesBD.detacuenta()

    # Se obtiene el valor del ultimo idcuenta insertado que se almaceno en la BD
    rowSelect = pg.select(cuenta.selectMaxPk())
    for r in rowSelect:
        cuenta.setIdCuenta(r[0])

    if cuenta.getIdCuenta() == -1:
        print("Error seteando el idcuenta maximo")
        return
    
    # Seteamos el valor de idcuenta con el que vamos a realizar el auto incremental
    idCuenta = cuenta.getIdCuenta()

    #Ciclo para procesar los 50 mil registros
    for i in range(50000000):
        if i % 2 == 0 and i < 10:
            print("Iteracion: "+str(i+1)+" - Fecha Hora: "+datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

        if i % 10 == 0 and i < 100:
            print("Iteracion: "+str(i+1)+" - Fecha Hora: "+datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

        if i % 100 == 0 and i < 100000:
            print("Iteracion: "+str(i+1)+" - Fecha Hora: "+datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

        if i % 100000 == 0 and i < 1000000:
            print("Iteracion: "+str(i+1)+" - Fecha Hora: "+datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

        if i % 1000000 == 0 and i < 10000000:
            print("Iteracion: "+str(i+1)+" - Fecha Hora: "+datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

        if i % 10000000 == 0:
            print("Iteracion: "+str(i+1)+" - Fecha Hora: "+datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        #Seteamos los datos aleatorios de la cuenta
        idCuenta += 1
        cuenta.setIdCuenta(idCuenta)
        cuenta.datosAleatorio()

        #insertamos el registro aleatorio
        rowInsert = pg.insert(cuenta.insertSql())
        if rowInsert == 0:
            print("Error insertando el registro. "+ cuenta.insertSql())
            return
        
        # insertamos los registros en los detalles de cuenta de modo aleatorio
        # pueden ser de 1 a 20 registros por cuenta
        cantidadCargos = random.randint(1,20)
        for i in range(cantidadCargos):
            # Seteo los datos aleatorios y le paso la referencia del idCuenta
            detacuenta.datosAleatorio(idCuenta,cuenta.getFechaCreacion())
            rowInsert = pg.insert(detacuenta.insertSql())

            if rowInsert == 0:
                print("Error insertando el registro. "+ detacuenta.insertSql())
                return

if __name__ == "__main__":
    run()


