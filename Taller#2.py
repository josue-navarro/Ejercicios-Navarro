from random import  randrange



class Bus :
    _pasajerosActuales=0
    _totalPasajeros=0
    def __init__(self,placa,capacidadPasajeros,precioPasaje):
        self._placa=placa
        self._capacidadPasajeros=capacidadPasajeros
        self._precioPasaje=precioPasaje
    def getPlaca(self):
        return self._placa
    def getCapacidad(self):
        return self._capacidadPasajeros
    def getPrecioPasaje(self):
        return self._precioPasaje
    def getPasajerosTotales(self):
        return self._totalPasajeros
    def getPasajerosActuales(self):
        return self._pasajerosActuales
    def subirPasajeros(self):        
        if(self._pasajerosActuales<self._capacidadPasajeros): 
            self._pasajerosActuales += 1  
            self._totalPasajeros +=1    
        else:
            print("capacidad del bus llena")
    def bajarPasajeros(self):
        if(self._pasajerosActuales <1):
            print("no quedan pasajeros por bajar")
        else:
            self._pasajerosActuales -= 1
    def getDineroAcumulado(self):
        return self._totalPasajeros*self._precioPasaje

buseta =Bus("xmn-opr",25,2500)

#creo 2 test uno basico y otro donde lo hago de forma mas dinamica la subida y bajada de pasajeros ademas de que muestro los pasajeros actuales y cuantos subieron
#----test1------
#subimos 25 pasajeros pero como la capacidad es 25 no dejara subir a 1 pasajero
# for i in range(26):
#     buseta.subirPasajeros()
# #bajamos 26 pasajeros pero como la cantidad de pasajeros actuales es inferior a 26 nos sale que no hay mas nada por bajar
# for i in range(26):
#     buseta.bajarPasajeros()
# #mostramos por consola cuanto dinero se acumulo
# print(f"el dinero acumulado del dia fue {buseta.getDineroAcumulado()} pesos")

