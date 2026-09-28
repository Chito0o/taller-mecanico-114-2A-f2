from model.vehiculo import Vehiculo
from modelo import Modelo

class Auto(Vehiculo):
    def __init__(self, patente: str, anio: int, modelo: Modelo, capacidad_maletero: int):
        super().__init__(patente, anio, modelo)
        self.__capacidad_maletero: int = capacidad_maletero

    def tarifa_hora(self) -> int:
        return 25000

