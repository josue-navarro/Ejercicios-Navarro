class Cuenta:
    # creo dos atributos de clase privados pero nos los inicializo
    
    _saldoActual = None
    _saldoMinimo = None
    
    # creo el metodo constructor con sus respectivos parametros

    def __init__(self, numero, tipo, valorInicial):
        
        self._numero = numero
        self._tipo = tipo
        self._saldoActual = valorInicial
        
        #inicializo saldo minimo

        self._saldoMinimo= valorInicial*0.1

    # creo el metodo  consignar  y retirar ,tipo= void (que no retorna nada) con su respectivo parametro
    
    def consignar(self, monto):
        self._saldoActual += monto

    def retirar(self, monto):
        if monto > self._saldoActual- self._saldoMinimo:
            print(f"el monto no puede ser mayor al saldo disponible su saldo es: {self._saldoActual- self._saldoMinimo}")
        else:
            print("transacción exitosa")
            self._saldoActual-= monto
            print(f"su saldo actual es: {self._saldoActual- self._saldoMinimo}")
    
    #creo los metodos get de saldo actual y saldo minimo
    
    def getSaldo(self):
        return self._saldoActual
    def getSaldoMinimo(self):
        return self._saldoMinimo

    #creo el metodo getCapacidadCredito
    def  getCapacidadCredito(self):
        tipoDeCuenta=self._tipo
        tipo1="credito"
        tipo2="ahorro"
        #valido el tipo de cuenta  y calculo su capacidad de credito dependiendo del tipo de cuenta que tenga
        if tipoDeCuenta == tipo1:
            capacidadCredito=self._saldoActual*3
            return capacidadCredito            
        elif tipoDeCuenta ==tipo2:
            capacidadCredito=self._saldoActual-self._saldoMinimo
            return capacidadCredito
        else:
            print("digite un tipo de cuenta valido recuerde que los tipos son (ahorro-credito)")

#creo un objeto con tipo de cuenta  ahorro y pruebo los metodos de la clase
CuentaAhorro= Cuenta(111111,"ahorro",500000)
CuentaAhorro.consignar(500000)
CuentaAhorro.retirar(100000)
CuentaAhorro.retirar(900000)
print(f"su saldo es de: {CuentaAhorro.getSaldo()}")
print(f"su saldo minimo  es de: {CuentaAhorro.getSaldoMinimo()}")
print(f"su capacidad de credito es de  : {CuentaAhorro.getCapacidadCredito()}")

#creo un objeto con tipo de cuenta  credito y pruebo los metodos de la clase

CuentaCredito= Cuenta(111111,"credito",500000)
CuentaCredito.consignar(500000)
CuentaCredito.retirar(100000)
CuentaCredito.retirar(900000)
print(f"su saldo es de: {CuentaCredito.getSaldo()}")
print(f"su saldo minimo  es de: {CuentaCredito.getSaldoMinimo()}")
print(f"su capacidad de credito es de  : {CuentaCredito.getCapacidadCredito()}")
