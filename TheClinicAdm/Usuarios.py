class Usuarios:
    def __init__(self, id_usuario, nombre_usuario, apellido_usuario, edad_usuario, dni_usuario, email_usuario,
                 contraseña_usuario, domicilio_usuario, fecha_nac_usuario, provincia_usuario, barrio_usuario,
                 notas_usuario, obra_soc_usuario, analisis_usuario, clinico_usuario, paciente_usuario, pagos_usuario,
                 permiso_usuario):

        self._id_usuario = id_usuario
        self._nombre_usuario = nombre_usuario
        self._apellido_usuario = apellido_usuario
        self._edad_usuario = edad_usuario
        self._dni_usuario = dni_usuario
        self._email_usuario = email_usuario
        self._contraseña_usuario = contraseña_usuario
        self._domicilio_usuario = domicilio_usuario
        self._fecha_nac_usuario = fecha_nac_usuario
        self._provincia_usuario = provincia_usuario
        self._barrio_usuario = barrio_usuario
        self._notas_usuario = notas_usuario
        self._obra_soc_usuario = obra_soc_usuario
        self._analisis_usuario = analisis_usuario
        self._clinico_usuario = clinico_usuario
        self._paciente_usuario = paciente_usuario
        self._pagos_usuario = pagos_usuario
        self._permiso_usuario = permiso_usuario

    @property
    def id_usuario(self):
        return self._id_usuario

    @id_usuario.setter
    def id_usuario(self, id_usuario):
        if self._validar_char(id_usuario):
            self._id_usuario = id_usuario
        else:
            print("Error Ingreso Nro.ID, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def nombre_usuario(self):
        return self._nombre_usuario

    @nombre_usuario.setter
    def nombre_usuario(self, nombre_usuario):
        if self._validar_inte(nombre_usuario):
            self._nombre_usuario = nombre_usuario
        else:
            print("Error Ingreso Nombre, No Tiene Que Ser Un Numero!!! :D")

    @property
    def apellido_usuario(self):
        return self._apellido_usuario

    @apellido_usuario.setter
    def apellido_usuario(self, apellido_usuario):
        if self._validar_inte(apellido_usuario):
            self._apellido_usuario = apellido_usuario
        else:
            print("Error Ingreso Nombre, No Tiene Que Ser Un Numero!!! :D")

    @property
    def edad_usuario(self):
        return self._edad_usuario

    @edad_usuario.setter
    def edad_usuario(self, edad_usuario):
        if self._validar_inte(edad_usuario):
            self._edad_usuario = edad_usuario
        else:
            print("Error Ingreso Edad, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def dni_usuario(self):
        return self._dni_usuario

    @dni_usuario.setter
    def dni_usuario(self, dni_usuario):
        if self._validar_inte(dni_usuario):
            self._dni_usuario = dni_usuario
        else:
            print("Error Ingreso DNI, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def email_usuario(self):
        return self._email_usuario

    @email_usuario.setter
    def email_usuario(self, email_usuario):
        self._email_usuario = email_usuario

    @property
    def contraseña_usuario(self):
        return self._contraseña_usuario

    @contraseña_usuario.setter
    def contraseña_usuario(self, contraseña_usuario):
        self._contraseña_usuario = contraseña_usuario

    @property
    def domicilio_usuario(self):
        return self._domicilio_usuario

    @domicilio_usuario.setter
    def domicilio_usuario(self, domicilio_usuario):
        self._domicilio_usuario = domicilio_usuario

    @property
    def fecha_nac_usuario(self):
        return self._fecha_nac_usuario

    @fecha_nac_usuario.setter
    def fecha_nac_usuario(self, fecha_nac_usuario):
        self._fecha_nac_usuario = fecha_nac_usuario

    @property
    def provincia_usuario(self):
        return self._provincia_usuario

    @provincia_usuario.setter
    def provincia_usuario(self, provincia_usuario):
        self._provincia_usuario = provincia_usuario

    @property
    def barrio_usuario(self):
        return self._barrio_usuario

    @barrio_usuario.setter
    def barrio_usuario(self, barrio_usuario):
        self._barrio_usuario = barrio_usuario

    @property
    def notas_usuario(self):
        return self._notas_usuario

    @notas_usuario.setter
    def notas_usuario(self, notas_usuario):
        self._notas_usuario = notas_usuario

    @property
    def obra_soc_usuario(self):
        return self._obra_soc_usuario

    @obra_soc_usuario.setter
    def obra_soc_usuario(self, obra_soc_usuario):
        self._obra_soc_usuario = obra_soc_usuario

    @property
    def analisis_usuario(self):
        return self._analisis_usuario

    @analisis_usuario.setter
    def analisis_usuario(self, analisis_usuario):
        if self._validar_char(analisis_usuario):
            self._analisis_usuario = analisis_usuario
        else:
            print("Error Ingreso De Nro.Analisis, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def clinico_usuario(self):
        return self._clinico_usuario

    @clinico_usuario.setter
    def clinico_usuario(self, clinico_usuario):
        if self._validar_char(clinico_usuario):
            self._clinico_usuario = clinico_usuario
        else:
            print("Error Ingreso Nro.Clinico, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def paciente_usuario(self):
        return self._paciente_usuario

    @paciente_usuario.setter
    def paciente_usuario(self, paciente_usuario):
        if self._validar_char(paciente_usuario):
            self._paciente_usuario = paciente_usuario
        else:
            print("Error Ingreso Nro.Paciente, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def pagos_usuario(self):
        return self._pagos_usuario

    @pagos_usuario.setter
    def pagos_usuario(self, pagos_usuario):
        if self._validar_char(pagos_usuario):
            self._pagos_usuario = pagos_usuario
        else:
            print("Error Ingreso Nro.Pago, No Tiene Que Ser Un Caracter!!! :D")

    @property
    def permiso_usuario(self):
        return self._permiso_usuario

    @permiso_usuario.setter
    def permiso_usuario(self, permiso_usuario):
        if self._validar_char(permiso_usuario):
            self._permiso_usuario = permiso_usuario
        else:
            print("Error Ingreso Nro.Permiso, No Tiene Que Ser Un Caracter!!! :D")

    def __str__(self):
        return f'[ID: {self._id_usuario},Nombre: {self._nombre_usuario},Apellido: {self._apellido_usuario},' \
               f'Edad: {self._edad_usuario},Dni: {self._dni_usuario},Email: {self._email_usuario}, ' \
               f'Contraseña: {self._contraseña_usuario},Domicilio: {self._domicilio_usuario}, ' \
               f'F.Nacimiento: {self._fecha_nac_usuario},Provincia: {self._provincia_usuario},' \
               f'Barrio: {self._barrio_usuario},Notas: {self._notas_usuario},O.Social: {self._obra_soc_usuario}, ' \
               f'Nro.Analisis: {self._analisis_usuario},Nro.Clinico: {self.clinico_usuario},' \
               f'Nro.Paciente: {self._paciente_usuario},Nro.Pago: {self._pagos_usuario},' \
               f'Nro.permiso: {self._permiso_usuario} ]'

    def _validar_char(self, char):
        return True if ('a' <= char <= 'z') or ('A' <= char <= 'Z') else False

    def _validar_inte(self, inte):
        return True if (0 <= inte <= 0) else False


if __name__ == '__name__':
    print(__name__)
