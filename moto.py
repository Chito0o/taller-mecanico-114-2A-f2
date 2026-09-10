# Importa la clase padre VEHICULO desde el módulo vehiculo
from vehiculo import VEHICULO

# Definición de la clase moto que hereda de la clase VEHICULO
class moto(VEHICULO):
    # Método constructor que se ejecuta al crear un nuevo objeto de la clase moto
    def __init__(self, patente: str, anio: int, marca: str, modelo: str):
        # Llama al constructor de la clase padre (VEHICULO) pasando la patente y el año
        super().__init__(patente, anio)
        # Asigna el valor del parámetro marca al atributo de instancia self.marca con tipo de dato str
        self.marca: str = marca
        # Asigna el valor del parámetro modelo al atributo de instancia self.modelo con tipo de dato str
        self.modelo: str = modelo