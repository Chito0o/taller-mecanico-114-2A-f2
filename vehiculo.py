# Definición de la clase llamada Vehiculo
class Vehiculo:
    # Declaración de atributos con sus tipos indicados
    patente: str      # Patente del vehículo (texto)
    anio: int         # Año del vehículo (número entero)
    _en_taller: bool  # Indicador de si está en taller (verdadero o falso)

    # Método constructor para inicializar los atributos de la instancia
    def __init__(self, patente: str, anio: int):
        # Asigna la patente recibida al atributo de la instancia
        self.patente = patente
        # Asigna el año recibido al atributo de la instancia
        self.anio = anio
        # Inicializa el atributo protegido en False (inicia fuera de taller)
        self._en_taller = False

    # Método para registrar el ingreso del vehículo al taller
    def ingresar(self):
        # Cambia el estado _en_taller a True indicando que ingresó al taller
        self._en_taller = True

    # Método para registrar la entrega del vehículo fuera del taller
    def entregar(self):
        # Cambia el estado _en_taller a False indicando que salió del taller
        self._en_taller = False
