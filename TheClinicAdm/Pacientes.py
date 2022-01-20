from Usuarios import Usuarios


class Pacientes:
    def __init__(self, id_paciente, turno_paciente):
        self._id_paciente = id_paciente
        self._turno_paciente = turno_paciente

    @property
    def id_paciente(self):
        return self._id_paciente

    @id_paciente.setter
    def id_paciente(self, id_paciente):
        if Usuarios._validar_inte(self, id_paciente):
            self._id_paciente = id_paciente
        else:
            print("Error Ingreso ID, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def turno_paciente(self):
        return self._turno_paciente

    @turno_paciente.setter
    def turno_paciente(self, turno_paciente):
        if Usuarios._validar_inte(self, turno_paciente):
            self._turno_paciente = turno_paciente
        else:
            print("Error Ingreso De Turno, No Tiene Que Ser Un Caracter!!! :D")

    def __str__(self):
        return f'[ID:{self._id_paciente},Turno Paciente: {self._turno_paciente}] '


if __name__ == '__name__':
    print(__name__)
