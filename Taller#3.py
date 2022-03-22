class Cuenta:
    
    _saldoActual = None
    _saldoMinimo = None
    

    def __init__(self, numero, tipo, valorInicial):
        
        self._numero = numero
        self._tipo = tipo
        self._saldoActual = valorInicial
        

        self._saldoMinimo= valorInicial*0.1

    
    def consignar(self, monto):
        self._saldoActual += monto

    def retirar(self, monto):
        if monto > self._saldoActual- self._saldoMinimo:
            print(f"el monto no puede ser mayor al saldo disponible su saldo es: {self._saldoActual- self._saldoMinimo}")
        else:
            print("transacción exitosa")
            self._saldoActual-= monto
            print(f"su saldo actual es: {self._saldoActual- self._saldoMinimo}")
    
    
    def getSaldo(self):
        return self._saldoActual
    def getSaldoMinimo(self):
        return self._saldoMinimo

    def  getCapacidadCredito(self):
        tipoDeCuenta=self._tipo
        tipo1="credito"
        tipo2="ahorro"
        if tipoDeCuenta == tipo1:
            capacidadCredito=self._saldoActual*3
            return capacidadCredito            
        elif tipoDeCuenta ==tipo2:
            capacidadCredito=self._saldoActual-self._saldoMinimo
            return capacidadCredito
        else:
            print("digite un tipo de cuenta valido recuerde que los tipos son (ahorro-credito)")

CuentaAhorro= Cuenta(111111,"ahorro",500000)
CuentaAhorro.consignar(500000)
CuentaAhorro.retirar(100000)
CuentaAhorro.retirar(900000)
print(f"su saldo es de: {CuentaAhorro.getSaldo()}")
print(f"su saldo minimo  es de: {CuentaAhorro.getSaldoMinimo()}")
print(f"su capacidad de credito es de  : {CuentaAhorro.getCapacidadCredito()}")


CuentaCredito= Cuenta(111111,"credito",500000)
CuentaCredito.consignar(500000)
CuentaCredito.retirar(100000)
CuentaCredito.retirar(900000)
print(f"su saldo es de: {CuentaCredito.getSaldo()}")
print(f"su saldo minimo  es de: {CuentaCredito.getSaldoMinimo()}")
print(f"su capacidad de credito es de  : {CuentaCredito.getCapacidadCredito()}")
