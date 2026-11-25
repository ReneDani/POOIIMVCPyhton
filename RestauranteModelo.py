class Plato:
    def __init__(self, codigo, nombre, precio, porciones):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.porciones = porciones

    def servir(self, cantidad):
        if cantidad <= 0:
            return False, "Error: la cantidad debe ser mayor que cero."
        if cantidad > self.porciones:
            return False, f"Error: solo hay {self.porciones} porciones."

        self.porciones -= cantidad
        return True, f"Listo. Quedan {self.porciones} porciones."

    def __str__(self):
        return f"{self.codigo:<8} | {self.nombre:<18} | ${self.precio:<8.2f} | {self.porciones:<10}"


class RestauranteModelo:
    def __init__(self):
        self.platos = [
            Plato(1, "Mote pillo", 3.50, 30),
            Plato(2, "Hornado", 6.00, 20)
        ]

    def agregar_plato(self, nombre, precio, porciones):
        nuevo_codigo = len(self.platos) + 1
        nuevo_plato = Plato(nuevo_codigo, nombre, precio, porciones)
        self.platos.append(nuevo_plato)
        return nuevo_codigo

    def buscar_plato(self, codigo):
        for plato in self.platos:
            if plato.codigo == codigo:
                return plato
        return None