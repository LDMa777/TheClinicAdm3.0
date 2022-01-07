class Horarios:
    def __init__(self, id_horario, tiempo_horario):
        self._id_horario = id_horario
        self._tiempo_horario = tiempo_horario

    def __str__(self):
        return f'[ID:{self._id_horario},Horario:{self._tiempo_horario}]'

    @property
    def id_horario(self):
        return self._id_horario

    @id_horario.setter
    def id_horario(self, id_horario):
        self._id_horario = id_horario

    @property
    def tiempo_horario(self):
        return self._tiempo_horario

    @tiempo_horario.setter
    def tiempo_horario(self, tiempo_horario):
        self._tiempo_horario = tiempo_horario