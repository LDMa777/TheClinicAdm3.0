class Analisis:
    def __init__(self, id_analisis, fecha_analisis, clinico_analisis, obser_analisis, resultados_analisis):
        self._id_analisis = id_analisis
        self._fecha_analisis = fecha_analisis
        self._clinico_analisis = clinico_analisis
        self._obser_analisis = obser_analisis
        self._resultados_analisis = resultados_analisis

    def __str__(self):
        return f'[ID: {self._id_analisis},Fecha:{self._fecha_analisis},Nro.Clinico:{self._clinico_analisis}, ' \
               f'Observaciones:{self._obser_analisis},Resultados:{self._resultados_analisis}]'

    @property
    def id_analisis(self):
        return self._id_analisis

    @id_analisis.setter
    def id_analisis(self, id_analisis):
        self._id_analisis = id_analisis

    @property
    def fecha_analisis(self):
        return self._fecha_analisis

    @fecha_analisis.setter
    def fecha_analisis(self, fecha_analisis):
        self._fecha_analisis = fecha_analisis

    @property
    def clinico_analisis(self):
        return self._clinico_analisis

    @clinico_analisis.setter
    def clinico_analisis(self, clinico_analisis):
        self._clinico_analisis = clinico_analisis

    @property
    def obser_analisis(self):
        return self._obser_analisis

    @obser_analisis.setter
    def obser_analisis(self, obser_analisis):
        self._obser_analisis = obser_analisis

    @property
    def resultados_analisis(self):
        return self._resultados_analisis

    @resultados_analisis.setter
    def resultados_analisis(self, resultados_analisis):
        self._resultados_analisis = resultados_analisis