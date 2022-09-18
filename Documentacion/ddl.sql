-- Creacion de la tabla maestra
CREATE TABLE public.cuenta (
	idcuenta int8 NOT NULL GENERATED ALWAYS AS IDENTITY,
	identificacion int8 NOT NULL,
	nombre varchar NOT NULL,
	fechacreacion timestamp with time zone NOT NULL,
	estadocuenta int NOT NULL,
	tipocuenta int NULL,
	CONSTRAINT cuenta_pk PRIMARY KEY (idcuenta)
);
COMMENT ON TABLE public.cuenta IS 'tabla maestro de las cuentas';

-- Column comments

COMMENT ON COLUMN public.cuenta.idcuenta IS 'identificador unico de la cuenta';
COMMENT ON COLUMN public.cuenta.identificacion IS 'identificacion del propietario de la cuenta';
COMMENT ON COLUMN public.cuenta.nombre IS 'nombre del propietario de la cuenta';
COMMENT ON COLUMN public.cuenta.fechacreacion IS 'fecha en que se creo la cuenta';
COMMENT ON COLUMN public.cuenta.estadocuenta IS 'estado de la cuenta. 1.Activa 2.Inactiva';
COMMENT ON COLUMN public.cuenta.tipocuenta IS 'tipo de cuenta';


-- Creacion de la tabla detalle de cuenta
CREATE TABLE public.detacuenta (
	iddetacuenta int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	idcuenta int4 NOT NULL,
	fechacreacion timestamp with time zone NOT NULL,
	valor int8 NOT NULL,
	tipomovimiento int NOT NULL,
	ipcreacion varchar NOT NULL,
	idconcepto int not null,
	CONSTRAINT detacuenta_pk PRIMARY KEY (iddetacuenta),
	CONSTRAINT detacuenta_fk FOREIGN KEY (idcuenta) REFERENCES public.cuenta(idcuenta)
);
COMMENT ON TABLE public.detacuenta IS 'detalles de cuenta';

-- Column comments

COMMENT ON COLUMN public.detacuenta.iddetacuenta IS 'identificador unico de la tabla detalle de cuenta';
COMMENT ON COLUMN public.detacuenta.idcuenta IS 'identificador de la tabla maestro';
COMMENT ON COLUMN public.detacuenta.fechacreacion IS 'fecha de creacion del movimiento';
COMMENT ON COLUMN public.detacuenta.valor IS 'valor del movimiento';
COMMENT ON COLUMN public.detacuenta.tipomovimiento IS 'tipo de movimiento realizado';
COMMENT ON COLUMN public.detacuenta.ipcreacion IS 'ip de la maquina que realizo el movimiento';
COMMENT ON COLUMN public.detacuenta.idconcepto IS 'id del concepto del cargo generado de la cuenta';

