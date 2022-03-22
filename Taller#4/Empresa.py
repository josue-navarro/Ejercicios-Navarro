from Cliente import Cliente

class Empresa(Cliente):
    def __init__(self,nit ,nombre,representante):
        super().__init__(nombre)
        self._nit = nit
        self._representante = representante
    def obtIdentificacion(self):
        return self._nit
    def obtRepresentante(self):
        return self._representante
    def cambiarRepresentante(self,representante):
        self._representante =representante
    
              