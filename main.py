# Importa la clase VEHICULO desde el módulo vehiculo
from vehiculo import VEHICULO
# Importa la clase AUTO desde el módulo auto
from auto import AUTO

# Crea una instancia de VEHICULO con patente "1234" y año 1930
V = VEHICULO("1234", 1930)
# Crea una instancia de AUTO con patente "auto1234" y año 1935
A = AUTO("auto1234", 1935)

# Registra el ingreso del auto A al taller cambiando su estado interno
A.ingresar_al_taller()

# Muestra en consola el atributo patente de la instancia de AUTO
print(A.patente)

# Registra el ingreso del vehículo V al taller cambiando su estado interno
V.ingresar_al_taller()
# Imprime el mensaje indicando que el vehículo ingresó al taller
print("vehiculo en taller")

# Muestra en consola la tarifa por hora calculada para el vehículo V
print(V.tarifa_hora())

# Registra la entrega del vehículo V al cliente cambiando su estado interno
V.entregar_al_cliente()
# Imprime el estado del atributo protegido _en_taller del vehículo V
print(V._en_taller)

# Muestra en consola la patente del vehículo V obtenida mediante get_patente()
print("la patente es: ", V.get_patente())
# Muestra en consola el año del vehículo V obtenido mediante get_anio()
print("el año del vehiculo es: ", V.get_anio())