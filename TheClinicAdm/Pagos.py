from Usuarios import Usuarios


class Pagos:
    def __init__(self, id_pago, fecha_pago, descripcion_pago, cantidad_pago, liqui_pago, dni_pago):
        self._id_pago = id_pago
        self._fecha_pago = fecha_pago
        self._descripcion_pago = descripcion_pago
        self._cantidad_pago = cantidad_pago
        self._liqui_pago = liqui_pago
        self._dni_pago = dni_pago

    def __str__(self):
        return f'[ID:{self._id_pago},Fecha:{self._fecha_pago},Descripcion:{self._descripcion_pago},' \
               f'Cantidad:{self._cantidad_pago},Liquidacion:{self._liqui_pago},DNI:{self._dni_pago}]'

    @property
    def id_pago(self):
        return self._id_pago

    @id_pago.setter
    def id_pago(self, id_pago):
        if Usuarios._validar_inte(self, id_pago):
            self._id_pago = id_pago
        else:
            print("Error Ingreso ID, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def fecha_pago(self):
        return self._fecha_pago

    @fecha_pago.setter
    def fecha_pago(self, fecha_pago):
        self._fecha_pago = fecha_pago

    @property
    def descripcion_pago(self):
        return self._descripcion_pago

    @descripcion_pago.setter
    def descripcion_pago(self, descripcion_pago):
        self._descripcion_pago = descripcion_pago

    @property
    def cantidad_pago(self):
        return self._cantidad_pago

    @cantidad_pago.setter
    def cantidad_pago(self, cantidad_pago):
        if Usuarios._validar_inte(self, cantidad_pago):
            self._cantidad_pago = cantidad_pago
        else:
            print("Error Ingreso De Cantidad, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def liqui_pago(self):
        return self._liqui_pago

    @liqui_pago.setter
    def liqui_pago(self, liqui_pago):
        if Usuarios._validar_inte(self, liqui_pago):
            self._liqui_pago = liqui_pago
        else:
            print("Error Ingreso Liquidacion, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def dni_pago(self):
        return self._dni_pago

    @dni_pago.setter
    def dni_pago(self, dni_pago):
        self._dni_pago = dni_pago


if __name__ == '__name__':
    print(__name__)
