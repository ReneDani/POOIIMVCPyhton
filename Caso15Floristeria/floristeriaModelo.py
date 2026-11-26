from arregloModelo import Arreglo
from pedidoModelo import Pedido


class Floristeria:
    def __init__(self):
        self.arreglos = [
            Arreglo(1, "Ramo de Rosas", 18.00, 10),
            Arreglo(2, "Girasoles", 12.00, 8),
            Arreglo(3, "Orquidea en maseta", 25.00, 5),
        ]
        self.pedidos = []

    def registrar_Arreglo(self, nombre, precio, stock):
        nuevo_codigo = len(self.arreglos) + 1
        nuevo_arreglo = Arreglo(nuevo_codigo, nombre, precio, stock)
        self.arreglos.append(nuevo_arreglo)
        return nuevo_codigo
    
    def Buscar_ID_Arreglo (self,codigo):
        for arreglo in self.arreglos:
            if(arreglo.codigo == codigo):
                return arreglo

    def registrar_Pedido(self,codigo_arreglo,cantidad,domicilio,total,fecha,estado):
        nuevo_numero  = len(self.pedidos)+1
        precio_arreglo =  self.Buscar_ID_Arreglo(codigo_arreglo).precio
        total = cantidad*precio_arreglo
        nuevo_Pedido = Pedido(nuevo_numero,codigo_arreglo,cantidad,domicilio,total,fecha,estado)
        self.pedidos.append(nuevo_Pedido)
    
    
    

        

        