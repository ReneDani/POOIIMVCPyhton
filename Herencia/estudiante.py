from persona import Persona


class Estudiante(Persona):
    def __init__(self, cedula, nombre, apellido, celular, correo, edad, direccion, carrera, notas):
        super().__init__(cedula, nombre, apellido, celular, correo, edad, direccion)
        self.carrera = carrera
        self.notas = notas  # Se espera una lista, ej: [8.5, 9.0, 7.5]

    def calcular_notas(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)

    def validar_edad(self):
        return super().validar_edad(), self.carrera

    def __str__(self):
        # Convierte la lista [8.5, 9.0, 7.5] en un texto limpio: "8.5, 9.0, 7.5"
        notas_texto = ", ".join(str(nota) for nota in self.notas)
        promedio = self.calcular_notas()
        return (
            f"{super().__str__()} | Carrera: {self.carrera} | "
            f"Notas: [{notas_texto}] | Promedio: {promedio:.2f}"
        )

    
      
         