from modelo.rectangulo import Rectangulo

class ServicioCalculoArea:
    def __init__(self, area_referencia: int = 200):
        self.area_referencia = area_referencia

    def evaluar_area(self, rectangulo: Rectangulo) -> dict:
        if rectangulo.base <= 0 or rectangulo.altura <= 0:
            raise ValueError("La base y la altura deben ser mayores que cero.")

        area = rectangulo.calcular_area()
        es_mayor = area > self.area_referencia

        return {
            "area": area,
            "es_area_grande": es_mayor
        }
