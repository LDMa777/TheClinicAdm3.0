class Especialidades:
    def __init__(self, id_especialidad, nombre_especialidad):
        self._id_especialidad = id_especialidad
        self._nombre_especialidad = nombre_especialidad

    def __str__(self):
        return f'[ID:{self._id_especialidad},Nombre:{self._nombre_especialidad}]'

    @property
    def id_especialidad(self):
        return self._id_especialidad

    @id_especialidad.setter
    def id_especialidad(self, id_especialidad):
        self._id_especialidad = id_especialidad

    @property
    def nombre_especialidad(self):
        return self._nombre_especialidad

    @nombre_especialidad.setter
    def nombre_especialidad(self, nombre_especialidad):
        self._nombre_especialidad = nombre_especialidad


if __name__ == '__name__':
    print(__name__)
