class Persona:
    def __init__(self,cedula,nombre,apellido,celular,correo,edad,direccion):
        self.cedula =cedula
        self.nombre =nombre
        self.apellido =apellido
        self.edad = edad
        self.celular = celular
        self.correo = correo
        self.direccion = direccion
    def validar_edad(self):
        if(self.edad >= 18):
          return "Es mayor de edad"
        else:
            return "Es nenor de edad"

    def __str__(self):
        return (
            f"{self.cedula:<12} | {self.nombre:<15} | {self.apellido:<15} | "
            f"{self.edad:<5} | {self.celular:<12} | {self.correo:<25} | {self.direccion:<20}"
        )

      
    
        