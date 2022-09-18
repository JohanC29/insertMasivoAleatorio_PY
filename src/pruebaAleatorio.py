import datosAleatorios

def run():

    datosRandom = datosAleatorios.datoAleatorio()

    print(datosRandom.getIdentificacion())
    print(datosRandom.getNombre()+"")
    print(datosRandom.getEstadoCuenta())
    print(datosRandom.getIpCreacion())
    print(datosRandom.getTipoMovimiento())
    print(datosRandom.getTipoCuenta())
    print(datosRandom.getFechaCreacion())

if __name__ == "__main__":
    run()