from Usuarios import Usuarios


class Historiales:
    def __init__(self, id_historial, turno_historial, clinico_historial, paciente_historial, fecha_historial,
                 observacion_historial, diagnostico_historial):

        self._id_historial = id_historial
        self._turno_historial = turno_historial
        self._clinico_historial = clinico_historial
        self._paciente_historial = paciente_historial
        self._fecha_historial = fecha_historial
        self._observacion_historial = observacion_historial
        self._diagnostico_historial = diagnostico_historial

    @property
    def id_historial(self):
        return self._id_historial

    @id_historial.setter
    def id_historial(self, id_historial):
        if Usuarios._validar_inte(self, id_historial):
            self._id_historial = id_historial
        else:
            print("Error Ingreso ID, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def turno_historial(self):
        return self._turno_historial

    @turno_historial.setter
    def turno_historial(self, turno_historial):
        if Usuarios._validar_inte(self, turno_historial):
            self._turno_historial = turno_historial
        else:
            print("Error Ingreso Nro.Turno, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def clinico_historial(self):
        return self._clinico_historial

    @clinico_historial.setter
    def clinico_historial(self, clinico_historial):
        self._clinico_historial = clinico_historial

    @property
    def paciente_historial(self):
        return self._paciente_historial

    @paciente_historial.setter
    def paciente_historial(self, paciente_historial):
        self._paciente_historial = paciente_historial

    @property
    def fecha_historial(self):
        return self._fecha_historial

    @fecha_historial.setter
    def fecha_historial(self, fecha_historial):
        self._fecha_historial = fecha_historial

    @property
    def observacion_historial(self):
        return self._observacion_historial

    @observacion_historial.setter
    def observacion_historial(self, observacion_historial):
        self._observacion_historial = observacion_historial

    @property
    def diagnostico_historial(self):
        return self._diagnostico_historial

    @diagnostico_historial.setter
    def diagnostico_historial(self, diagnostico_historial):
        self._diagnostico_historial = diagnostico_historial

    def __str__(self):
        return f'[ID:{self._id_historial},Turno:{self._turno_historial},Clinico:{self._clinico_historial},' \
               f'Paciente:{self._paciente_historial},Fecha:{self._fecha_historial}],' \
               f'Observaciones:{self._observacion_historial},Diagnostico:{self._diagnostico_historial}'


if __name__ == '__name__':
    print(__name__)
