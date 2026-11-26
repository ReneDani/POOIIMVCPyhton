from persona import Persona


class Docente(Persona):
    def __init__(self, cedula, nombre, apellido, celular, correo, edad, direccion, salario, materia, nhoras):
        super().__init__(cedula, nombre, apellido, celular, correo, edad, direccion)
        self.salario = salario  # Valor que gana por hora (ej. 15.50)
        self.materia = materia
        self.nhoras = nhoras    # Número de horas trabajadas (ej. 40)

    def calcular_salario(self):
        return self.salario * self.nhoras

    def __str__(self):
        salario_total = self.calcular_salario()
        return (
            f"{super().__str__()} | Materia: {self.materia} | "
            f"Valor/Hora: ${self.salario:.2f} | Horas: {self.nhoras} | "
            f"Salario Total: ${salario_total:.2f}"
        )

