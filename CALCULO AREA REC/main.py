"""

Programa: Cálculo del área de un rectángulo
Descripción: Este programa solicita al usuario la base y la altura de un rectángulo,
calcula su área y determina si esta es mayor a un valor establecido. """
print("UNIVERSIDAD ESTATAL AMAZONICA")
print("Autor Juan Carlos Pérez León")
print("Tipos de datos, Identificadores. Implementación ")
print("Cálculo del área de un rectángulo ")
print("Curso 2526-UEA-L-UFB-030-A\n")

from modelo.rectangulo import Rectangulo
from servicio.calculo_area import ServicioCalcul

def main():
    try:
        base = float(input("Ingrese la base del rectángulo (en metros): "))
        altura = float(input("Ingrese la altura del rectángulo (en metros): "))

        rectangulo = Rectangulo(base, altura)
        servicio = ServicioCalculoArea()

        resultado = servicio.evaluar_area(rectangulo)

        print(f"El área del rectángulo es: {resultado['area']} m²")

        if resultado["es_area_grande"]:
            print("El área es mayor al valor de referencia.")
        else:
            print("El área es menor o igual al valor de referencia.")

    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()

