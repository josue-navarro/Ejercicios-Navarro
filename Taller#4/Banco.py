from Persona  import Persona
from Empresa  import Empresa

class Banco:
    _clientes=[]
    _numeroClientes=0
    def __init__(self,nombreBanco):
        self._nombreBanco = nombreBanco
    def obtNombreBanco(self):
        return self._nombreBanco
    def cambiarNombreBanco(self , nombre):
        self._nombreBanco = nombre
    def addCliente(self,clientes):        
        for i in range(len(clientes)):
            self._clientes.append(clientes[i])
            self._numeroClientes+=1
    def obtNumClientes(self):
        return self._numeroClientes
    def getClientes(self): 
        NombreClientes=[]
        CedulaPersonas=[]
        DatosEmpresa={}
        NombreClientesMenores=[]
        ClienteMasJoven={"nombre":"", "edad":1000}
        ClienteMasViejo={"nombre":"", "edad":0}

        for i in range(self._numeroClientes):

            
            NombreClase=type(self._clientes[i]).__name__
            
            if  NombreClase == "Empresa" :
                NombreClientes.append(self._clientes[i].obtNombre())
                DatosEmpresa[f"{self._clientes[i].obtNombre()}"]= self._clientes[i].obtRepresentante()

            elif NombreClase == "Persona":
                NombreClientes.append(self._clientes[i].obtNombre())            
                CedulaPersonas.append(self._clientes[i].obtIdentificacion())
                
                if self._clientes[i].obtEdad()<18 :
                
                    NombreClientesMenores.append(self._clientes[i].obtNombre())                        
                if  ClienteMasJoven["edad"]>self._clientes[i].obtEdad():
                
                    ClienteMasJoven["nombre"]=self._clientes[i].obtNombre()
                    ClienteMasJoven["edad"]=self._clientes[i].obtEdad()
                if  ClienteMasViejo["edad"]<self._clientes[i].obtEdad():
                    ClienteMasViejo["nombre"]=self._clientes[i].obtNombre()
                    ClienteMasViejo["edad"]=self._clientes[i].obtEdad()

            else:
                print("huboun error el objeto no pertenece a ninguna clase")
            
        return (
            f"los nombre de todos los clientes son: {NombreClientes}\n"\
            f"los datos de las empresa son: {DatosEmpresa}\n"\
            f"Los clientes menores de edad son : {NombreClientesMenores}\n"\
            f"El cliente mas joven es: {ClienteMasJoven}\n"\
            f"EL cliente mas viejo es: {ClienteMasViejo}"            
        )
    def buscarCliente(self,posicion):
        if posicion>len(self._clientes):
            print("no existe tal registro")
        else:
            return(self._clientes[posicion])            
persona1 =Persona(111,18,"jose#1")
persona2 =Persona(112,1,"jose#2")
persona3 =Persona(113,12,"jose#3")
persona4 =Persona(114,95,"jose#4")
persona5 =Persona(115,66,"jose#5")
persona6 =Persona(116,0,"jose#6")
clientes=[]
clientes.append(persona1)
clientes.append(persona2)
clientes.append(persona3)
clientes.append(persona4)
clientes.append(persona5)
clientes.append(persona6)
empresa1=Empresa(11124,"thanos.com","mario")
empresa2=Empresa(11124,"its mario","luigi")
empresa1.cambiarRepresentante("browser")
clientes.append(empresa1)
clientes.append(empresa2)


banquito=Banco("miami")
banquito.addCliente(clientes)

print(banquito.getClientes())




