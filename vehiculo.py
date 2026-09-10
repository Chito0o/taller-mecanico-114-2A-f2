# Definición de la clase llamada VEHICULO
class VEHICULO:
    # Método constructor para inicializar los atributos de la instancia
    def __init__(self, patente: str, anio: int):
        # Asigna la patente recibida al atributo de la instancia (texto)
        self.patente: str = patente
        # Asigna el año recibido al atributo de la instancia (número entero)
        self.anio: int = anio
        # Inicializa el atributo protegido _en_taller en False (inicia fuera de taller)
        self._en_taller: bool = False

    # Método para registrar el ingreso del vehículo al taller
    def ingresar_al_taller(self):
        # Cambia el estado _en_taller a True indicando que ingresó al taller
        self._en_taller = True

    # Método para registrar la entrega del vehículo fuera del taller
    def entregar_al_cliente(self):
        # Cambia el estado _en_taller a False indicando que salió del taller
        self._en_taller = False

    # Método que retorna la tarifa por hora del vehículo
    def tarifa_hora(self) -> int:
        # Retorna el valor entero 5000 correspondiente a la tarifa por hora
        return 5000

    # Método para obtener la patente del vehículo
    def get_patente(self) -> str:
        # Retorna el valor del atributo patente
        return self.patente

    # Método para obtener el año del vehículo
    def get_anio(self) -> int:
        # Retorna el valor del atributo anio
        return self.anio

