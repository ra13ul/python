class Empleado:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self._nombre
    
    def set_cedula(self, cedula):
        self.cedula = cedula
    
    def get_cedula(self, cedula):
        return self._cedula
    
    def set_telefono(self, telefono):
        self.telefono = telefono

    def get_telefono(self):
        return self._telefono
    
class EmpleadoDefinido(Empleado):
    def __init__(self, nombre, cedula, telefono, nPlaza, salario, duracion_contrato):
        
        #constructor de la clase empleado
        super().__init__(nombre, cedula, telefono)

        #Atributos añadidos
        self.nPlaza = nPlaza
        self.salario = salario
        self.duracion_contrato = duracion_contrato

    def set_nPlaza(self, nPlaza):
        self._nPlaza = nPlaza
    def get_nPlaza(self):
        return self._nPlaza
    
    def set_salario(self, salario):
        self._salario = salario
    def get_salario(self):
        return self._salario
    
    def set_duracionContrato(self, duracion_contrato):
        self._duracion_contrato = duracion_contrato
    def get_duracionContrato(self):
        return self._duracion_contrato
    
    #Calaculo del salario
    def calcularSalarioTotal(self):
        return self._salario + (self._salario * 0.02)
    