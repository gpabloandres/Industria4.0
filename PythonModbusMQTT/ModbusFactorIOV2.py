from pymodbus.client import ModbusTcpClient
import time

# Crear una instancia del cliente Modbus TCP
PLC = ModbusTcpClient("192.168.1.17")

# Conectar al PLC
PLC.connect()

# Bucle infinito
while True:
    # Leer el estado del sensor en el input 0
    result = PLC.read_discrete_inputs(0, count=1)
    
    # Verificar si la lectura fue exitosa
    if result.isError():
        print("Error al leer el sensor. Reintentando...")
        time.sleep(0.5)
        continue
    
    sensor_state = result.bits[0]
    
    # Si el sensor está activado (True), interrumpir el programa
    if sensor_state:
        print("Sensor activado. Interrumpiendo el programa.")
        break

    print("-----TABLERO DE CONTROL----")
    print("ENCENDER (1)")
    print("APAGAR (0)")
    print("___________________________")
    
    # Leer la opción del usuario
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        PLC.write_coil(0, True)
        print("Dispositivo encendido.")
    elif opcion == "0":
        PLC.write_coil(0, False)
        print("Dispositivo apagado.")
    else:
        print("Opción incorrecta! Vuelva a intentarlo.")
    
    # Esperar un momento antes de la siguiente iteración
    time.sleep(0.1)

# Desconectar del PLC
PLC.close()