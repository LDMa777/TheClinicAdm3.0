from Usuarios import Usuarios


class Especialidades:
    def __init__(self, id_especialidad, nombre_especialidad):
        self._id_especialidad = id_especialidad
        self._nombre_especialidad = nombre_especialidad

    @property
    def id_especialidad(self):
        return self._id_especialidad

    @id_especialidad.setter
    def id_especialidad(self, id_especialidad):
        if Usuarios._validar_inte(self, id_especialidad):
            self._id_especialidad = id_especialidad
        else:
            print("Error Ingreso Nro.Turno, No Tiene Que Ser Un Numero!!! :D")

    @property
    def nombre_especialidad(self):
        return self._nombre_especialidad

    @nombre_especialidad.setter
    def nombre_especialidad(self, nombre_especialidad):
        if Usuarios._validar_char(self, nombre_especialidad):
            self._nombre_especialidad = nombre_especialidad
        else:
            print("Error Ingreso Nombre, No Tiene Que Ser Un Caracter!!! :D")

    def __str__(self):
        return f'[ID:{self._id_especialidad},Nombre:{self._nombre_especialidad}]'


if __name__ == '__name__':
    print(__name__)
