class Cita :
    #creo un atributo de clase para guardar el valor final 
    _valorFinal=None

    #procedo a crear dicho constructor e inicializar  sus respectivos atributos
    def __init__(self, numero ,tipo,tarifa ):
        self._numero = numero
        self._tipo = tipo
        self._tarifa = tarifa

    #creo los respectivo get de numero ,tarifa y tipo 
    def getNumero(self):
        return self._numero
    def getTarifa(self):
        return self._tarifa
    def getTipo(self):
        if (self._tipo>0) and (self._tipo <4):
            return "General" 
        elif (self._tipo>3) and (self._tipo<6):
            return "Especialista" 
        else:
            return f"el tipo va de 1-5 y usted digito: {self._tipo}"
    def  calcularValorFinal(self):
        #atrapo el tipo de la cita con el getTipo para no repetir la misma validacion hecha en getTipo, procedo a comparar cadenas
        tipo=self.getTipo()
        tipo1="General"
        tipo2="Especialista"
        if ( tipo == tipo1) :
            #calculo el decremento de la tarifa y le doy un valor a _valorFinal
            decremento=self._tarifa*0.5
            self._valorFinal = self._tarifa - decremento
        elif (tipo == tipo2):
            #calculo el Incremento de la tarifa y le doy un valor a _valorFinal
            incremento=self._tarifa*0.5
            self._valorFinal = self._tarifa + incremento
        else:
            return (f"Su tarifa es: {self._tarifa}")
    def __str__ (self):
        return f"El numero de cita es :\t{self._numero}\n"\
        f"Esta cita es de tipo:\t{self.getTipo()}\n"\
        f"Su tarifa es:\t{self._tarifa}\n"\
        f"Pero por se de tipo:{self.getTipo()} queda con un valor final de:{self._valorFinal}\t  \n"

#procedo a crear un objeto con el tipo de cita Especialista  y llamo a sus respectivos metodos    
cita1=Cita(100,5,4500)
cita1.getTipo()
cita1.calcularValorFinal()
print(cita1)

print()

#procedo a crear un objeto con el tipo de cita General y llamo a sus respectivos metodos
cita2=Cita(100,1,4500)
cita2.getTipo()
cita2.calcularValorFinal()
print(cita2)
