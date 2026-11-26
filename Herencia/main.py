from estudiante import Estudiante
from docente import Docente


def main():
    est1 = Estudiante(
        "0102030405", "Ana", "Gómez", "0991112233", "ana@email.com",
        20, "Av. Loja", "Desarrollo de Software", [9.0, 8.5, 9.5]
    )
    est2 = Estudiante(
        "0106070809", "Luis", "Torres", "0982223344", "luis@email.com",
        17, "Av. Solano", "Contabilidad", [7.0, 6.5, 8.0]
    )
    est3 = Estudiante(
        "0109101112", "María", "Paredes", "0993334455", "maria@email.com",
        22, "El Vergel", "Diseño Gráfico", [10.0, 9.5, 9.0]
    )
    est4 = Estudiante(
            "0107252389", "Rene", "Dominguez", "0987873805", "rene.nover@gmail.com",
            22, "El Vergel", "Diseño Gráfico", [10.0, 9.5, 9.0]
        )
    est5 = Estudiante(
                "0107252388", "Gwen", "Dominguez", "0987873805", "gwen.nover@gmail.com",
                22, "El Vergel", "Diseño Gráfico", [10.0, 9.5, 9.0]
            )
    doc1 = Docente(
        "0103040506", "Carlos", "Méndez", "0984445566", "carlos@instituto.edu.ec",
        38, "Av. Ordóñez Lasso", 15.50, "Programación Orientada a Objetos", 40
    )
    doc2 = Docente(
        "0107080910", "Sofía", "Vintimilla", "0995556677", "sofia@instituto.edu.ec",
        42, "Baños", 18.00, "Bases de Datos", 35
    )

    doc3 = Docente(
        "0101121314", "Jorge", "Andrade", "0988889900", "jorge@instituto.edu.ec",
        45, "El Batán", 16.00, "Ingeniería de Software", 30
    )
    doc4 = Docente(
        "0105161718", "Elena", "Salazar", "0999990011", "elena@instituto.edu.ec",
        34, "Ricaurte", 14.50, "Estructura de Datos", 25
    )
    doc5 = Docente(
        "0109202122", "Roberto", "Orellana", "0980001122", "roberto@instituto.edu.ec",
        50, "San Joaquín", 20.00, "Redes y Telecomunicaciones", 40
    )


    print("=== REGISTRO DE ESTUDIANTES ===")
    estudiantes = [est1, est2, est3,est4,est5]

    for est in estudiantes:
        print(est)  
        print(f" -> Promedio calculado: {est.calcular_notas():.2f}")
        print(f" -> Validación edad/carrera: {est.validar_edad()}")
        print("-" * 60)


    print("\n=== REGISTRO DE DOCENTES ===")
    docentes = [doc1, doc2,doc3,doc4,doc5]

    for doc in docentes:
        print(doc)  
        print(f" -> Salario total a pagar: ${doc.calcular_salario():.2f}")
        print(f" -> Validación edad: {doc.validar_edad()}")
        print("-" * 60)


if __name__ == "__main__":
    main()