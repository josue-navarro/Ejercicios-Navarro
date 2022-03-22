from Cliente import Cliente

class Persona (Cliente):
    def __init__(self,cedula,edad,nombre):        
        super().__init__(nombre)
        self._cedula = cedula
        self._edad = edad 
    def obtIdentificacion(self):
        return self._cedula
    def obtEdad(self):
        return self._edad
    def cumplirAños(self):
        self._edad+=1
