class Recibos:
    def __init__(self, id_recibo, fecha_recibo, descripcion_recibo, clinico_recibo, liqui_recibo):
        self._id_recibo = id_recibo
        self._fecha_recibo = fecha_recibo
        self._descripcion_recibo = descripcion_recibo
        self._clinico_recibo = clinico_recibo
        self._liqui_recibo = liqui_recibo

    def __str__(self):
        return f'[ID:{self._id_recibo},Fecha:{self._fecha_recibo},Descripcion:{self._descripcion_recibo},' \
               f'Clinico:{self._clinico_recibo},Liquidacion:{self._liqui_recibo}]'

    @property
    def id_recibo(self):
        return self._id_recibo

    @id_recibo.setter
    def id_recibo(self, id_recibo):
        self._id_recibo = id_recibo

    @property
    def fecha_recibo(self):
        return self.fecha_recibo

    @fecha_recibo.setter
    def fecha_recibo(self, fecha_recibo):
        self._fecha_recibo = fecha_recibo

    @property
    def descripcion_recibo(self):
        return self._descripcion_recibo

    @descripcion_recibo.setter
    def descripcion_recibo(self, descripcion_recibo):
        self._descripcion_recibo = descripcion_recibo

    @property
    def clinico_recibo(self):
        return self._clinico_recibo

    @clinico_recibo.setter
    def clinico_recibo(self, clinico_recibo):
        self._clinico_recibo = clinico_recibo

    @property
    def liqui_recibo(self):
        return self._liqui_recibo

    @liqui_recibo.setter
    def liqui_recibo(self, liqui_recibo):
        self._liqui_recibo = liqui_recibo


if __name__ == '__name__':
    print(__name__)

