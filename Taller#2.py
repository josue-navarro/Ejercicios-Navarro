from random import  randrange



class Bus :
    #creo dos atributos de clase privados
    _pasajerosActuales=0
    _totalPasajeros=0
    #procedo a crear el metodo constructor e inicializar sus respectivas variables de instancia
    def __init__(self,placa,capacidadPasajeros,precioPasaje):
        self._placa=placa
        self._capacidadPasajeros=capacidadPasajeros
        self._precioPasaje=precioPasaje
    #creo los metodos get de placa,capacidad,precio pasaje ,pasajeros totales y pasajeros actuales        
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
    #creo lo metodos subir pasajero y bajar pasajero (estos metodos modifican a _pasajerosActuales)
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
    #creo el metodo que devuelve el total de todos los pasajes
    def getDineroAcumulado(self):
        return self._totalPasajeros*self._precioPasaje

#creo el objeto y le paso sus respectivos argumentos
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

#----test2-----
# for i in range (25):
#     opcion=randrange(3)
#     if opcion==1:
#         buseta.subirPasajeros()
#     else:
#         buseta.bajarPasajeros()
# print("la cantidad de pasajeros actuales es : ",buseta.getPasajerosActuales())
# print("la cantidad de pasajeros totales es: ",buseta.getPasajerosTotales())
# print(f"el dinero acumulado del dia fue {buseta.getDineroAcumulado()} pesos")
