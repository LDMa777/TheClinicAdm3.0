from Usuarios import Usuarios


class Permisos:
    def __init__(self, id_permiso, nombre_permiso):
        self._id_permiso = id_permiso
        self._nombre_permiso = nombre_permiso

    def __str__(self):
        return f'[ID:{self._id_permiso},Nombre:{self._nombre_permiso}]'

    @property
    def id_permiso(self):
        return self._id_permiso

    @id_permiso.setter
    def id_permiso(self, id_permiso):
        if Usuarios._validar_inte(self, id_permiso):
            self._id_permiso = id_permiso
        else:
            print("Error Ingreso Nro.ID, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def nombre_permiso(self):
        return self._nombre_permiso

    @nombre_permiso.setter
    def nombre_permiso(self, nombre_permiso):
        if Usuarios._validar_char(self, nombre_permiso):
            self._nombre_permiso = nombre_permiso
        else:
            print("Error Ingreso Nombre, No Tiene Que Ser Un Numero!!! :D")


if __name__ == '__name__':
    print(__name__)
