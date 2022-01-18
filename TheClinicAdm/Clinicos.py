class Clinicos:
    def __init__(self, id_clinico, analisis_clinico, recibos_clinico, turnos_clinico, esp_clinico):
        self._id_clinico = id_clinico
        self._analisis_clinico = analisis_clinico
        self._recibos_clinico = recibos_clinico
        self._turnos_clinico = turnos_clinico
        self._esp_clinico = esp_clinico

    def __str__(self):
        return f'[ID:{self._id_clinico},Nro.Analsis Clinico:{self._analisis_clinico},' \
               f'Nro.Recibo Sueldo{self._recibos_clinico},Nro.Turnos:{self._turnos_clinico},' \
               f'Nro.Especialidad:{self._esp_clinico}]'

    @property
    def id_clinico(self):
        return self._id_clinico

    @id_clinico.setter
    def id_clinico(self, id_clinico):
        self._id_clinico = id_clinico

    @property
    def analisis_clinico(self):
        return self._analisis_clinico

    @analisis_clinico.setter
    def analisis_clinico(self, analisis_clinico):
        self._analisis_clinico = analisis_clinico

    @property
    def recibos_clinico(self):
        return self._recibos_clinico

    @recibos_clinico.setter
    def recibos_clinico(self, recibos_clinico):
        self._recibos_clinico = recibos_clinico

    @property
    def turnos_clinico(self):
        return self._turnos_clinico

    @turnos_clinico.setter
    def turnos_clinico(self, turnos_clinico):
        self._turnos_clinico = turnos_clinico

    @property
    def esp_clinico(self):
        return self._esp_clinico

    @esp_clinico.setter
    def esp_clinico(self, esp_clinico):
        self._esp_clinico = esp_clinico


if __name__ == '__name__':
    print(__name__)
