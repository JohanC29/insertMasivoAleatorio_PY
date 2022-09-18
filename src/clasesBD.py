
from datetime import datetime, timezone
from datosAleatorios import datoAleatorio
    

# INSERT INTO public.cuenta
# (identificacion, nombre, fechacreacion, estadocuenta, tipocuenta)
# VALUES(0, '', '', 0, 0);
class cuenta(datoAleatorio):
    def __init__(self):
        self.limpiar()

        # Invoca al constructor de clase datoAleatorio
        datoAleatorio.__init__(self)

    def limpiar(self):
        self.idcuenta = -1
        self.identificacion = 0
        self.nombre = ""
        self.fechacreacion = datetime.now(timezone.utc)
        self.estadocuenta = 0
        self.tipocuenta = 0
    
    def insertSql(self):

        query = f""" INSERT INTO public.cuenta (idcuenta, identificacion, nombre, fechacreacion, estadocuenta, tipocuenta) 
                    VALUES({self.idcuenta},{self.identificacion}, '{self.nombre}', '{self.fechacreacion}', {self.estadocuenta}, {self.tipocuenta});"""

        return query

    def datosAleatorio(self):
        self.identificacion = super().getIdentificacion()
        self.nombre = super().getNombre()
        self.fechacreacion = super().getFechaCreacion()
        self.estadocuenta = super().getEstadoCuenta()
        self.tipocuenta = super().getTipoCuenta()

    def getIdCuenta(self):
        return self.idcuenta
    
    def setIdCuenta(self,inuIdCuenta):
        self.idcuenta = inuIdCuenta
    
    def selectMaxPk(self):
        return """select COALESCE(max(c.idcuenta),0)  from cuenta c ;"""
    
    def getFechaCreacion(self):
        return self.fechacreacion


# INSERT INTO public.detacuenta
# (idcuenta, fechacreacion, valor, tipomovimiento, ipcreacion)
# VALUES(0, '', 0, 0, '');
class detacuenta(datoAleatorio):
    def __init__(self):
        self.limpiar()

    def limpiar(self):
        self.idcuenta = 0
        self.fechacreacion = datetime.now(timezone.utc)
        self.valor = 0
        self.tipomovimiento = 0
        self.ipcreacion = "0.0.0.0"
        self.idconcepto = 0
    
    def insertSql(self):

        query = f""" INSERT INTO public.detacuenta
                    (idcuenta, fechacreacion, valor, tipomovimiento, ipcreacion, idconcepto)
                    VALUES({self.idcuenta}, '{self.fechacreacion}', {self.valor}, {self.tipomovimiento}, '{self.ipcreacion}',
                    {self.idconcepto});"""

        return query

    def datosAleatorio(self, inuIdCuenta, ideFechaCreaCuenta):
        self.idcuenta = inuIdCuenta
        self.fechacreacion = super().getFechaCreacion(ideFechaCreaCuenta) 
        self.valor = super().getValor()
        self.tipomovimiento = super().getTipoMovimiento()
        self.ipcreacion = super().getIpCreacion()
        self.idconcepto = super().getIdConcepto()
