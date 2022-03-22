from abc import ABC, abstractmethod

class Cliente(ABC):
    def __init__(self,nombre):
        self._nombre=nombre
    def obtNombre(self):
        return self._nombre
    @abstractmethod
    def obtIdentificacion(self):
        pass            
