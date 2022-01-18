class Turnos:
    def __init__(self, id_turno, fecha_turno, clinico_turno, paciente_turno, comentarios_turno, horario_turno):
        self._id_turno = id_turno
        self._fecha_turno = fecha_turno
        self._clinico_turno = clinico_turno
        self._paciente_turno = paciente_turno
        self._comentarios_turno = comentarios_turno
        self._horario_turno = horario_turno

    def __str__(self):
        return f'[ID:{self._id_turno},Fecha:{self._fecha_turno},Clinico:{self._clinico_turno},' \
               f'Paciente:{self._paciente_turno},Comentarios:{self._comentarios_turno},Horario:{self._horario_turno}]'

    @property
    def id_turno(self):
        return self._id_turno

    @id_turno.setter
    def id_turno(self, id_turno):
        self._id_turno = id_turno

    @property
    def fecha_turno(self):
        return self._fecha_turno

    @fecha_turno.setter
    def fecha_turno(self, fecha_turno):
        self._fecha_turno = fecha_turno

    @property
    def clinico_turno(self):
        return self._clinico_turno

    @clinico_turno.setter
    def clinico_turno(self, clinico_turno):
        self._clinico_turno = clinico_turno

    @property
    def paciente_turno(self):
        return self._paciente_turno

    @paciente_turno.setter
    def paciente_turno(self, paciente_turno):
        self._paciente_turno = paciente_turno

    @property
    def comentarios_turno(self):
        return self._comentarios_turno

    @comentarios_turno.setter
    def comentarios_turno(self, comentarios_turno):
        self._comentarios_turno = comentarios_turno

    @property
    def horario_turno(self):
        return self._horario_turno

    @horario_turno.setter
    def horario_turno(self, horario_turno):
        self._horario_turno = horario_turno


if __name__ == '__name__':
    print(__name__)
