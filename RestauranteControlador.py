from RestauranteModelo import RestauranteModelo
from RestauranteVista import RestauranteVista


class RestauranteControlador:
    def __init__(self):
        self.modelo = RestauranteModelo()
        self.vista = RestauranteVista()

    def iniciar(self):
        opcion = 0
        while opcion != 4:
            opcion = self.vista.mostrar_menu()

            if opcion == 1:
                self.registrar_plato()
            elif opcion == 2:
                self.mostrar_platos()
            elif opcion == 3:
                self.servir_plato()
            elif opcion == 4:
                self.vista.mostrar_mensaje(
                    "¡Gracias por usar el sistema del Restaurante Sabor Cuencano!"
                )
            else:
                self.vista.mostrar_mensaje("Opción no válida")

    def registrar_plato(self):
        nombre, precio, porciones = self.vista.pedir_datos_plato()
        codigo = self.modelo.agregar_plato(nombre, precio, porciones)
        self.vista.mostrar_mensaje(f"Registrado con el código {codigo}.")

    def mostrar_platos(self):
        self.vista.mostrar_tabla_platos(self.modelo.platos)

    def servir_plato(self):
        codigo = self.vista.pedir_codigo()
        plato = self.modelo.buscar_plato(codigo)

        if plato is None:
            self.vista.mostrar_mensaje("Error: no existe ese código.")
        else:
            cantidad = self.vista.pedir_cantidad()
            exito, mensaje = plato.servir(cantidad)
            self.vista.mostrar_mensaje(mensaje)
