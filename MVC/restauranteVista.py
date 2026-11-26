class RestauranteVista:
    def mostrar_menu(self):
        print("""
=== RESTAURANTE SABOR CUENCANO ===
1. Registrar plato
2. Mostrar platos
3. Servir platos
4. Salir""")
        try:
            return int(input("Seleccione una opción: "))
        except ValueError:
            return -1

    def pedir_datos_plato(self):
        while True:
            nombre = input("Nombre del plato: ").strip()
            if nombre:
                break
            print("Error: el nombre del plato no puede estar vacío.")

        while True:
            try:
                precio = float(input("Precio: "))
                if precio > 0:
                    break
                print("Error: el precio debe ser mayor a 0.")
            except ValueError:
                print("Error: ingrese un precio numérico válido (ej. 3.50).")

        while True:
            try:
                porciones = int(input("Porciones: "))
                if porciones > 0:
                    break
                print("Error: las porciones deben ser un número entero mayor a 0.")
            except ValueError:
                print("Error: ingrese un número entero válido para las porciones.")

        return nombre, precio, porciones

    def mostrar_tabla_platos(self, platos):
        print(
            "\n" + f"{'Código':<8} | {'Nombre':<18} | {'Precio':<9} | {'Porciones':<10}"
        )
        print("-" * 54)
        for plato in platos:
            print(plato)

    def pedir_codigo(self):
        while True:
            try:
                return int(input("Código del plato: "))
            except ValueError:
                print("Error: ingrese un código numérico válido.")

    def pedir_cantidad(self):
        while True:
            try:
                return int(input("Cantidad de porciones a servir: "))
            except ValueError:
                print("Error: ingrese una cantidad entera válida.")

    def mostrar_mensaje(self, mensaje):
        print(mensaje)

