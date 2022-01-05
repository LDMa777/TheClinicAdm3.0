class Pacientes:
    def __init__(self, id_paciente, turno_paciente, clinico_paciente):
        self._id_paciente = id_paciente
        self._turno_paciente = turno_paciente
        self._clinico_paciente = clinico_paciente

    def __str__(self):
        return f'[ID:{self._id_paciente},Turno Paciente: {self._turno_paciente},Clinico:{self._clinico_paciente}] '

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, id_paciente):
        self._id_paciente = id_paciente

    @property
    def turno_paciente(self):
        return self._turno_paciente

    @id_paciente.setter
    def turno_paciente(self, turno_paciente):
        self._turno_paciente = turno_paciente

    @property
    def clinico_paciente(self):
        return self._clinico_paciente

    @id_paciente.setter
    def clinico_paciente(self, clinico_paciente):
        self._clinico_paciente = clinico_paciente