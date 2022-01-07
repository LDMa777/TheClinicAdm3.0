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
        self._id_permiso = id_permiso

    @property
    def nombre_permiso(self):
        return self._nombre_permiso

    @nombre_permiso.setter
    def nombre_permiso(self, nombre_permiso):
        self._nombre_permiso = nombre_permiso